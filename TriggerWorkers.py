import requests
import sys

def trigger_action(token, repo, ref):
    url = "https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_dispatch}/dispatches"

    payload = {
        "ref": ref,
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
        print("Usage: python3 script.py <PAT> <ref>")
        sys.exit(1)

    token = sys.argv[1]
    ref = sys.argv[2]

    trigger_action(token, "worker", ref)
