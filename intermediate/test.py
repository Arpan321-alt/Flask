import requests
url = "http://127.0.0.1:500"
response = requests.get(url=url)
print(response.text)