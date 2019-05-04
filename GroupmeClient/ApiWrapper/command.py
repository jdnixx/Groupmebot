import requests

class Command:


    def __init__(self, groupmeAccessToken, requestType):
        self.url = ''
        self.load = {}

        self.requestType = requestType
        self.accessToken = groupmeAccessToken
        print("Command init: groupmeAccessToken ="+groupmeAccessToken)
        self.URL_BASE = 'https://api.groupme.com/v3'
        if len(self.accessToken) == 26:
            self.TOKEN_QUERY_STRING = '?bot_id=' + self.accessToken
        else:
            self.TOKEN_QUERY_STRING = '?token=' + self.accessToken
        
    def createUrl(self):
        return self.url

    def createLoad(self):
        return self.load

    def makeCall(self):
        if self.requestType == 'POST':
            print("Command makeCall: self.load="+str(self.load))
            #
            self.newCreateUrl = self.createUrl()
            self.newload = self.createLoad()
            print("Command makeCall: self.newCreateUrl=" + str(self.newCreateUrl))
            print("Command makeCall: self.newload="+str(self.newload))
            #
            return requests.post(self.newCreateUrl, json = self.newload)
            # return requests.post(self.createUrl(), json = self.createLoad())
        elif self.requestType == 'GET':
            return requests.get(self.createUrl())
        