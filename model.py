from IModel import IModel
import requests
import json
import sys
from defines import APIKEY, FILTER, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_CLIENT_REDIRECT_URI
import html.parser
from datetime import datetime,timezone,time,timedelta

import praw

class AppModel(IModel):
    baseURL = "https://api.stackexchange.com/2.2/"
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
        page = 1
        results = []
        hasMore = True
        params={"key": APIKEY, "filter": "!6Oe*vJ1yH.MGi"}
        while hasMore:
            params['page'] = page
            res = requests.get(self.baseURL + "sites", params=params)
            if res.status_code == 200:
                resJSON = res.json()
                for item in resJSON['items']:
                    item['name'] = html.parser.unescape(item['name'])
                    results.append(item)
                hasMore = resJSON['has_more']
                page += 1
            else:
                print("An error has occured when making API call")
                sys.exit(1)
        return results
    
    def getNoAnswerQuestions(self, site):
        page = 1
        best = []
        good = []
        okay = []
        hasMore = True
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
            res = requests.get(self.baseURL + "questions/no-answers", params=params)
            if res.status_code == 200:
                resJSON = res.json()
                for item in resJSON['items']:
                    item['title'] = html.parser.unescape(item['title'])
                    item['owner']['display_name'] = html.parser.unescape(item['owner']['display_name'])

                    viewCount = item['view_count'] 
                    timedif = datetime.now() - datetime.fromtimestamp(item['creation_date'])
                    difHours, remainder = divmod(timedif.total_seconds(), 3600)
                    difMinutes, difSeconds = divmod(remainder, 60)

                    item['creation_date'] = "Created {0} hours, {1} minutes, {2} seconds ago".format(int(difHours), int(difMinutes), int(difSeconds))

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
        self.reddit.auth.authorize(code)
        return list(self.reddit.user.subreddits(limit=None))
    
    def getSubredditNew(self, sr):
        submissionTitles = list()
        for submission in self.reddit.subreddit(sr).new():
            submissionTitles.append(submission.title)
        return list(submissionTitles)