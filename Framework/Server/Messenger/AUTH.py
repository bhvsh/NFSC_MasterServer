from Utilities.Packet import Packet

from Globals import globalUsers
from Globals import globalUserCount
from Globals import ServerUser



def ReceiveRequest(self, data):
    toSend = Packet().create()
    lkey = data.get("PacketData", "LKEY")
    
    user = ServerUser().getUserBySessionKey(lkey)
    toSend.set("PacketData", "TIID", "0")
    toSend.set("PacketData", "TITL", "Need for Speed Carbon")
    toSend.set("PacketData", "ID", "1")
    toSend.set("PacketData", "USER", user.Username+"@messaging.ea.com/eagames/NFS-2007")
    
    Packet(toSend).send(self, "AUTH", 0x00000000, 0)