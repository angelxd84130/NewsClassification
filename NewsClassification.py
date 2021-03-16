# using deep learning_RNN
from newsapi import NewsApiClient
import numpy as np
import pandas as pd
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')
#Alltop = ["science", "general", "health", "business", "entertainment", "sports"]
Alltop = ["health", "business", "entertainment", "sports"]
TopNum = {}
data = np.array([])
Texts = []
Labels = []
page_size = 100


def getPlan(data, idx, Texts, Labels, TopNum):
    TopNum[Alltop[idx]] = 0
    for j in range(len(data)):
        if data[j]['content'] is not None:
            # clean data (get content only)
            #print([data[j]['content']])
            Texts.append(data[j]['content'])
            # set up labels (categories)
            Labels.append(idx)
            TopNum[Alltop[idx]] += 1
    #print("Here", Texts)
    #return np.array(Texts)


for i in range(len(Alltop)):
    data = np.array([])
    # get all data from newsAPI
    data = newsapi.get_top_headlines(category=Alltop[i], language='en', country="us", page_size=page_size).get('articles')
    getPlan(data, i, Texts, Labels, TopNum)
    #print(data)

# check how many data we have
print("Articles:", TopNum)
#print("Lebel", Labels)
#print("Text:\n", Texts)

# address Texts
# design how to remove punctuation from every sentence
import string
remove = str.maketrans('', '', string.punctuation)
def addressSentence(sentence):
    sentence = sentence.lower()
    return sentence.translate(remove)

# lemmatize words
import nltk
#  download all needed packages
#nltk.download()
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# check out word's type first, and then lemma word by its type
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

wnl = WordNetLemmatizer()
Train_data = []
for sentence in Texts:
    Train_Sentence = ['']
    sentence = addressSentence(sentence)
    # separate words
    tokens = word_tokenize(sentence)
    tagged_sent = pos_tag(tokens)
    #print(tagged_sent)
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        Train_Sentence[0] += wnl.lemmatize(tag[0], pos=wordnet_pos) + ' '
    Train_data.append(Train_Sentence)
#print(Train_data)

# make training data and testing data

from sklearn.model_selection import train_test_split
trainX, testX, trainY, testY = train_test_split(Train_data, Labels, test_size=0.25, random_state=1000)

# one-hot encoding
from keras.utils import np_utils
trainY_oneHot = np_utils.to_categorical(trainY)
testY_oneHot = np_utils.to_categorical(testY)
print(trainX[:1])

# make a dictionary to store words
from keras.preprocessing.text import Tokenizer
dictionary = Tokenizer(num_words=10000)
dictionary.fit_on_texts(trainX)
#print(dictionary.word_index)
x_train = dictionary.texts_to_sequences(trainX)
x_test = dictionary.texts_to_sequences(testX)
from keras.preprocessing import sequence
x_train = sequence.pad_sequences(x_train, maxlen=400)
x_test = sequence.pad_sequences(x_test, maxlen=400)

# set up training model
from keras import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers.recurrent import SimpleRNN
model = Sequential()
# Embedding layer
# input 2000 training examples, and each length is 100
model.add(Embedding(output_dim=32, input_dim=4000, input_length=400))
model.add(Dropout(0.25))
# RNN layer
model.add(SimpleRNN(units=32))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(units=4, activation='softmax'))
print(model.summary())
# there are 6 results, so use categorical_crossentropy
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# start training
# train an example pre time (text length=100), and train all example 10 times
train_history = model.fit(x_train, trainY_oneHot, batch_size=100, epochs=10, verbose=2, validation_split=0.2)

# show train history
import matplotlib.pyplot as plt
def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.xlabel('Epoch')
    plt.ylabel(train)
    plt.legend(['train', 'validation'])
    plt.show()


# using accuracy and loss plots helps to check overfitting problem
print(show_train_history(train_history, 'accuracy', 'val_accuracy'))
print(show_train_history(train_history, 'loss', 'val_loss'))

# evaluation
scores = model.evaluate(x_test, testY_oneHot)
print("Final accuracy", scores[1])
'''
prediction = model.predict_classes(x_test)
# convert predict result from 2D to 1D
import numpy as np
prediction = prediction.reshape(-1)
'''
