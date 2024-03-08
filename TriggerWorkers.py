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

    owner = "oleksandr-yakov"
    workflow_dispatch = "delivery-android.yml"

    response = requests.post(url.format(owner=owner, repo=repo, workflow_dispatch=workflow_dispatch),
                             json=payload, headers=headers)

    if response.status_code == 204:
        print(f"Action triggered for {repo}")
    else:
        print(f"Action triggered failed for {repo}")
        print("Code Status:", response.status_code)
        print("Text error:", response.text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <PAT> <new_core_tag> ")
        sys.exit(1)

    token = sys.argv[1]
    new_core_tag = sys.argv[2]
    if new_core_tag == "main":
        new_core_tag = "latest"

    trigger_action(token, new_core_tag, "worker-on-premise")
