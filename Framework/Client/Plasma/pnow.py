from Globals import globalServerStartID
from Globals import globalServerGameIDGen
#from Globals import globalServerLobbyIDGen
from Globals import Clients
from Utilities.Packet import Packet
from ConfigParser import ConfigParser

def HandleStatus(self, data): # TODO - figure out more of actual status calls
    toSend.set("PacketData", "TXN", "Status")
    Packet(toSend).send(self, "pnow", 0x80000000, self.CONNOBJ.plasmaPacketID)

def HandleStart(self, data): # TODO - Add PlayNow matchmaking handling here... Currently stubbed out with predef. values
    global globalServerGameIDGen 
    global globalServerStartID
    #global globalServerLobbyIDGen
    
    globalServerGameIDGen += 1
    globalServerStartID += 1
    #globalServerLobbyIDGen += 1
    
    toSend = Packet().create()
    toSend.set("PacketData", "TXN", "Start")
    toSend.set("PacketData", "id.id", str(globalServerStartID))
    toSend.set("PacketData", "id.partition", "/eagames/NFS-2007")
    Packet(toSend).send(self, "pnow", 0x80000000, self.CONNOBJ.plasmaPacketID)
    
    # start Status packet here
    toSend = Packet().create()
    toSend.set("PacketData", "sessionState", "COMPLETE")
    toSend.set("PacketData", "props.{avgFit}", "1.0")
    toSend.set("PacketData", "props.{games}.[]", "1")
    toSend.set("PacketData", "props.{games}.0.gid", str(globalServerGameIDGen))
    
    toSend.set("PacketData", "TXN", "Status")
    toSend.set("PacketData", "props.{}", "3") # total count of props?
    toSend.set("PacketData", "props.{games}.0.lid", "1")   # apparently BFBC2 server supports only 1 lobby?
    toSend.set("PacketData", "props.{resultType}", "JOIN") # resultType can also be NOSERVER if none are found
    toSend.set("PacketData", "id.id", str(globalServerStartID))
    toSend.set("PacketData", "id.partition", "/eagames/NFS-2007")
    
    # setup host client / server
    self.CONNOBJ.serverData = ConfigParser()
    self.CONNOBJ.serverData.optionxform = str
    self.CONNOBJ.serverData.add_section("ServerData")
    
    self.CONNOBJ.serverData.set("ServerData", "LID", "1")
    self.CONNOBJ.serverData.set("ServerData", "GID", str(globalServerGameIDGen))
    self.CONNOBJ.serverData.set("ServerData", "PORT", "19018") # not sure if this is constant...
    self.CONNOBJ.serverData.set("ServerData", "INT-PORT", "19018")
    self.CONNOBJ.serverData.set("ServerData", "UGID", "4e26106f-8c56-48bd-8615-824d41051c9a") # TODO GENERATE THIS
    self.CONNOBJ.serverData.set("ServerData", "NAME", "NA2CarbonPC-02-019")
    
   # hostclientname = data.get("PacketData", "players.0.props.{name}")

   # for srv in Clients:
   #     if srv.personaName == hostclientname:
   #         srv.serverData.set("ServerData", "LID", globalServerLobbyIDGen)
   #         srv.serverData.set("ServerData", "GID", globalServerGameIDGen)

    Packet(toSend).send(self, "pnow", 0x80000000, 0)
    

def ReceivePacket(self, data, txn):
    if txn == 'Start':
        HandleStart(self, data)
    elif txn == 'Status':
        HandleStatus(self)
   # elif txn == 'Ping':
   #     HandlePing(self)
   # elif txn == 'Goodbye':
   #     HandleGoodbye(self, data)
   # elif txn == 'GetPingSites':
   #     HandleGetPingSites(self)
    else:
        self.logger_err.new_message("[" + self.ip + ":" + str(self.port) + ']<-- Got unknown pnow message (' + txn + ")", 2)
