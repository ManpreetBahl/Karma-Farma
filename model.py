from IModel import IModel
import requests
import json
import sys
from defines import APIKEY
import html.parser
from datetime import datetime,timezone,time,timedelta

class AppModel(IModel):
    baseURL = "https://api.stackexchange.com/2.2/"

    def __init__(self, app):
        """
	    Initialization of the Model class
	    @params
	        Web app initialized by Flask
	    return
	        N/A
        """
        self.arg = app
    
    def makeAPICall(self, url, params):
        page = 1
        results = []
        hasMore = True

        while hasMore:
            params['page'] = page
            res = requests.get(url, params=params)
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
        results = []
        hasMore = True
        params = {
            "key": APIKEY,
            "order": "desc",
            "sort": "creation",
            "site": site,
            "min": int((datetime.now() - timedelta(hours=12)).timestamp())
        }

        while hasMore:
            params['page'] = page
            res = requests.get(self.baseURL + "questions/no-answers", params=params)
            if res.status_code == 200:
                resJSON = res.json()
                for item in resJSON['items']:
                    item['title'] = html.parser.unescape(item['title'])
                    item['creation_date'] = datetime.fromtimestamp(item['creation_date'], timezone.utc).astimezone().strftime("%m-%d-%Y %H:%M:%S")
                    results.append(item)
                hasMore = resJSON['has_more']
                #hasMore = False
                page += 1
            else:
                print("An error has occured when making API call")
                sys.exit(1)

        return results

if __name__ == "__main__":
    model = AppModel(None)
    print(model.getSites())
    print(model.getNoAnswerQuestions("stackoverflow", 1531180800, 1531267200))