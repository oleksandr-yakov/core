import requests
import sys


def trigger_action(token, new_core_tag, repo):
    url = "https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_dispatch}/dispatches"

    payload = {
        "ref": "main",
        "inputs": {
            "new_core_tag": new_core_tag
        }
    }

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    owner = "oversecured"
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
    new_core_tag = sys.argv[2]
    repo = sys.argv[3]
    if new_core_tag == "main": new_core_tag = "latest"

    trigger_action(token, new_core_tag, repo)
