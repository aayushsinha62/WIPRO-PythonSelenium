#
# Install and import BeautifulSoup from the bs4 module.
# Write a simple program to parse a small HTML string.
# Given this HTML:
# Extract the title text.
# Extract the <h1 > text.
# Extract
# the
# paragraph
# text.
# Write
# a
# program
# to:
# Find
# the
# first < a > tag.
# Print
# its
# href
# attribute.
# Use.prettify()
# to
# format
# parsed
# HTML.
# What is the
# difference
# between:
# find()
# find_all()
# < html >
# < head > < title > Test
# Page < / title > < / head >
# < body >
# < h1 > Welcome < / h1 >
# < p > This is a
# paragraph. < / p >
# < / body > < / html >
#
# 2.
# Scrape
# product
# details
# from an e
#
# -commerce
# sample
# page:
# Product
# name
# Price
# Rating
# Availability
# Extract
# all
# image
# URLs
# from a webpage.

from bs4 import BeautifulSoup

html_doc="""
<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click here</a>
  </body>
</html>
"""

soup=BeautifulSoup(html_doc,"html.parser")

#extract title text
print(soup.title.text)


#extract <h1> text
print(soup.h1.text)

#extrat paragraph text
print(soup.p.text)

#find first anchor tag and print href

link=soup.find("a")
print(link["href"])

#use .prettify to format html

print(soup.prettify())


#diff betn find and findall

# Feature -	find() -	find_all()
# Returns	- First matching tag -	List of all matching tags
# Output type -	Tag / None -	List
# Use case -	One element -	Multiple elements

#scrape product details

html_doc1="""<div class="product">
  <h2 class="name">Laptop</h2>
  <span class="price">$999</span>
  <span class="rating">4.5</span>
  <p class="availability">In Stock</p>
  <img src="laptop1.jpg">
  <img src="laptop2.jpg">
</div>"""

soup=BeautifulSoup(html_doc1,"html.parser")

name=soup.find("h2",class_="name").text
price=soup.find("span",class_="price").text
rating=soup.find("span",class_="rating").text
availability=soup.find("p",class_="availability").text

print(name)
print(price)
print(rating)
print(availability)

images=soup.find_all("img")

for img in images:
    print(img["src"])