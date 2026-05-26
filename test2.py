


import requests

API_KEY="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjBjNDkyNjY1ZjFkZDQ3MzU5OTNiZGRiNGEwMTk2ZDZjIiwiaCI6Im11cm11cjY0In0="
API_ROUTE="https://api.openrouteservice.org/geocode/search"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "text": "Belgrade, Serbia"
}

response = requests.get(API_ROUTE, params=params, headers=headers)
data = response.json()

print(data['features'][0]['geometry']['coordinates'])