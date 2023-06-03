import requests
import json

def create_webhook(repository, webhook_url, secret=None, events=['push']):
    api_url = f"https://api.github.com/repos/{repository}/hooks"
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'name': 'web',
        'active': True,
        'events': events,
        'config': {
            'url': webhook_url,
            'content_type': 'json',
            'secret': secret
        }
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Webhook created successfully.")
    else:
        print("Failed to create webhook. Status code:", response.status_code)
        print("Error message:", response.text)

# Example usage
repository = "your/repository"
webhook_url = "https://your-webhook-url.com"
secret = "your-webhook-secret"
events = ['push', 'pull_request']

create_webhook(repository, webhook_url, secret, events)
