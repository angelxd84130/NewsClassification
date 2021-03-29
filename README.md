
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">News Article Classification</h2>

  <p align="center">
    Automatic classification system
    <br />
    <a href="https://github.com/angelxd84130/NewsClassification">View Demo</a>
    ·
    <a href="https://github.com/angelxd84130/NewsClassification/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/NewsClassification/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Want to make a system that can continuously obtain real-world data and apply machine learning to classify after processing. It is hoped that by continuously and automatically obtaining and training new data, the accuracy of classification can be improved.   
In this project, articles are collected from newsAPI and are in 6 categories: science, general, health, business, entertainment, sports.

Here's why:
* Real-world data is very complicated and needs to be handled carefully
* Only by accumulating the amount of data can the accuracy of the training model be improved
* The training results can be used in the automatic filing and search system of articles

At present, several supervised learning models are used on the data, and the results are generated to compare the accuracy.  
For supervised learning models: Naive Bayes, Linear Regression, SVM, and RandomForest,  
it uses nltk library to process and lemmatize words and applies scikit-learn to filter stop words before traning models.  
Also, in Naive Bayes model, it considers both unigrams and bigrams at the same time.  

The system for automatically storing articles is being processed to increase the amount of data for training and testing.  
(The API has a download limit of < 100 articles per category)

### Built With

* [NewsAPI](https://newsapi.org/docs/client-libraries/python)
* [scikit-learn](https://scikit-learn.org/stable/#)
* [matplotlib](https://matplotlib.org/)
* [nltk](https://www.nltk.org/)
* [keras](https://keras.io/)



<!-- GETTING STARTED -->
## Getting Started

Start with a python file with any machine learning model ex.NaiveBayes.py  
Download code and repalce the api_key to your own.

### Prerequisites


1. Get a free API Key at [NewsAPI](https://newsapi.org/docs/client-libraries/python)
2. Replace api_key to your own.
   ```sh
   newsapi = NewsApiClient(api_key=' your api key here ')
   ```
3. Run the python file
   
4. Check the plot to see predict results



<!-- USAGE EXAMPLES -->
## Usage

Use the plot to check result.  
### confused matrix 
![NaiveBayes][product-screenshot] 
### accuracy
- Naive Bayes: 0.55
- CNN: 0.33
- RNN: 0.28
- LSTM: 0.31 

or copy an article content and apply it on the model to make predition.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Multi-Class Text Classification with Scikit-Learn](https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f)
* [Text Classification Using Naive Bayes: Theory & A Working Example](https://towardsdatascience.com/text-classification-using-naive-bayes-theory-a-working-example-2ef4b7eb7d5a)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/NewsClassification.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/NewsClassification/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/NewsClassification.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/NewsClassification/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/NewsClassification.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/NewsClassification/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/NewsClassification.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/NewsClassification/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/NewsClassification.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/NewsClassification/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot]: NaiveBayes.png
