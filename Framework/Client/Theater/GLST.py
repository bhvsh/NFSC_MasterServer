from Globals import Servers
from Utilities.Packet import Packet


def ReceiveRequest(self, data):
    """ Game List """

    toSend = Packet().create()
    toSend.set("PacketData", "TID", str(data.get("PacketData", "TID")))
    toSend.set("PacketData", "LID", "1")
    toSend.set("PacketData", "LOBBY-NUM-GAMES", str(len(Servers)))
    toSend.set("PacketData", "LOBBY-MAX-GAMES", "1000")
    toSend.set("PacketData", "FAVORITE-GAMES", "0")
    toSend.set("PacketData", "FAVORITE-PLAYERS", "0")
    toSend.set("PacketData", "NUM-GAMES", str(len(Servers) - self.CONNOBJ.filteredServers))

    Packet(toSend).send(self, "GLST", 0x00000000, 0)

    if len(Servers) == 0 or self.CONNOBJ.filteredServers == len(Servers):
        self.CONNOBJ.filteredServers = 0
    else:
        """ Game Data """

        server = Servers[self.CONNOBJ.filteredServers]

        toSend = Packet().create()
        toSend.set("PacketData", "TID", str(data.get("PacketData", "TID")))
        toSend.set("PacketData", "LID", "1")  # id of lobby
        toSend.set("PacketData", "GID", str(server.serverData.get("ServerData", "GID")))  # id of game/server
        toSend.set("PacketData", "HN", server.personaName)  # account name of server (host name)
        toSend.set("PacketData", "HU", str(server.userID))  # account id of server (host user)
        toSend.set("PacketData", "N", str(server.serverData.get("ServerData", "NAME")))  # name of server in list

        toSend.set("PacketData", "I", server.ipAddr)
        toSend.set("PacketData", "P", str(server.serverData.get("ServerData", "PORT")))  # Port

        toSend.set("PacketData", "JP", str(server.joiningPlayers))  # Players that are joining the server right now?
        toSend.set("PacketData", "QP", str(server.serverData.get("ServerData", "B-U-QueueLength")))  # Something with the queue...lets just set this equal to B-U-QueueLength
        toSend.set("PacketData", "AP", str(server.activePlayers))  # current number of players on server
        toSend.set("PacketData", "MP", str(server.serverData.get("ServerData", "MAX-PLAYERS")))  # Maximum players on server
        toSend.set("PacketData", "PL", "PC")  # Platform - PC / XENON / PS3

        """ Constants """
        toSend.set("PacketData", "F", "0")  # ???
        toSend.set("PacketData", "NF", "0")  # ???
        toSend.set("PacketData", "J", str(server.serverData.get("ServerData", "JOIN")))  # ??? constant value - "O"
        toSend.set("PacketData", "TYPE", str(server.serverData.get("ServerData", "TYPE")))  # what type?? constant value - "G"
        toSend.set("PacketData", "PW", "0")  # ??? - its certainly not something like "hasPassword"

        """ Other server specific values """
        toSend.set("PacketData", "B-U-matchmaking_state", str(server.serverData.get("ServerData", "B-U-matchmaking_state")))
        toSend.set("PacketData", "B-U-team_play", str(server.serverData.get("ServerData", "B-U-team_play")))
        toSend.set("PacketData", "B-U-car_tier", str(server.serverData.get("ServerData", "B-U-car_tier")))
        toSend.set("PacketData", "B-U-game_mode", str(server.serverData.get("ServerData", "B-U-game_mode")))
        toSend.set("PacketData", "B-U-help_type", str(server.serverData.get("ServerData", "B-U-help_type")))
        toSend.set("PacketData", "B-U-player_dnf", str(server.serverData.get("ServerData", "B-U-player_dnf")))

        toSend.set("PacketData", "B-version", str(server.serverData.get("ServerData", "B-version")))  # Version of the server (exact version) - TRY TO CONNECT TO ACTUAL VERSION OF SERVER
        toSend.set("PacketData", "V", str(server.clientVersion))  # "clientVersion" of server (shows up in server log on startup)
        toSend.set("PacketData", "B-U-max_online_player", str(server.serverData.get("ServerData", "B-U-max_online_player"))) 
        toSend.set("PacketData", "B-U-n2o", str(server.serverData.get("ServerData", "B-U-n2o")))
        toSend.set("PacketData", "B-U-track", str(server.serverData.get("ServerData", "B-U-track")))
        toSend.set("PacketData", "B-U-collision_detection", str(server.serverData.get("ServerData", "B-U-collision_detection")))
        toSend.set("PacketData", "B-U-version", str(server.serverData.get("ServerData", "B-U-version")))
        toSend.set("PacketData", "B-U-race_type_sprint", str(server.serverData.get("ServerData", "B-U-race_type_sprint")))
        toSend.set("PacketData", "B-U-race_type_pursuit_tag", str(server.serverData.get("ServerData", "B-U-race_type_pursuit_tag")))
        toSend.set("PacketData", "B-U-race_type_speedtrap", str(server.serverData.get("ServerData", "B-U-race_type_speedtrap")))

        toSend.set("PacketData", "B-U-game_type", str(server.serverData.get("ServerData", "B-game_type")))
        toSend.set("PacketData", "B-U-race_type_canyon_due", str(server.serverData.get("ServerData", "B-U-race_type_canyon_due")))
        toSend.set("PacketData", "B-U-race_type_circuit", str(server.serverData.get("ServerData", "B-U-race_type_circuit")))
        toSend.set("PacketData", "B-U-race_type_knockout", str(server.serverData.get("ServerData", "B-U-race_type_knockout")))
        toSend.set("PacketData", "B-U-length", str(server.serverData.get("ServerData", "B-U-length")))  # players in queue or maximum queue

      #  if server.serverData.get("ServerData", "B-U-Punkbuster") == 1:
      #      toSend.set("PacketData", "B-U-PunkBusterVersion", "1")

        Packet(toSend).send(self, "GDAT", 0x00000000, 0)
        self.CONNOBJ.filteredServers += 1
