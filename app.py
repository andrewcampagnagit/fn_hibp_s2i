import requests
import os

url = "https://haveibeenpwned.com/api/v3/breachedaccount/andrewalex@optonline.net"
payload={}
api_key = os.environ["APP_INPUTS"]

headers = {
  "hibp-api-key": api_key,
  "format": "application/json",
  "timeout": "2.5",
  "HIBP": api_key,
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print("Done!")
