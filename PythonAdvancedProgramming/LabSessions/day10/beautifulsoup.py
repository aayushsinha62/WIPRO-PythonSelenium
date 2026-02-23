from bs4 import BeautifulSoup

html = """
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<p>This is a paragraph.</p>
<a href="https://google.com">Google</a>
<a href="https://github.com">GitHub</a>
<b>Bold Text</b>
<h2>First H2</h2>
<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>Aayush</td><td>22</td></tr>
</table>
<img src="image1.png">
<img src="image2.jpg">
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")


# 1) Parse HTML – Extract title and h1

print("Title:", soup.title.text)
print("H1:",soup.h1.text)

# 2) Extract All Paragraphs

paragraphs=soup.find_all("p")
for p in paragraphs:
    print(p.text)

# 3) Extract All Links and Count

links=soup.find_all("a")
print("Total links:", len(links))

for link in links:
    print(link.get("href"))

# 4) Extract Attributes

link=soup.find("a")
print(link.attrs)

# 5) Extract First h2

h2=soup.find("h2")
print(h2.text)

# 6) Extract Bold Text

bold=soup.find_all("b")
for b in bold:
    print(b.text)

# 7) Extract All href Values

hrefs=[a.get("href") for a in soup.find_all("a")]
print(hrefs)

# 8) Get All Text Without Tags

print(soup.find_all("img"))

# 9) Extract Title from Website

print(soup.title.string)

# 10) Extract All Headings

headings=soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
for h in headings:
    print(h.name,":",h.text)

# 11) Extract Table Data

rows=soup.find_all("tr")
for row in rows:
    cols=row.find_all(["td","th"])
    print([col.text for col in cols])

# 12) Extract Images

images=soup.find_all("img")
for img in images:
    print(img.get("src"))



