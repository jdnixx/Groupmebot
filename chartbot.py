import os
# import GroupmeClient.client
import chartbot
from ApiClient.client import GroupMeApiClient
from TradingViewScreenshotTesting.tvchartbot import TradingViewScraper


GROUP_ID = 12375272     # nerd chat


def incoming_message(data):
    # Chartbot
    if data['name'] != "Chartbot" and data['group_id'] == "36792321":
        firstblood.incoming_message(data)