import requests

print("=== GitHub API ===")
response = requests.get("https://api.github.com")
print("Status:", response.status_code)
print("Type:", response.headers.get("content-type"))
data = response.json()
for key, value in list(data.items())[:3]:
    print(key, ":", value)

print("\n=== Cat Fact API ===")
response = requests.get("https://catfact.ninja/fact")
print("Status:", response.status_code)
print("Type:", response.headers.get("content-type"))
print("Body:", response.json())

print("\n=== Joke API ===")
response = requests.get("https://official-joke-api.appspot.com/random_joke")
print("Status:", response.status_code)
print("Type:", response.headers.get("content-type"))
data = response.json()
print("Setup:", data["setup"])
print("Punchline:", data["punchline"])

print("\n=== POST test ===")
response = requests.post("https://catfact.ninja/fact")
print("POST status:", response.status_code)
print("POST body:", response.text)

print("\n=== DELETE test ===")
response = requests.delete("https://catfact.ninja/fact")
print("DELETE status:", response.status_code)
print("DELETE body:", response.text)

print("\n=== 404 test ===")
response = requests.get("https://api.github.com/nonexistent-endpoint")
print("Status:", response.status_code)
print("Body:", response.json())
