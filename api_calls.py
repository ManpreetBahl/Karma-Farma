import requests
import json
from defines import APIKEY

baseURL = "https://api.stackexchange.com/2.2/"

#Get the list of sites
params = {"key": APIKEY, "page": 1, "filter": "!6P.ZZU_Ynt.HP"}

res = requests.get(baseURL + "sites", params=params)
print(res.json())

