import requests
from send_email import send_email

api_key = "2436fb163b4e4ff4a0883d737c2e68d8"
url = """https://newsapi.org/v2/everything?q=tesla&from=2025
-01-10&sortBy=publishedAt&apiKey=2436fb163b4e4ff4a0883d737c2e68d8"""

request = requests.get(url)
content = request.json()
body = ""

for article in content['articles']:
    if article['title'] is not None:
        body = body + (article['title']) + "\n" + (article['description']) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
