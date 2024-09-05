import requests

url = "https://api.upbit.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}
res = requests.get(url, headers=headers)
data = res.json()

print(data)
print("------------------------------")
print(f"Response : {res}")
