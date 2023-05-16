import requests
import json
import os
import ast

def main():
    github_url = "https://api.github.com"
    org =  str(os.environ["org"])
    callee_repo_name =  str(os.environ["callee_repo_name"])
    func_token =  str(os.environ["func_token"])
    payload =  str(os.environ["appID"])
    workflow_id = str(os.environ["workflow_id"])
    

    
    repo_dispatch(payload, workflow_id, github_url, org, callee_repo_name, func_token)
    
    
    
    

def repo_dispatch(payload, workflow_id, github_url, org, callee_repo_name, func_token):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {func_token}",
    }

    data = {
        "event_type": f"{workflow_id}",
        "client_payload": {
            "payload": payload
          
        }
    }

    response = requests.post(
        f"{github_url}/repos/{org}/{callee_repo_name}/dispatches",
        json=data,
        headers=headers
    )
    print(response.status_code)
    if response.status_code == 204:
        print(f"Successfully triggering repo_dispatch on the repo: {callee_repo_name} with event_type: {workflow_id} ")
    else:
         print(f"Repo_dispatch on the repo: {callee_repo_name} failed")

if __name__ == "__main__":
    main()
