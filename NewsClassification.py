# clean data & lemma words

# address Texts
# design how to remove punctuation from every sentence
import string
remove = str.maketrans('', '', string.punctuation)
def addressSentence(sentence):
    sentence = sentence.lower()
    return sentence.translate(remove)

# lemmatize words

# download all needed packages
import nltk
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


def lemma_words(x):
    wnl = WordNetLemmatizer()
    Train_data = []
    for sentence in x:
        Train_Sentence = ['']
        sentence = addressSentence(sentence)
        # separate words
        tokens = word_tokenize(sentence)
        tagged_sent = pos_tag(tokens)
        # print(tagged_sent)
        for tag in tagged_sent:
            wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
            Train_Sentence[0] += wnl.lemmatize(tag[0], pos=wordnet_pos) + ' '
        Train_data.append(Train_Sentence)
    return Train_data

def lemma_data():
    # get data
    from news import news_data
    (trainX, trainY), (testX, testY) = news_data()
    trainX = lemma_words(trainX)
    testX = lemma_words(testX)
    print("Get lemma data successfully! training size:", len(trainX), "testing size:", len(testX))
    return (trainX, trainY), (testX, testY)
