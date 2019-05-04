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
    def __init__(self, token, botid):
        super().__init__()
        self.URL_BASE = "https://api.groupme.com/v3"
        self.access_token = token
        self.botid = botid

        # set bot ID
        # if len(token) == 26:
        #     self.URL_TOKEN_STRING = '?bot_id=' + self.access_token
        # else:
        #     raise Exception("Bot ID needs to be 26 characters long. Check your keyfile/config vars?")


    def _send_request(self, category, final_data=None):
        # category: should be "bots" ONLY for now
        # TODO: implement for GET requests
        return self.post(self.URL_BASE + f"/{category}" + "/post", final_data)


    def get_pic_upload_url(self, picfile):
        """
        Uploads a picture to Groupme's Image Service and returns the image's URL.
        https://dev.groupme.com/docs/image_service

        :param picfile: file-like object of the desired image. NOTE: open in binary mode, i.e. open(<file>, 'rb')
        :return: URL of newly uploaded image on groupme's servers
        """
        url_base_pictures = 'https://image.groupme.com/pictures'

        resp = self.post(url_base_pictures + '?token=' + self.access_token, data=picfile)
        jsonresp = resp.json()
        picurl = jsonresp['payload']['picture_url']
        return picurl


    # this is the user-facing function
    def postfrombot(self, text, picture_url=None):
        datadict = {'bot_id': self.botid,
                    'text': text}

        if picture_url:
            # attachments = {'type': 'image',
            #                'url': picture_url}  # too lazy to include support for location
            # datadict['attachments'] = attachments
            datadict['picture_url'] = picture_url

        return self._send_request('bots', datadict)