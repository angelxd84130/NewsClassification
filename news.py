from newsapi import NewsApiClient
import numpy as np
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
TopNum = {}
data = np.array([])
Texts = []
Labels = []
page_size = 50

def top_name():
    return Alltop

def getPlan(data, idx, Texts, Labels, TopNum):
    TopNum[Alltop[idx]] = 0
    for j in range(len(data)):
        if data[j]['content'] is not None:
            # clean data (get content only)
            Texts.append(data[j]['content'])
            # set up labels (categories)
            Labels.append(idx)
            TopNum[Alltop[idx]] += 1

def news_data():
    print("Get news articles from newsapi.NewsApiClient in 6 categories")
    for i in range(len(Alltop)):
        # get all data from newsAPI
        data = newsapi.get_top_headlines(category=Alltop[i], language='en', country="us", page_size=page_size).get('articles')
        getPlan(data, i, Texts, Labels, TopNum)

    # check how many data we have
    print("Articles:", TopNum)

    # make training data and testing data
    from sklearn.model_selection import train_test_split
    trainX, testX, trainY, testY = train_test_split(Texts, Labels, test_size=0.25, random_state=1000)
    return (trainX, trainY), (testX, testY)