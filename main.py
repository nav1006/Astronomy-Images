import requests
import streamlit as st

#prepare api key and api url
api = 'dDHwLv5YUpMGDBSAqyofhc9MNhe6fbI32LLkv8jK'
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

#Get the request data as dictionary
response1 = requests.get(url)
data = response1.json()

#extract the image title, url and explaination
title = data['title']
image_url = data['url']
explaination = data['explanation']

#Download the image
image_filepath = 'img.png'
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explaination)

