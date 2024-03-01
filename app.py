import requests
import os
import json

app_inputs = json.loads(os.environ["APP_INPUTS"].replace("'",'"')
url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + app_inputs["account"]
payload={}
api_key = app_inputs["api_key"]


headers = {
  "hibp-api-key": api_key,
  "format": "application/json",
  "timeout": "2.5",
  "HIBP": api_key,
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
