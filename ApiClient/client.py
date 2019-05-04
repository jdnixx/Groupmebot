"""
client - groupme API client object


"""
import requests


class GroupMeApiClient(requests.Session):
    """
    The API client Session object.
    ****Currently only works for BOTS****

    :param token: assumed, for now, to be a BOT id
    """
    def __init__(self, token):
        super().__init__()
        self.URL_BASE = "https://api.groupme.com/v3"
        self.access_token = token

        # set Bot_ID
        if len(token) == 26:
            self.URL_TOKEN_STRING = '?bot_id=' + self.access_token
        else:
            raise Exception("Bot ID needs to be 26 characters long. Check your keyfile/config vars?")


    def _send_request(self, category, final_data=None):
        # category: should be "bots" ONLY for now
        # TODO: implement for GET requests
        return self.post(self.URL_BASE + f"/{category}" + "/post", final_data)

    # this is the user-facing function
    def postfrombot(self, text, picture_url=None):
        datadict = {'bot_id': self.access_token,
                    'text': text}

        if picture_url:
            attachments = {'type': 'image',
                           'url': picture_url}  # too lazy to include support for location
            datadict['attachments'] = attachments

        return self._send_request('bots', datadict)