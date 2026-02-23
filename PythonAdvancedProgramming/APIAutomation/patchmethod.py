import requests

try:
    data={
            "name":"Apple Macbook Pro 16 (Updated Name)"
        }


    #make a get request to a api endpoint

    response=requests.post("https://fakestoreapi.com/products/21",json=data)
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

