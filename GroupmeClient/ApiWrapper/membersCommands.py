from .command import Command

class Add(Command):
    '''
    Add a member the group
    Params
        members: array - objects described below. nickname is required. You must use one of the following identifiers: user_id, phone_number, or email.
            object
                nickname (string) required
                user_id (string)
                phone_number (string)
                email (string)
                guid (string)
    '''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(Add, self).__init__(groupmeAccessToken, 'POST')   

    def createUrl(self):
        print(self.groupId)
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/members/add' + self.TOKEN_QUERY_STRING
    
    def createLoad(self):
        load = {}
        members = []
        array = []
        for key, value in self.args.items():
            if key == 'members':
                members = value
                hasNickname = False
                hasRequiredFields = False
                for member in members:
                    if 'nickname' in member:
                        hasNickname = True
                    if 'user_id' in member:
                        hasRequiredFields = True
                    if 'phone_number' in member:
                        hasRequiredFields = True
                    if 'email' in member:
                        hasRequiredFields = True
                    if hasNickname and hasRequiredFields:
                        array.append(member)
        load['members'] = array
        return load

    def makeCall(self):
        return super(Add, self).makeCall()

    def prepareMemberObject(self, nickname=None, user_id=None, phone_number=None, email=None):
        '''A helper method for preparing Member objects which can be passed as array members to the Add command'''
        member = {}
        if nickname is None:
            raise Exception("Nickname is required to create Member object")
        else:
            member['nickname'] = nickname
        if user_id is not None:
            member['user_id'] = user_id
        if phone_number is not None:
            member['phone_number'] =  phone_number
        if email is not None:
            member['email'] = email
        return member
        

class Remove(Command):
    '''
    Remove a member from a grup
    NOTE: Creator cannot be removed
    Params
        membership_id: string — Please note that this isn't the same as the user ID. In the members key in the group JSON, this is the id value, not the user_id.
    '''

    def __init__(self, groupmeAccessToken, groupId, membership_id=None, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        self.membership_id = membership_id
        super(Remove, self).__init__(groupmeAccessToken, 'POST')   
    
    def createUrl(self): 
        if self.membership_id is None:
            raise Exception('membership_id is required')       
        url = self.URL_BASE + '/groups/' + str(self.groupId) + '/members/' + str(self.membership_id) + '/remove' + self.TOKEN_QUERY_STRING
        return url
    
    def makeCall(self):
        return super(Remove, self).makeCall()


class Update(Command):
    '''
    Update YOUR nickname in a group. The nickname must be between 1 and 50 chars
    Params
        nickname: string - YOUR new nickname
    '''

    def __init__(self, groupmeAccessToken, groupId, nickname=None, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        self.nickname = nickname
        super(Update, self).__init__(groupmeAccessToken, 'POST')   

    def createUrl(self):
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/memberships/update' + self.TOKEN_QUERY_STRING

    def createLoad(self):
        load = {}
        load['membership'] =  {'nickname': self.nickname}
        return load

    def makeCall(self):
        super(Update, self).makeCall()


