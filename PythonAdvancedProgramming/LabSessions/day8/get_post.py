# 1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.

import requests
url="https://jsonplaceholder.typicode.com/users"
response=requests.get(url)

users=response.json()

for user in users:
    print(user["name"],"_",user["email"])


# 2. Send a GET request with query parameter userId=2 and print number of posts returned.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}

response = requests.get(url, params=params)
posts = response.json()

print("Number of posts:", len(posts))


# 3. Write a POST request to create a new resource and verify status code 201.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "API Testing",
    "body": "Learning requests module",
    "userId": 1
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("Resource created successfully")
else:
    print("Failed, status code:", response.status_code)

# 4. Explain the difference between data= and json= in requests.post().


# 5. Write code to check if response status code is not 200 and raise an exception.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code != 200:
    raise Exception(f"Request failed with status code {response.status_code}")


# Section 2: Intermediate Level
# 6. Fetch all users and print usernames in uppercase.

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(user["username"].upper())


# 7. Implement timeout handling (2 seconds) and catch Timeout exception.

import requests
from requests.exceptions import Timeout

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=2
    )
    print("Request successful")
except Timeout:
    print("Request timed out")

# 8. Use Session object to send multiple requests and demonstrate cookie persistence.

import requests

session = requests.Session()

# First request
response1 = session.get("https://httpbin.org/cookies/set/sessionid/12345")

# Second request (cookie persists)
response2 = session.get("https://httpbin.org/cookies")

print(response2.json())

# 9. Upload a file using requests and print server response.

import requests

url = "https://httpbin.org/post"

with open("sample.txt", "w") as f:
    f.write("Hello from Python")

with open("sample.txt", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print(response.json())

# 10. Fetch posts and save response JSON into a file named posts.json.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

with open("posts.json", "w") as file:
    json.dump(response.json(), file, indent=4)

print("posts.json saved successfully")
