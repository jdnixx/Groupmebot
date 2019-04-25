from .ApiWrapper import groupCommands
from .ApiWrapper import membersCommands
from .ApiWrapper import messagesCommands
from .ApiWrapper import userCommands
# from config import config



class Client(object):

    def __init__(self, groupmeAccessToken):
        self.accessToken = groupmeAccessToken

    def makeCall(self, groupmeObject, call, **kwargs):
        '''
        Currently implemented calls, by groupmeObject\n
        \n
        users
            Get
        groups
            GetAllGroups
            Former
            GetSingleGroup
            Create
            Update
            Destroy
        members
            Add
            Remove
            Update
        messages
            Get
            Create
            Like

        '''

        if  groupmeObject == 'users':
            return getattr(userCommands, call)(self.accessToken, **kwargs).makeCall()
        
        if groupmeObject == 'groups':
            groups_instance = getattr(groupCommands, call)(self.accessToken, **kwargs)
            return groups_instance.makeCall()

        if groupmeObject == 'members':
            return getattr(membersCommands, call)(self.accessToken, **kwargs).makeCall()
            
        if groupmeObject == 'messages':
            return getattr(messagesCommands, call)(self.accessToken, **kwargs).makeCall() #do not have to explicitly pass groupId b/c it's in kwargs under the same name
        
        return 'error'
            










# # # help(groups.getGroups())
# client = Client(config['accessToken'])
# print(client.makeCall('groups', 'createGroup', name='Client Test Group2'))

