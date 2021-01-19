#from Globals import Clients
from Globals import globalUsers
from Globals import globalUserCount
from Globals import ServerUser

from Utilities.Packet import Packet


def ReceiveRequest(self, data):
    toSend = Packet().create()

    lkey = data.get("PacketData", "LKEY")
    
    user = ServerUser().getUserBySessionKey(lkey)
    
    if user == 0:
        self.transport.loseConnection()
        return

   #for client in Clients:
   #  if client.personaSessionKey == lkey:
   #      self.CONNOBJ = client
   # # self.logger_err.new_message("Client:" + client.personaSessionKey)
   #
   #if self.CONNOBJ is None:
   #    self.transport.loseConnection()
   #else:
    toSend.set("PacketData", "NAME", user.Username)
    toSend.set("PacketData", "TID", str(data.get("PacketData", "TID")))
    

    Packet(toSend).send(self, "USER", 0x00000000, 0)
