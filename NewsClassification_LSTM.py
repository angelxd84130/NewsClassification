# using deep learning_LSTM

# get data
from news import news_data
(trainX, trainY), (testX, testY) = news_data()

# one-hot encoding
from keras.utils import np_utils
trainY_oneHot = np_utils.to_categorical(trainY)
testY_oneHot = np_utils.to_categorical(testY)

# make a dictionary to store words
from keras.preprocessing.text import Tokenizer
dictionary = Tokenizer(num_words=12000)
dictionary.fit_on_texts(trainX)
#print(dictionary.word_index)
x_train = dictionary.texts_to_sequences(trainX)
x_test = dictionary.texts_to_sequences(testX)
# limit the length of each article
from keras.preprocessing import sequence
x_train = sequence.pad_sequences(x_train, maxlen=200)
x_test = sequence.pad_sequences(x_test, maxlen=200)

# set up training model RNN
from keras import Sequential
from keras.layers.core import Dense, Dropout
from keras.layers import Embedding
from keras.layers.recurrent import LSTM
model = Sequential()
# Embedding layer
# input 200+ training examples, and each length is 200
model.add(Embedding(output_dim=32, input_dim=12000, input_length=200))
model.add(Dropout(0.25))
# RNN layer
model.add(LSTM(units=32))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(units=6, activation='softmax'))
print(model.summary())
# there are 6 results, so use categorical_crossentropy
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# start training
# train an example pre time (text length=100), and train all example 10 times
train_history = model.fit(x_train, trainY_oneHot, batch_size=50, epochs=10, verbose=2, validation_split=0.2)

# show training history
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

