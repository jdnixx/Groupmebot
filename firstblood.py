"""
FIRSTBLOOD - first GroupMe API bot

Mostly for testing API connectivity & commands
"""

# from GroupmeClient.client import Client as RestClient

"""
Client setup
---
Keyfile must have one line - consisting of the Groupme Access Token
"""
GROUP_ID = 12375272
PATH_TO_KEYFILE = "../groupme_keys.txt"     # assumes keyfile is in parent dir

with open(PATH_TO_KEYFILE, "r") as f:
    token = f.readline().strip()
    print(token)
# c = RestClient(token)


# groupz = c.makeCall("groups", "GetAllGroups")
# print(groupz)


def new_message(data):
    """
    Main method invoked when a new message arrives from the group.
    The (flask) app receives a POST with the new message, and it is immediately sent here
    :param data: dict of JSON data from GroupMe API's POST request
    :return:
    """
    if data['text'] == "ride on cowboy":
        respond_rideoncowboy(data)


def respond_rideoncowboy(data)
    resp = "Hell Yeah, brother"
    resp2 = "*takes swig of Busch Lite*"

