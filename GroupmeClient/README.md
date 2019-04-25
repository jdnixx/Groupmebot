# GroupmeClient-python
A python library that is a client for Groupme.  Not officially affiliated with Groupme

## Usage
Every command can be accessed by the library's simple client or by executing the command directly.
Simple client commands work by instantiating the Client class and passing the GroupMe object and command name to Client.makeCall
example:
```
client_instance = GroupmeClient.Client(accessToken)
client_instance.makeCall('groups', 'Update', **kwargs)
```
This documentation will show both usages for every command where applicable.

## Groups
Commands related to Groups GroupMe objects

### GetAllGroups
Gets all groups associated with your user
```
client_instance.makeCall('groups', 'GetAllGroups')
```

```
GroupmeClient.ApiWrapper.groupCommands.GetAllGroups(accessToken).makeCall()
```

### Former
Gets groups your user was formerly a member of
```
client_instance.makeCall('groups', 'Former')
```

```
GroupmeClient.ApiWrapper.groupCommands.Former(accessToken).makeCall()
```

### GetSingleGroup
Gets a single specified group
```
client_instance.makeCall('groups', 'GetSingleGroup')
```

```
GroupmeClient.ApiWrapper.groupCommands.GetSingleGroup(accessToken).makeCall()
```

### Create
Creates a new group

#### Params

name (required): string — Primary name of the group. Maximum 140 characters

description: string — A subheading for the group. Maximum 255 characters

image_url: string — GroupMe Image Service URL

share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.
```
kwargs = {'name':'Foo McBar'}
client_instance.makeCall('groups', 'Create', **kwargs)
```

```
kwargs = {'name':'Foo McBar'}
GroupmeClient.ApiWrapper.groupCommands.Create(accessToken, **kwargs).makeCall()
```

### Update
Updates a specified group

#### Params

id: groupid

name: string — Primary name of the group. Maximum 140 characters

description: string — A subheading for the group. Maximum 255 characters

image_url: string — GroupMe Image Service URL

share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.
```
kwargs = {'id':'1234567890', 'name':'Foo McBar', 'description': 'A GroupMe group!'}
client_instance.makeCall('groups', 'Update', **kwargs)
```

```
kwargs = {'id':'1234567890', 'name':'Foo McBar', 'description': 'A GroupMe group!'}
GroupmeClient.ApiWrapper.groupCommands.Update(accessToken, **kwargs).makeCall()
```

### Destroy
Destroys a specified group
#### Params
id: groupid
```
kwargs = {'id':'1234567890'}
client_instance.makeCall('groups', 'Destroy', **kwargs)
```

```
kwargs = {'id':'1234567890'}
GroupmeClient.ApiWrapper.groupCommands.Destroy(accessToken, **kwargs).makeCall()
```


## Messages
Commands related to message GroupMe objects for a specified group.
NOTE: all message commands by nature require a specified group

### Get
Gets messages for specified group

By default, messages are returned in groups of 20, ordered by created_at descending. This can be raised or lowered by passing a limit parameter, up to a maximum of 100 messages.

#### Params

before_id:  string — Returns messages created before the given message ID

since_id:   string — Returns most recent messages created after the given message ID

after_id:   string — Returns messages created immediately after the given message ID

limit:      integer — Number of messages returned. Default is 20. Max is 100.
```
kwargs = {'groupId':'1234567890', 'limit':20}
client_instance.makeCall('messages', 'Get', **kwargs)
```

```
kwargs = {'groupId':'1234567890', 'limit':20}
GroupmeClient.ApiWrapper.messagesCommands.Get(accessToken, **kwargs).makeCall()
```

### Create
Creates a message in the specified group

#### Params

source_guid (required): string — Client-side IDs for messages. This can be used by clients to set their own identifiers on messages, but the server also scans these for de-duplication. That is, if two messages are sent with the same source_guid within one minute of each other, the second message will fail with a 409 Conflict response. So it's important to set this to a unique value for each message.

text (required):        string — This can be omitted if at least one attachment is present. The maximum length is 1,000 characters.

attachments:            array — A polymorphic list of attachments (locations, images, etc). You may have You may have more than one of any type of attachment, provided clients can display it.
  
*elements must be one of the following object types*

##### object

type (string) — “image” required

url (string) required — Must be an image service (i.groupme.com) URL
  
##### object

type (string) — “location” required

name (string) required

lat (string) required

lng (string) required

##### object

type (string) — “split” required

token (string) required
  
##### object

type (string) — “emoji” required

placeholder (string) — “☃” required

charmap (array) — “[{pack_id},{offset}]” required
 
##### object
      
type (string) - "mentions" required

user_ids (array) - array of user ids of members being tagged
```
kwargs = {'groupId': '1234567890', 'source_guid':'1234567890', 'text': 'Sample Text', 'attachments':[{'type':'image',  'url':'http://www.imageurl.com'}]}
client_instance.makeCall('messages', 'Like', **kwargs)
```

```
kwargs = {'groupId': '1234567890', 'source_guid':'1234567890', 'text': 'Sample Text', 'attachments':[{'type':'image',  'url':'http://www.imageurl.com'}]}
GroupmeClient.ApiWrapper.messagesCommands.Like(accessToken, **kwargs).makeCall()
```

### Like
Likes the specified message
#### Params
message_id - id of the message to be liked
```
kwargs = {'groupId':'1234567890', 'message_id': '9876543210'}
client_instance.makeCall('messages', 'Like', **kwargs)
```

```
kwargs = {'groupId':'1234567890', 'message_id': '9876543210'}
GroupmeClient.ApiWrapper.messagesCommands.Like(accessToken, **kwargs).makeCall()
```

## Members
Commands related to Members GroupMe objects

### Add
Add a member the specified group
NOTE: all message commands by nature require a specified group
#### Params
members: array - objects described below. nickname is required. You must use one of the following identifiers: user_id, phone_number, or email.

*object*

nickname (string) required

user_id (string)

phone_number (string)

email (string)

guid (string)
```
kwargs = {'groupId': '1234567890', 'members': [{'nickname': 'Foo McBar', 'phone_number': '5555555555'}]}
client_instance.makeCall('members', 'Add', **kwargs)
```

```
kwargs = {'groupId': '1234567890', 'members': [{'nickname': 'Foo McBar', 'phone_number': '5555555555'}]}
GroupmeClient.ApiWrapper.membersCommands.Like(accessToken, **kwargs).makeCall()
```

### Remove
Removes specified member
#### Params
membership_id: string — Please note that this isn't the same as the user ID. In the members key in the group JSON, this is the id value, not the user_id.
```
kwargs = {'groupId': '1234567890', 'membership_id':'9876543210'}
client_instance.makeCall('members', 'Remove', **kwargs)
```

```
kwargs = {'groupId': '1234567890', 'membership_id':'9876543210'}
GroupmeClient.ApiWrapper.membersCommands.Remove(accessToken, **kwargs).makeCall()
```

### Update
Updates your member
#### Params
nickname: string - YOUR new nickname
```
kwargs = {'groupId': '1234567890', 'nickname':'Foo McBar'}
client_instance.makeCall('members', 'Update', **kwargs)
```

```
kwargs = {'groupId': '1234567890', 'nickname':'Foo McBar'}
GroupmeClient.ApiWrapper.membersCommands.Update(accessToken, **kwargs).makeCall()
```


## Users
Commands related to User GroupMe objects

The User is different than a Member in that it refers to the User of the Groupme API

### Me
Get details about the authenticated user
```
client_instance.makeCall('users', 'Me', **kwargs)
```

```
GroupmeClient.ApiWrapper.userCommands.Me(accessToken, **kwargs).makeCall()
```
