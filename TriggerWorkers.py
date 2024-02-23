import requests
import sys


def trigger_action(token, new_variable):
    url = "https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_dispatch}/dispatches"

    payload = {
        "ref": "main",
        "inputs": {
            "new_variable": new_variable
        }
    }

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    owner = "oleksandr-yakov"
    repo = "worker"
    workflow_dispatch = "delivery-android.yml"

    response = requests.post(url.format(owner=owner, repo=repo, workflow_dispatch=workflow_dispatch),
                             json=payload, headers=headers)

    if response.status_code == 204:
        print("Action triggered")
    else:
        print("Action triggered failed")
        print("Code Status:", response.status_code)
        print("Text error:", response.text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    token = sys.argv[1]
    new_variable = sys.argv[2]

    trigger_action(token, new_variable)
