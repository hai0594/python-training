import requests
import json 

F = "EUR"
T = "VND"
Amount = int(input("Enter amount to convert: "))

url_cv = f"https://api.apilayer.com/exchangerates_data/convert?to={T}&from={F}&amount={Amount}"
payload = {}
headers= {
  "apikey": "2SNBzHbawZ70KQ1fdLuYFbwKA1OfYdkL"
}

response = requests.request("GET", url_cv, headers=headers, data = payload)

status_code = response.status_code
result = response.json()

print(json.dumps(result, indent= 4))