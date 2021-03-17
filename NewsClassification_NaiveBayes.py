# using supervised learning_Naive Bayes

# load data
from NewsClassification import lemma_data
(trainX, trainY), (testX, testY) = lemma_data()

# Vectorization_count the total number of each word
#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer()
#X = vectorizer.fit_transform(trainX, trainY)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score
#print(X.toarray())
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(trainX, trainY)
predict_categories = model.predict(testX)
acc = accuracy_score(testY, predict_categories)
print("Final accuracy:", acc)
# plot
from matplotlib.pyplot import plot
#mat = confusion_matrix(testY, predict_categories)



