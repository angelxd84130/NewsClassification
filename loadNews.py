from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
TopNum = {}

from datetime import datetime
import time
import sched

def top_name():
    return Alltop

def getPlan(data, idx, Texts, Labels, TopNum):
    TopNum[Alltop[idx]] = 0
    timeNow = datetime.now().strftime("%Y-%m-%d")
    for j in range(len(data)):
        if data[j]['content'] is not None and data[j]['publishedAt']==timeNow:
            # clean data (get content only)
            Texts.append(data[j]['content'])
            # set up labels (categories)
            Labels.append(idx)
            TopNum[Alltop[idx]] += 1

def load():
    task()
    print("Get news articles from newsapi.NewsApiClient in 6 categories")
    Texts = []
    Labels = []
    page_size = 50
    for i in range(len(Alltop)):
        # get all data from newsAPI
        data = newsapi.get_top_headlines(category=Alltop[i], language='en', country="us", page_size=page_size).get('articles')
        getPlan(data, i, Texts, Labels, TopNum)

    # check how many data we have
    print("Articles:", TopNum)

    # store data in the file

def task():
    print("Loading..", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# auto loading 7 days
for i in range(7):
    # initialize time
    scheduler = sched.scheduler(time.time, time.sleep)
    # schedule the time to call load function
    scheduler.enter(24*60*60, 1, load)
    scheduler.run()


