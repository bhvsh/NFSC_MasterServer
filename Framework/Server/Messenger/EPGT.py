from Utilities.Packet import Packet

def ReceiveRequest(self, data):
    toSend = Packet().create()
    typeID = data.get("PacketData", "ID")
    
    toSend.set("PacketData", "ID", str(typeID))
    toSend.set("PacketData", "ENAB", "F")
    toSend.set("PacketData", "ADDR", "ojama@da.edu")
    
    Packet(toSend).send(self, "EPGT", 0x00000000, 0)