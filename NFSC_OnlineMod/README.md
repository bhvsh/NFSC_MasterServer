# NFSC - OnlineMod Module

In this directory you will find a module for:

- Client online logging (packets and other stuff)
- Overriding IP addresses and ports for various parts of online services (Messenger, Plasma and Theater) and their ports where applicable

## USAGE

### End Users

1. Copy .asi and .ini from bin/Release to the scripts folder in your NFSC installation

2. Copy and replace the executable from this directory to your NFSC installation directory (if you have avoided using the Lame Patcher)

3. Configure .ini file to your liking

   3.1. If you want to connect to a custom server, set EnableOverrides to 1 and set all addresses to the custom server (Plasma, Theater and Messenger)

### Debuggers / Testers / Reverse Engineers / Snoopers

1. Copy .asi and .ini from bin/Release (or Debug, whatever you need) to the scripts folder in your NFSC installation
2. If you want to snoop packages with the EA servers (no need for WireShark and similar), set the following in the ini:
   - EnableOverrides to 0
   - EnablePrinting to 1 - for this you need a console attached to the game process, included is a ConsoleAttachment.asi
   - To eliminate crashing from an attached console, copy the World folder 2 directories ABOVE the game (yes, ../../Need for Speed Carbon, so your Program Files folder if it's at the stock location...) - this is because the game needs a BuildVersion SpeedScript file.
   - ForceSiteIP is optional (thanks to nfs-ec site being down, it's finicky, WIP on that)
   - FileLog to 1 (recommended to log to file)
   - Look at the log, decipher any data in base64 if necessary and replicate the behavior and responses of EA's server in the custom server framework
   - If a command is missing in the custom server, add it to the framework by going to the guilty party (PlasmaClient, TheaterClient or MessengerServer), create a new Python file with the command type (e.g. Framework/Server/Messenger/PSET.py if PSET is missing in MessengerServer), add it to init.py (with underscores) and finally to Network/(guilty_part).py in the dataReceived function (within the ifs and elifs) - then you can, within the newly made .py file, make a simulated response the game requires.
3. If you want to test the custom server:
   - Start the server by starting init.py in Python2
   - EnableOverrides to 1
   - EnablePrinting to 1 - for this you need a console attached to the game process, included is a ConsoleAttachment.asi
   - To eliminate crashing from an attached console, copy the World folder (found in bin) 2 directories ABOVE the game (yes, ../../Need for Speed Carbon, so your Program Files folder if it's at the stock location...) - this is because the game needs a BuildVersion SpeedScript file.
   - FileLog to 1 (recommended to log to file)
   - PlasmaAddress, TheaterAddress and MessengerAddress to localhost (or remote IP if connecting from a remote location)
   - Ports leave at default
   - Monitor the server's log and the game's log. From here you can see if any commands are missing by looking at how the game (mis)behaves (server will mark any unknowns in bright red)