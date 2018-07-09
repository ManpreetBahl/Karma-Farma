import requests
import json
import sys
from defines import APIKEY

baseURL = "https://api.stackexchange.com/2.2/"


#================Get the list of sites==================
def getSites():
    page = 1

    params = {"key": APIKEY, "page": page, "filter": "!6P.ZZU_Ynt.HP"}
    res = requests.get(baseURL + "sites", params=params)
    resJSON = res.json()
    sites = resJSON['items']
    hasMore = resJSON['has_more']

    while hasMore:
        params = {"key": APIKEY, "page": page, "filter": "!6P.ZZU_Ynt.HP"}
        res = requests.get(baseURL + "sites", params=params)
        if res.status_code == 200:
            resJSON = res.json()
            sites.append(resJSON['items'])
            hasMore = resJSON['has_more']
            page += 1
        else:
            print("An error has occured when making API call")
            sys.exit(1)
    
    return sites

print(getSites())



