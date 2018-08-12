#======================Imports========================
from IModel import IModel
import requests
import json
import sys
from defines import APIKEY, FILTER, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_CLIENT_REDIRECT_URI
import html.parser
from datetime import datetime,timezone,time,timedelta

import praw
import pendulum
#=====================================================

#====================AppModel=========================
class AppModel(IModel):
    """
    This class extends the IModel abstract base class and
    interacts with both the Stack Exchange API and Reddit
    API (through PRAW). 

    Attributes:
        seBaseURL: The base URL for the Stack Exchange API
        reddit: The PRAW Reddit instance for all Reddit API calls
    """
    seBaseURL = "https://api.stackexchange.com/2.2/"
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, redirect_uri=REDDIT_CLIENT_REDIRECT_URI, user_agent="Karma Farma")

    def __init__(self, app):
        """
	    Initialization of the Model class
	    @params
	        Web app initialized by Flask
	    return
	        N/A
        """
        self.arg = app
    
    def getSites(self):
        """
        This method gets all available subsites on Stack Exchange
        for the user to select which one to farm.
        
        Returns:
            results: List of sites on Stack Exchange
        """
        page = 1 #API results paginated results so we start from page 1
        results = []
        hasMore = True #API response includes this field to indicate whether there's a next page or not
        params={"key": APIKEY, "filter": "!6Oe*vJ1yH.MGi"}
        while hasMore:
            params['page'] = page
            res = requests.get(self.seBaseURL + "sites", params=params)
            if res.status_code == 200:
                resJSON = res.json()
                for item in resJSON['items']:
                    #Unescape any special HTML characters for rendering
                    item['name'] = html.parser.unescape(item['name'])
                    results.append(item)
                hasMore = resJSON['has_more']
                page += 1
            else:
                print("An error has occured when making API call")
                sys.exit(1)
        return results
    
    def getNoAnswerQuestions(self, site):
        """
        This method returns questions on Stack Exchange
        with no answers for posts that are maximum of 12 hours
        old. The API response is filtered based on view count and
        time difference.

        Parameters:
            site: The Stack Exchange site to fetch questions with
                  no answers
        
        Returns:
            best, good, okay: 3 separate lists after being filtered
                              based on potential of getting karma.
        """
        page = 1 #API response is paginated so start at page 1
        best = [] #Questions with highest potential to gain karma
        good = [] #Questions with good potential to gain karma
        okay = [] #Questions with so-so potential to gain karma
        hasMore = True #Determine whether paginated responses are done
        params = {
            "key": APIKEY,
            "order": "desc",
            "sort": "creation",
            "site": site,
            "min": int((datetime.now() - timedelta(hours=12)).timestamp()),
            "filter": "withbody"
        }

        while hasMore:
            params['page'] = page
            res = requests.get(self.seBaseURL + "questions/no-answers", params=params)
            if res.status_code == 200:
                resJSON = res.json()
                for item in resJSON['items']:
                    item['title'] = html.parser.unescape(item['title'])
                    item['owner']['display_name'] = html.parser.unescape(item['owner']['display_name'])

                    viewCount = item['view_count']

                    dt = pendulum.from_timestamp(item['creation_date'])
                    now = pendulum.now('UTC')
                    difMinutes = dt.diff(now).in_minutes()
                    item['creation_date'] = dt.diff_for_humans(now, absolute=True) + " ago"

                    """
                    timedif = datetime.now() - datetime.fromtimestamp(item['creation_date'])
                    difHours, remainder = divmod(timedif.total_seconds(), 3600)
                    difMinutes, difSeconds = divmod(remainder, 60)

                    item['creation_date'] = "Created {0} hours, {1} minutes, {2} seconds ago".format(int(difHours), int(difMinutes), int(difSeconds))
                    """

                    #Filter the results based on view counts and how long has it been till it hasn't been answered
                    if viewCount >= 50 and difMinutes < 240:
                        best.append(item)
                    elif viewCount >= 10 and viewCount < 50 and difMinutes < 60:
                        good.append(item)
                    else:
                        okay.append(item)

                hasMore = resJSON['has_more']
                page += 1
            else:
                print("An error has occured when making API call")
                sys.exit(1)

        return (best,good,okay)

    def userApproveApp(self):
        return self.reddit.auth.url(['*'], '...', 'permanent')
    
    def getUserSubreddits(self, code):
        if code != None:
            self.reddit.auth.authorize(code)
        return list(self.reddit.user.subreddits(limit=None))
    
    def getSubredditNew(self, sr):
        submissions = list()
        for submission in self.reddit.subreddit(sr).new():
            post = dict()
            post['title'] = submission.title
            post['num_comments'] = submission.num_comments
            post['url'] = "https://www.reddit.com" + submission.permalink

            dt = pendulum.from_timestamp(submission.created_utc)
            post['created'] = dt.diff_for_humans(pendulum.now('UTC'), absolute=True) + " ago"

            submissions.append(post)

        return list(submissions)