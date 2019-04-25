import unittest
from GroupmeClient import ApiWrapper
from GroupmeClient import client

class GetAllGroupsTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.command = ApiWrapper.groupCommands.GetAllGroups(self.fakeAccessToken)
        self.client_instance = client.Client(self.fakeAccessToken)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups?token=" + self.fakeAccessToken + '&page=1&per_page=10', 'Group command GetAllGroups: url not correct')


class FormerTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.command = ApiWrapper.groupCommands.Former(self.fakeAccessToken)
        self.client_instance = client.Client(self.fakeAccessToken)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/former?token=" + self.fakeAccessToken, 'Group command Former: url not correct')


class GetSingleGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '123452412'
        kwargs = {'id':self.fakeGroupId}
        self.command = ApiWrapper.groupCommands.GetSingleGroup(self.fakeAccessToken, **kwargs)
        
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/groups' + '?token=' + self.fakeAccessToken + '&id=' + self.fakeGroupId, 'Group command GetSingleGroup: url not correct')


class CreateTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '123452412'
        kwargs = {'id':self.fakeGroupId, 'name': 'test group 4'}
        self.command = ApiWrapper.groupCommands.Create(self.fakeAccessToken, **kwargs)
        
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/groups' + '?token=' + self.fakeAccessToken, 'Group command Create: url not correct')

    def test_CreateLoad(self):
        load = self.command.createLoad()
        self.assertEqual(load['name'], 'test group 4', 'Group command Create: load not correct')

class UpdateTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '123452412'
        kwargs = {'id':self.fakeGroupId, 'description': 'this is a group for testing and test like behaviors'}
        self.command = ApiWrapper.groupCommands.Update(self.fakeAccessToken, **kwargs)
        
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/groups/' + self.fakeGroupId + '/update' + '?token=' + self.fakeAccessToken, 'Group command Update: url not correct')

    def test_CreateLoad(self):
        load = self.command.createLoad()
        self.assertEqual(load['description'], 'this is a group for testing and test like behaviors', 'Group command Update: load not correct')


class DestroyTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '123452412'
        kwargs = {'id':self.fakeGroupId, 'description': 'this is a group for testing and test like behaviors'}
        self.command = ApiWrapper.groupCommands.Destroy(self.fakeAccessToken, **kwargs)
        
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/groups/' + self.fakeGroupId + '/destroy' + '?token=' + self.fakeAccessToken, 'Group command Update: url not correct')
