import smtplib
import requests
from send_email import send_email

topic = "tesla"

api_key = "1263ae8bbec842d5a63117877fe1f176"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-01-11&" \
      "sortBy=publishedAt&" \
      "apiKey=1263ae8bbec842d5a63117877fe1f176&" \
      "language=pl"

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and descriptions
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "Subject: Today's news"\
               + '\n' + body + article['title'] + "\n" \
               + article['description'] \
               + '\n' + article['url'] + 2*'\n'

body = body.encode('utf-8')

# send email
try:
    send_email(message=body)
except smtplib.SMTPDataError:
    exit()