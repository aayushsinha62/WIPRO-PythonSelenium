import requests

try:
    #make a get request to a api endpoint

    response=requests.get("https://videogamedb.uk:443/api/v2/videogame")
    print(response)

    #check if the status code is 200ok
    if response.status_code==200:
        print("status code is 200ok")
        #parse the json file
        data=response.json()
        print(data)

    else: print(f"error: received status code {response.status_code}")

except requests.exception.RequestException as e:
    print(f"An error occured:{e}")

try:
    #make a get request to a api endpoint

    response=requests.get("https://fakestoreapi.com/products")
    print(response)

    #check if the status code is 200ok
    if response.status_code==200:
        print("status code is 200ok")
        #parse the json file
        data=response.json()
        print(data)

    else: print(f"error: received status code {response.status_code}")

except requests.exception.RequestException as e:
    print(f"An error occured:{e}")