# NewsClassification
**Gain news articles from News API https://newsapi.org/docs/client-libraries/python**  
**Classify articles in 6 categories: science, general, health, business, entertainment, sports.**  
**Use nltk library to organize and lemmatize words**  
*Implement in Python*  
### Predicted Results(accuracy)  
- Naive Bayes: 0.55
- CNN: 0.33
- RNN: 0.28
- LSTM: 0.31  
### Problems & Solutions  
- Underfit: Download and save articles regularly to increase training volume(The API has a download limit of < 100 articles per category).
- Noice: Filte stop words to highlight keywords.
- Optimization: set up ngram function to consider both unigrams and bigrams at the same time.
