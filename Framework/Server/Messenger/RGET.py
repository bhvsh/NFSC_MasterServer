from Utilities.Packet import Packet


def ReceiveRequest(self, data):
    toSend = Packet().create()
    toSendROST = Packet().create()
    typeID = data.get("PacketData", "ID")
    
    if typeID == 0:
        associations = db.getUserAssociations(self.CONNOBJ.personaID, 'MutedPlayers')
    elif typeID == 1:
        associations = db.getUserAssociations(self.CONNOBJ.personaID, 'BlockedPlayers')
    elif typeID == 2:
        associations = db.getUserAssociations(self.CONNOBJ.personaID, 'UsersFriends')
    elif typeID == 3:
        associations = db.getUserAssociations(self.CONNOBJ.personaID, 'RecentPlayers')
    else:
        associations = []
    
    toSend.set("PacketData", "ID", str(typeID))
    
    if len(associations) > 0:
        toSend.set("PacketData", "SIZE", str((len(associations))))
    else:
        toSend.set("PacketData", "SIZE", "0")
        
    for association in associations:
        toSendROST.set("PacketData", "GROUP" , "")
        toSendROST.set("PacketData", "UID", association['concernPersonaID'])
        toSendROST.set("PacketData", "ID", association['type'])
        toSendROST.set("PacketData", "ATTR", "AT")
        toSendROST.set("PacketData", "USER", association['concernPersonaName']+"@messaging.ea.com")
    
    Packet(toSend).send(self, "RGET", 0x00000000, 0)
    if len(associations) > 0:
        Packet(toSendROST).send(self, "ROST", 0x00000000, 0)