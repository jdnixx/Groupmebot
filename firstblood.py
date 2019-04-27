"""
FIRSTBLOOD - first GroupMe API bot

Mostly for testing API connectivity & commands
"""
import os
import GroupmeClient.client


GROUP_ID = 12375272     # nerd chat

"""
Client setup
---
Keyfile can have 2 lines, containing:
line 1 | Groupme Access Token
line 2 | (optional) Bot ID
"""
# PATH_TO_KEYFILE = "../groupme_keys.txt"     # assumes keyfile is in parent dir
#
# with open(PATH_TO_KEYFILE, "r") as f:
#     TOKEN = f.readline().strip()
#     BOTID = f.readline().strip()
#     print(TOKEN, BOTID)
TOKEN = os.environ.get('TOKEN')
BOTID = os.environ.get('BOT_ID')

c = GroupmeClient.client.Client(TOKEN)

# groupz = c.makeCall("groups", "GetAllGroups")
# print(groupz)


def incoming_message(data):
    """
    Main method invoked when a new message arrives from the group.
    The (flask) app receives a POST with the new message, and it is immediately sent here
    :param data: dict of JSON data from GroupMe API's POST request
    :return:
    """
    if data['text'] == "ride on cowboy":
        respond_rideoncowboy()


def respond_rideoncowboy():
    resp = "Hell Yeah, brother"
    resp2 = "*takes swig of Busch Lite*"
    c.makeCall('messages', 'Create', groupId=GROUP_ID, text=resp)
    c.makeCall('messages', 'Create', groupId=GROUP_ID, text=resp2)