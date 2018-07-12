from IModel import IModel
import requests
import json
import sys
from defines import APIKEY

class AppModel(IModel):
    baseURL = "https://api.stackexchange.com/2.2/"
    
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
                    results.append(item)
                hasMore = resJSON['has_more']
                page += 1
            else:
                print("An error has occured when making API call")
                sys.exit(1)
        
        return results

    def getSites(self):
        return self.makeAPICall(url=self.baseURL + "sites", params={"key": APIKEY, "filter": "!6P.ZZU_Ynt.HP"})
    
    def getNoAnswerQuestions(self, site, min, max):
        params = {
            "key": APIKEY,
            "order": "desc",
            "sort": "creation",
            "site": site,
            "min": min,
            "max": max
        }
        return self.makeAPICall(url=self.baseURL + "/questions/no-answers", params=params)

if __name__ == "__main__":
    model = AppModel()
    print(model.getSites())
    print(model.getNoAnswerQuestions("stackoverflow", 1531180800, 1531267200))