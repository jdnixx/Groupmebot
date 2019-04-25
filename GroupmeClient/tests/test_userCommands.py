import unittest
from GroupmeClient import ApiWrapper
from GroupmeClient import client

class MeTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.command = ApiWrapper.userCommands.Me(self.fakeAccessToken)
        self.client_instance = client.Client(self.fakeAccessToken)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/users/me?token=" + self.fakeAccessToken, 'User command Me url not correct')
