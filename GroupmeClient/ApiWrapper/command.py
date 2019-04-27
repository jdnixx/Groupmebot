import requests

class Command:

    def __init__(self, groupmeAccessToken, requestType):
        self.url = ''
        self.load = {}
        self.requestType = requestType
        self.accessToken = groupmeAccessToken
        print("Command init: groupmeAccessToken ="+groupmeAccessToken)
        self.URL_BASE = 'https://api.groupme.com/v3'
        self.TOKEN_QUERY_STRING = '?token=' + self.accessToken
        
    def createUrl(self):
        return self.url

    def createLoad(self):
        return self.load

    def makeCall(self):
        if self.requestType == 'POST':
            print(self.load)
            newcreateUrl = self.createUrl()
            newload = self.createLoad()
            print(newcreateUrl)
            print(newload)
            return requests.post(newcreateUrl, json = newload)
            # return requests.post(self.createUrl(), json = self.createLoad())
        elif self.requestType == 'GET':
            return requests.get(self.createUrl())
        