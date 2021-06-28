import requests

token = "c689d40f0396f37e6f9f2543c9e82aa9ed56cbd0265a7d5838536fbfd03a9a39"

headers = {
    "Authorization": "Bearer %s" % token,
}

payload = {
  "power": "on",
  "color": "green saturation:0.8",
  "brightness": 0.5,
  "duration": 5,
}

# response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

print(response.json())