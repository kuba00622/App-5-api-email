import streamlit as st
import requests

api_key = 'NIPztqAcdJBuw2gvSirGHrWxELaHwdtOoVI27c0k'
url = 'https://api.nasa.gov/planetary/apod?' \
      f'api_key={api_key}'

response1 = requests.get(url)
data = response1.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

image_path = 'NASA.jpg'
response2 = requests.get(image_url)

with open('NASA.jpg', 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_path)
st.text(explanation)