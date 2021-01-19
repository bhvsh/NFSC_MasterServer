Clients = []
Servers = []

globalUserCount = 0	
globalUsers = []

class ServerUser:
    Username = "username"
    UserID = 0
    sessionKey = "abcdefg"
    
    def getUserBySessionKey(self, inkey):
        for user in globalUsers:
            if user.sessionKey == inkey:
                return user
        return 0
