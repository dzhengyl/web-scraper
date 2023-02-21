import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://www.apple.com"
page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

# Extract the product title
title = soup.title.string
print(title)


