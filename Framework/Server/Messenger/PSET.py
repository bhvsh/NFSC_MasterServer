from Utilities.Packet import Packet

def ReceiveRequest(self, data):
    toSend = Packet().create()
    typeID = data.get("PacketData", "ID")
    
    toSend.set("PacketData", "ID", str(typeID))
    
    Packet(toSend).send(self, "PSET", 0x00000000, 0)