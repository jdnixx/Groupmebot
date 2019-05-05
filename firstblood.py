"""
FIRSTBLOOD - first GroupMe API bot

Mostly for testing API connectivity & commands
"""
import os
# import GroupmeClient.client
from ApiClient.client import GroupMeApiClient
from TradingViewScreenshotTesting.tvchartbot import TradingViewScraper

GROUP_ID = 12375272     # nerd chat

"""
Client setup

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

"""
Client setup alternate method:
using environment variables

Meant for use with Heroku CONFIG_VARS:
TOKEN
BOT_ID
"""
TOKEN = os.environ.get('TOKEN')
BOTID = os.environ.get('BOT_ID')

c = GroupMeApiClient(TOKEN, BOTID)

tvbot = TradingViewScraper()


def incoming_message(data):
    """
    Main method invoked when a new message arrives from the group.
    The (flask) app receives a POST with the new message, and it is immediately sent here.
    :param data: dict of JSON data from GroupMe API's POST request
    :return:
    """
    # parse message
    msg = data['text'].strip().lower()

    # simple mirror response commands
    if msg == "ride on cowboy":
        respond_rideoncowboy()
    if msg == "jeremy is a":
        jeremyisa()
    # echo command
    if msg.startswith('echo'):
        echo(data['text'])
    # Tradingview Chart screenshot
    if msg.startswith('c '):
        chart(data['text'])






def respond_rideoncowboy():
    resp = "Hell Yeah, brother"
    resp2 = "*takes swig of Busch Lite*"
    print("respond_rideoncowboy should be working...")
    c.postfrombot(resp)
    c.postfrombot(resp2)
    # c.makeCall('bots', 'Post', text=resp)
    # c.makeCall('bots', 'Post', text=resp2)
    # c.makeCall('messages', 'Create', groupId=GROUP_ID, text=resp)
    # c.makeCall('messages', 'Create', groupId=GROUP_ID, text=resp2)


def jeremyisa():
    c.postfrombot('PEEPEEPOOPOOOOOO')
    # c.makeCall('bots', 'Post', text='PEEPEEPOOPOOOOOO')


def echo(text):
    """
    Echoes the message after the command by <multiplier> number of times.
    Invoked with "echo 2x <message>" where 2x is the multiplier; can be up to 20.
    :param text: raw text from latest group message
    :return:
    """
    indexofx = text.find('x')
    multiplier = int(text[5:indexofx])
    if multiplier > 10:
        multiplier = 10     # cap the number of repeats at 20x
    message_to_repeat = text[indexofx+2:]
    for i in range(multiplier):
        c.postfrombot(message_to_repeat)
        # c.makeCall('bots', 'Post', text=text)


def postpic(fpicture_binary):
    """
    Uploads & posts a picture, with its filename as the parameter.
    Picture file must be in same directory as firstblood.py.
    :param fpicture_binary: file-like object of the desired image to be posted
    :return:
    """
    url = c.get_pic_upload_url(fpicture_binary)
    c.postfrombot(" ", picture_url=url)



def chart(text):
    split = text.split()

    symbol = split[1]

    fchartpic = tvbot.get_chart_screenshot_binary(symbol)
    postpic(fchartpic)