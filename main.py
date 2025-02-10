import requests
from send_email import send_email

topic = "tesla"
lang = "en"

api_key = "2436fb163b4e4ff4a0883d737c2e68d8"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2025-01-10" \
      "&sortBy=publishedAt" \
      "&apiKey=2436fb163b4e4ff4a0883d737c2e68d8" \
      f"&language={lang}"

request = requests.get(url)
content = request.json()
body = ""

for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's News"\
            + "\n" + body + article['title'] + "\n"\
            + article['description']\
            + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
