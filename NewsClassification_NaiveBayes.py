# using supervised learning_Naive Bayes

# load data
from NewsClassification import lemma_data
(trainX, trainY), (testX, testY) = lemma_data()

# Vectorization_count the total number of each word
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

model = make_pipeline(TfidfVectorizer(sublinear_tf=True, norm='l2', ngram_range=(1, 2), stop_words='english'), MultinomialNB())
model.fit(trainX, trainY)
predict_categories = model.predict(testX)
acc = accuracy_score(testY, predict_categories)
print("Final accuracy:", acc)

# plot confusion matrix
import matplotlib.pyplot as plt
import seaborn as sns
mat = confusion_matrix(testY, predict_categories)
fig, ax = plt.subplots(figsize=(10, 10))
from news import top_name
sns.heatmap(mat, square=True, annot=True, fmt='d', xticklabels=top_name(), yticklabels=top_name())
plt.title("Naive Bayes")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig('NaiveBayes.png')

