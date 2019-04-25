import unittest
from GroupmeClient import ApiWrapper
from GroupmeClient import client


class AddTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        self.fakeMessageId = '9876543210'
        self.fakeNickname = 'Bobby Joe'
        self.fakeEmail = 'bobby.joe@testgroupmeemail.com'
        kwargs = {'groupId':self.fakeGroupId, 'message_id':self.fakeMessageId, 'members':[{'nickname':self.fakeNickname, 'email':self.fakeEmail}]}
        self.command = ApiWrapper.membersCommands.Add(self.fakeAccessToken, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/" + str(self.fakeGroupId) + "/members/add?token=" + self.fakeAccessToken, 'Members command Add: url not correct')

    def test_CreateLoad(self):
        load = self.command.createLoad()
        fakeLoad = {}
        fakeMembersArray = [{'nickname':self.fakeNickname, 'email':self.fakeEmail}]
        fakeLoad['members'] = fakeMembersArray
        self.assertEqual(load, fakeLoad, 'Members command Add: load not correct')


class RemoveTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        self.fakeMembershipId = '9876543210'
        kwargs = {'groupId':self.fakeGroupId, 'membership_id':self.fakeMembershipId}
        self.command = ApiWrapper.membersCommands.Remove(self.fakeAccessToken, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/" + str(self.fakeGroupId) + "/members/" + self.fakeMembershipId + "/remove?token=" + self.fakeAccessToken, 'Members command Add: url not correct')


class UpdateTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '1234567890'
        self.fakeNickname = 'Bobby Joe'
        kwargs = {'groupId':self.fakeGroupId, 'nickname':self.fakeNickname}
        self.command = ApiWrapper.membersCommands.Update(self.fakeAccessToken, **kwargs)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/" + str(self.fakeGroupId) + "/memberships/update?token=" + self.fakeAccessToken, 'Members command Add: url not correct')

    def test_CreateLoad(self):
        load = self.command.createLoad()
        fakeLoad = {}
        fakeMemberDict = {'nickname':self.fakeNickname}
        fakeLoad['membership'] = fakeMemberDict
        self.assertEqual(load, fakeLoad, 'Members command Add: load not correct')
