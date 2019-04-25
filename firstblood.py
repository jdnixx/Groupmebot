"""
FIRSTBLOOD - first GroupMe API bot

Mostly for testing API connectivity & commands
"""

from GroupmeClient.client import Client as RestClient


"""
Client setup
---
Keyfile must have one line - consisting of the Groupme Access Token
"""
PATH_TO_KEYFILE = "../groupme_keys.txt"     # assumes keyfile is in parent dir

with open(PATH_TO_KEYFILE, "r") as f:
    token = f.readline().strip()
    print(token)
c = RestClient(token)


groupz = c.makeCall("groups", "GetAllGroups")
print(groupz)