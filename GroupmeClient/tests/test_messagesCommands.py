import unittest
from GroupmeClient import ApiWrapper
from GroupmeClient import client


class GetTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        kwargs = {'limit':'20'}
        self.command = ApiWrapper.messagesCommands.Get(self.fakeAccessToken, self.fakeGroupId, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/" + str(self.fakeGroupId) + "/messages?token=" + self.fakeAccessToken + "&limit=20", 'Messages command Get: url not correct')


class CreateTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        self.fakeMessageGuid = '919633197927519'
        self.fakeText = 'Hello, Groupme.  This is a test'
        self.fakeAttachment = {'type':'image', 'url': 'http://i.groupme.com/d5e002b0a3120130b8f33ed00c848904'}
        kwargs = {'source_guid':self.fakeMessageGuid, 'text':self.fakeText, 'attachments':[self.fakeAttachment]}
        self.command = ApiWrapper.messagesCommands.Create(self.fakeAccessToken, self.fakeGroupId, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/" + str(self.fakeGroupId) + "/messages?token=" + self.fakeAccessToken, 'Messages command Create: url not correct')

    def test_CreateLoad(self):
        load = self.command.createLoad()
        fakeLoad = {}
        fakeMessage = {'source_guid': self.fakeMessageGuid,  'text': self.fakeText, 'attachments': [self.fakeAttachment]}
        fakeLoad['message'] = fakeMessage
        self.assertEqual(load, fakeLoad, 'Messages command Create: load not correct')

class LikeTestCase(unittest.TestCase):
    
    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        self.messageId = '9876543210'
        kwargs = {'limit':'20', 'message_id':self.messageId}
        self.command = ApiWrapper.messagesCommands.Like(self.fakeAccessToken, self.fakeGroupId, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/messages/' + str(self.fakeGroupId) + '/' + self.messageId + '/like?token=' + self.fakeAccessToken, 'Messages command Like: url not correct')

