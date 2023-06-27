import requests
from bs4 import BeautifulSoup
import json
from time import sleep

res = requests.get("https://athena.eslite.com/api/v1/best_sellers/online/month?l1=3&page=1&per_page=100")
jd = json.loads(res.text)

i = 0

for books in jd["products"]:

    print(jd["products"][i]("ean"))
    #print(jd["products"][i]["name"])
    #print(jd["products"][i]["author"])
    #print(jd["products"][i]["manufacturer"])
    #print(jd["products"][i]["manufacturer_date"])
    #print(jd["products"][i]["final_price"])
    #print(jd["products"][i]["discount_range"])
    #print(jd["products"][i]["retail_price"])
    #print("----------第"+str(i+1)+"本-----------")
    
    i += 1
    res = requests.get("https://athena.eslite.com/api/v1/best_sellers/online/month?l1=3&page=1&per_page=100")
    jd = json.loads(res.text)
    sleep(0.1)