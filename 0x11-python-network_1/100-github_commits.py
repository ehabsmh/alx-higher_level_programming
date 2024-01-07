#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the\
 GitHub API to display your id."""

import requests
from sys import argv
if __name__ == "__main__":
    payload = ""

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    response = requests.get(url).json()
    ten_commits = response[:10]
    
    dates = []

    for i in range(10):
      commit_date = response[i].get('commit').get('author').get('date')
      dates.append(commit_date)

    dates.sort()

    for date in dates:
      for i in range(len(ten_commits)):
        commit_date = response[i].get('commit').get('author').get('date')
        commit_author = response[i].get('commit').get('author').get('name')
        commit_sha = response[i].get('sha')
        if date == commit_date:
          print(f"{commit_sha}: {commit_author}")
          del ten_commits[i]
        