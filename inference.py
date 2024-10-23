import requests
import json

# Define the URL and headers
url = "http://127.0.0.1:2626/invocations"
headers = {"Content-Type": "application/json"}

# Create the JSON payload
data = {
    "inputs": [[14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0]]
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failed to get a valid response. Status code:", response.status_code)
    print("Response content:", response.text)

# if you want to test it in terminal, using curl
# curl -X POST -H "Content-Type: application/json" --data '{
#     "inputs": [[14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0]]
# }' http://127.0.0.1:1234/invocations