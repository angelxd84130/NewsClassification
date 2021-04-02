from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='9cd9ca0dc6ec44388be32fb87220cb75')

data = newsapi.get_top_headlines(category='health', language='en', country="us", page_size=1).get('articles')
for i in data[0]:
    print(i, ':', data[0][i])