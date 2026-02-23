import requests

try:
    data={
            "category": "Platform",
            "name": "Mario",
            "rating": "Mature",
            "releaseDate": "2012-05-04",
            "reviewScore": 85
        }


    #make a get request to a api endpoint

    response=requests.get("https://videogamedb.uk:443/api/v2/videogame",json=data)
    print(response)

    #check if the status code is 200ok
    if response.status_code==200:
        print("Status code is 200 k")

        # parse the json file
        data = response.json()

        # text of the response file
        print(response.text)

        # content of the response
        print(response.content)

        # status code of the response
        print(response.status_code)

        # headers
        print(response.headers)

        # history
        print(response.history)

        # url
        print(response.url)

        # fetch the single header
        content_type = response.headers.get('Content-Type')
        print(content_type)


    else: print(f"error: received status code {response.status_code}")

except requests.exception.RequestException as e:
    print(f"An error occured:{e}")