import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)

data = html.fromstring(response.content)

# Extract title
title = data.find(".//title").text
print(title)

# Links
links = data.xpath("//a/@href")
print(links)

# Links + URLs
links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))

# Extract the data using class name
titlelines = data.xpath("//span[@class = 'titleline']")
print(titlelines)

for title in titlelines:
    print(title.text)
