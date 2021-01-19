from Utilities.Packet import Packet

def generatePackets(self, packet_type, packet_id, PacketCount):
    packetData = self.packet_data.items("PacketData")

    self.packet_data = ""
    newPacket = "ECHO\x00\x00\x00\x00\x00\x00\x00\x20"
	
    for entry in packetData:
        parameter = entry[0]
        value = entry[1]
        
        #print("param:" + parameter)
        #print("value:" + value)

        try:
            newPacket += parameter + "=" + str(value) + "\n"
        except AttributeError:
            newPacket += parameter + "=" + str(value) + "\n"
    newPacket += "\x00"
    self.packet_data = self.packet_data[:-1]
    #newPacket = "ECHO\x00\x00\x00\x00\x00\x00\x00\x20" + parameter + "=" + str(value)
   # print("packet data:" +newPacket)
    #newPacket += self.packet_data

		
        
		
    return [newPacket]

def ReceiveRequest(self, data, addr):
    packets = generatePackets(Packet(data), "ECHO", 0, 0)
	
    if packets > 1:  # More than 1 packet
        for packet in packets:
            if addr is None:
                self.transport.write(packet)
                self.logger.new_message("[" + self.ip + ":" + str(self.port) + ']--> ' + repr(packet), 3)
            else:
                self.transport.write(packet, addr)
                self.logger.new_message("[" + addr[0] + ":" + str(addr[1]) + ']--> ' + repr(packet), 3)

    else:
        if addr is None:
            self.transport.write(packets[0])
            self.logger.new_message("[" + self.ip + ":" + str(self.port) + ']--> ' + repr(packets[0]), 3)
        else:
            self.transport.write(packets[0], addr)
            self.logger.new_message("[" + addr[0] + ":" + str(addr[1]) + ']--> ' + repr(packets[0]), 3)	
	
    #toSend = data
    
   #toSend.set("PacketData", "TID", str(data.get("PacketData", "TID")))
   #toSend.set("PacketData", "TYPE", "1")
   #toSend.set("PacketData", "UID", str(data.get("PacketData", "UID")))
   #toSend.set("PacketData", "TXN", "ECHO")
   #toSend.set("PacketData", "IP", addr[0])
   #toSend.set("PacketData", "PORT", str(addr[1]))
   #toSend.set("PacketData", "ERR", "0")
    
    


    #toSend.set("PacketData", "TXN", "ECHO")
    #toSend.set("PacketData", "IP", addr[0])
    #toSend.set("PacketData", "PORT", str(addr[1]))
    #toSend.set("PacketData", "ERR", "0")
    #toSend.set("PacketData", "TYPE", "1")
    #toSend.set("PacketData", "TID", str(data.get("PacketData", "TID")))
    #Packet(data).send(self, "ECHO", 0, 0, addr)
    #Packet(toSend).send(self, "ECHO", 0x00000000, 0, addr)
