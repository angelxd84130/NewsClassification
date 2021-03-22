# using supervised learning_Naive Bayes, Logistic Regression, RandomForest, and SVM

# load data
from NewsClassification import lemma_data
(trainX, trainY), (testX, testY) = lemma_data()

# Vectorization_count the total number of each word
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
#print(X.toarray())

#model = make_pipeline(TfidfVectorizer(sublinear_tf=True, norm='l2', ngram_range=(1, 2), stop_words='english'), MultinomialNB())
tfidf_vect = TfidfVectorizer(sublinear_tf=True, norm='l2', ngram_range=(1, 2), stop_words='english')
models = [
    make_pipeline(tfidf_vect, MultinomialNB()),
    make_pipeline(tfidf_vect, RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0)),
    make_pipeline(tfidf_vect, LinearSVC()),
    make_pipeline(tfidf_vect, LogisticRegression(random_state=0))]

for model in models:
    model.fit(trainX, trainY)
predict_categories = model.predict(testX)
acc = accuracy_score(testY, predict_categories)
print("Final accuracy:", acc)


# plot
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 10))
from news import top_name
plt.title("Naive Bayes")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig('SupervisedLearning.png')
#plt.show()



