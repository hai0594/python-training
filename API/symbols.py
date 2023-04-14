import requests
import json

url = "https://api.apilayer.com/exchangerates_data/symbols"

payload = {}
headers= {
  "apikey": "2SNBzHbawZ70KQ1fdLuYFbwKA1OfYdkL"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json()
result_sym = result["symbols"]
print(json.dumps(result_sym, indent=4))