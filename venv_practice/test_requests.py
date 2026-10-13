import requests

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
print("Content type:", response.headers.get("content-type"))
