import requests
import json
import sys
from defines import APIKEY

baseURL = "https://api.stackexchange.com/2.2/"


#================Get the list of sites==================
def getSites():
    page = 1
    sites = []
    hasMore = True

    while hasMore:
        params = {"key": APIKEY, "page": page, "filter": "!6P.ZZU_Ynt.HP"}
        res = requests.get(baseURL + "sites", params=params)
        if res.status_code == 200:
            resJSON = res.json()
            for item in resJSON['items']:
                sites.append(item)
            hasMore = resJSON['has_more']
            page += 1
        else:
            print("An error has occured when making API call")
            sys.exit(1)
    
    return sites
#=======================================================

def getNoAnswerQuestions(site, min, max):
    page = 1
    questions = []
    hasMore = True

    while hasMore:
        params = {
            "key": APIKEY, 
            "page": page, 
            "order": "desc",
            "sort": "creation",
            "site": site,
            "min": min,
            "max": max
        }

        res = requests.get(baseURL + "/questions/no-answers", params=params)
        if res.status_code == 200:
            resJSON = res.json()
            for item in resJSON['items']:
                questions.append(item)
            hasMore = resJSON['has_more']
            page += 1
        else:
            print("An error has occured when making API call")
            sys.exit(1)
    
    return questions


#print(getSites())
print(getNoAnswerQuestions("stackoverflow", 1531180800, 1531267200))


