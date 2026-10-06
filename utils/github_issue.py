import os

import requests
from dotenv import load_dotenv

load_dotenv()

TIMEOUT = 30


def create_issue(title, body):
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    if not token or not repo:
        return None

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    url = f"https://api.github.com/repos/{repo}/issues"

    existing = requests.get(
        url,
        headers=headers,
        params={"state": "open", "per_page": 100},
        timeout=TIMEOUT,
    )
    if existing.ok and any(issue["title"] == title for issue in existing.json()):
        return None

    response = requests.post(
        url,
        headers=headers,
        json={"title": title, "body": body, "labels": ["bug"]},
        timeout=TIMEOUT,
    )
    return response.json().get("html_url") if response.ok else None