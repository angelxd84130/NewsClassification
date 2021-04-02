import numpy as np
import pandas as pd
Alltop = ["science", "general", "health", "business", "entertainment", "sports"]

def top_name():
    return Alltop

def countData(df):
    # check how many data we have
    TopNum = {}
    for i in Alltop:
        TopNum[i] = 0
    for j in range(len(df)):
        TopNum[Alltop[df.iloc[j]['label']]] += 1
    print("Articles:", TopNum)

def news_data():
    print("Get news articles from newsapi.NewsApiClient in 6 categories")

    # get all data from json file
    df = pd.read_json("data.json")
    countData(df)

    # make training data and testing data
    from sklearn.model_selection import train_test_split
    trainX, testX, trainY, testY = train_test_split(df[:]['content'], df[:]['label'],
                                                    test_size=0.25, random_state=1000)
    return (trainX, trainY), (testX, testY)
news_data()
