from Globals import Clients
from Utilities.Packet import Packet
from Database import Database

db = Database()

def ReceiveRequest(self, data):
    toSend = Packet().create()
    
    searchuser = data.get("PacketData", "USER")
    rsrc = data.get("PacketData", "RSRC")
    dist = data.get("PacketData", "DIST")
    maxr = data.get("PacketData", "MAXR")
    typeID = data.get("PacketData", "ID")
    userCount = 0
    
    toSend.set("PacketData", "ID", str(typeID))
    
    users_to_search = db.searchPersonas(searchuser)
    
    userCount = len(users_to_search)
    
    toSend.set("PacketData", "SIZE", str(userCount))
    Packet(toSend).send(self, "USCH", 0x00000000, 0)
    if userCount > 0:
        # prepare packets and send separate packet for each user TODO: prevent self adding
        for user in users_to_search:
            toSendUSER = Packet().create()
            toSendUSER.set("PacketData", "ID", str(typeID))
            toSendUSER.set("PacketData", "RSRC", "eagames/NFS-2007")
            toSendUSER.set("PacketData", "USER", user['PersonaName'])
            Packet(toSendUSER).send(self, "USER", 0x00000000, 0)
