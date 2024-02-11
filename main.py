import requests
from send_email import send_email

api_key = "1263ae8bbec842d5a63117877fe1f176"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-11" \
      "&sortBy=publishedAt&apiKey=1263ae8bbec842d5a63117877fe1f176"

# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and descriptions
for article in content["articles"]:
    body = body + article['title'] + "\n" + article['description'] + 2*'\n'

body = body.encode('utf-8')

# send email
send_email(message=body)