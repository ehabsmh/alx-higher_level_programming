#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    try:
        commits = requests.get(url).json()
        for i in range(10):
            commit_sha = commits[i].get("sha")
            commit_author = commits[i].get("commit").get("author").get("name")
            print(f"{commit_sha}: {commit_author}")
    except IndexError:
        pass
