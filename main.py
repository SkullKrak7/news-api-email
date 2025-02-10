import requests

api_key = "2436fb163b4e4ff4a0883d737c2e68d8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-10&sortBy=publishedAt&apiKey=2436fb163b4e4ff4a0883d737c2e68d8"

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
    
