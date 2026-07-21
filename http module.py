import requests

response=requests.get("https://prakashchaudhary.netlify.app/")
print(response.text)



response = requests.post(
    "https://httpbin.org/post", 
    json={"name": "Alice", "role": "Developer"}
)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)


if response.text.strip():
    print("Parsed JSON:", response.json())
else:
    print("Server returned an empty response.")