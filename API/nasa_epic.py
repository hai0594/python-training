import requests
import json

API_KEY = "nKBTEYBgSvhDb01yqE0UFmOYwFGkh96dSP0UZCOy"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"


response = requests.get(URL)

data = response.json()
image_url = data["url"]

img_data = requests.get(image_url).content

with open("nasapicture.jpg", "wb") as file:
    file.write(img_data)
