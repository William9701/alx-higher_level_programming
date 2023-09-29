#!/usr/bin/python3
"""a Python script that lists 10 commits (from the most recent to oldest) of
a repository by a user"""

if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    response = requests.get(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/commits')

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    else:
        print(None)
