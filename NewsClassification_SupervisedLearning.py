# using supervised learning_Naive Bayes, SVM, and Logistic Regression

# load data
from NewsClassification import lemma_data
(trainX, trainY), (testX, testY) = lemma_data()

# Vectorization_count the total number of each word
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score


#model = make_pipeline(TfidfVectorizer(sublinear_tf=True, norm='l2', ngram_range=(1, 2), stop_words='english'), MultinomialNB())
tfidf_vect = TfidfVectorizer(sublinear_tf=True, norm='l2', ngram_range=(1, 2), stop_words='english')
Models = ['Naive Bayes', 'SVM', 'Logistic Regression']
models = [
    make_pipeline(tfidf_vect, MultinomialNB()),
    make_pipeline(tfidf_vect, LinearSVC()),
    make_pipeline(tfidf_vect, LogisticRegression(random_state=0))]
results = []

for model in models:
    model.fit(trainX, trainY)
    predict_categories = model.predict(testX)
    acc = accuracy_score(testY, predict_categories)
    results.append(acc)
print(results)


# plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.title("Supervised Learning")
plt.xlabel("Models")
plt.ylabel("Accuracy")
ax.plot(Models, results)
plt.savefig('SupervisedLearning.png')
#plt.show()



