Clients = []
Servers = []

globalUserCount = 0	
globalUsers = []
globalServerStartID = 0
globalServerGameIDGen = 0
globalServerLobbyIDGen = 0

class ServerUser:
    Username = "username"
    UserID = 0
    sessionKey = "abcdefg"
    
    def getUserBySessionKey(self, inkey):
        for user in globalUsers:
            if user.sessionKey == inkey:
                return user
        return 0
