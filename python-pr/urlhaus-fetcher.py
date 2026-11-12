import requests

url = "https://urlhaus-api.abuse.ch/v1/url/"

headers = {
    "Auth-Key": "Auth-token",
    "User-Agent": "CTI-Script/1.0"
}

data = {
    "url": "https://gold-marylee-16.tiiny.site/index.json"
}
response = requests.post(url, headers=headers , data=data)
print(response.status_code)
print(response.json())