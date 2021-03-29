from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
TopNum = {}

from datetime import datetime
import time
import sched
import json

def top_name():
    return Alltop

def clean(data, idx, Texts, TopNum):
    TopNum[Alltop[idx]] = 0
    timeNow = datetime.now().strftime("%Y-%m-%d")

    for j in range(len(data)):
        # clean data
        if data[j]['content'] is not None and data[j]['publishedAt'][:10]==timeNow:
            # set up labels (categories)
            data[j]['label'] = idx
            Texts.append(data[j])
            TopNum[Alltop[idx]] += 1

def load():
    task()
    print("Get news articles from newsapi.NewsApiClient in 6 categories")
    Texts = []
    page_size = 50
    with open('abc.json', 'r', encoding='utf-8') as f:
        output = json.load(f)
    for i in range(len(Alltop)):
        # get all data from newsAPI
        data = newsapi.get_top_headlines(category=Alltop[i], language='en', country="us", page_size=page_size).get('articles')
        clean(data, i, Texts, TopNum)

    # check how many data we have
    print("Articles:", TopNum)

    # store data in the file

    print("Finish loading -> machine learning is available now.")

def task():
    print("Loading..", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# auto loading 7 days
sec = 24*60*60
days = [0]+[sec]*6
for i in days:
    # initialize time
    scheduler = sched.scheduler(time.time, time.sleep)
    # schedule the time to call load function
    scheduler.enter(i, 1, load)
    scheduler.run()


