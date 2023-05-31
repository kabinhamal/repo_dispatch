import requests
import json

url = "https://api.github.com/repos/BAC/test-repo/dispatches"
access_token = "<GitHub Personal Access Token>"

payload = {
    "event_type": "my_event_type",
    "client_payload": {
        "appID": "app",
        "region": "eus"
    }
}

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {access_token}"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 204:
    print("Repository dispatch event triggered successfully")
else:
    print(f"Failed to trigger repository dispatch event. Status code: {response.status_code}")
