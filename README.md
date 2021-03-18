NFS Carbon FESL Server Emulator
=================================================

Based on [Battlefield: Bad Company 2 Master Server Emulator](https://github.com/Tratos/BFBC2_MasterServer) by [Tratos / B1naryKill3r](https://github.com/Tratos)

![Need for Speed: Carbon Cover](https://upload.wikimedia.org/wikipedia/en/a/a4/Need_for_Speed_Carbon_Game_Cover.jpg "Need for Speed: Carbon Cover")


Legal notes
-----------

- The project does not contain *any* of the original code from the game 
- It is an emulated program
- That imitates original server
- It is completely legal to use this code!

HELP WANTED
-----------
If you have expertise in making a basic matchmaking server, please contact me!

This project would greatly benefit from your help!

I am by no means qualified to write a server, this is a hack job at best.

Requirements
------------

- Need for Speed Carbon
- FESL SSL removal patch on NFSC executable
- NFSC_OnlineMod

Module           | Version | Download
----------------:|:-------:|:------------
Python           | 2.7     | [Python Download](https://www.python.org/)
colorama         | latest  | pip install colorama
passlib          | latest  | pip install passlib
Twisted          | 16.3.0  | pip install Twisted==16.3.0
pyOpenSSL        | 0.15.1  | pip install pyOpenSSL==0.15.1
cffi             | 1.3.0   | pip install cffi==1.3.0
cryptography     | 0.7.2   | pip install cryptography==0.7.2
service_identity | 1.0.0   | pip install service_identity==1.0.0

*...or just install everything via `pip install -r requirements.txt`*

Also you have to open these ports:

Port   | Type
------:|:-------
18210  | TCP/UDP
18215  | TCP/UDP
13505  | TCP
80     | TCP


Setting up the emulator
-----------------------

- Make sure that all required ports (see above) are open
- Write the IP of the PC where the emulator will be hosted in the config.ini to the key 'emulator_ip' (overwrite "localhost") and save it
- Run `Init.py`

Setting up Client and Server
----------------------------

1. Remove the SSL verification of the executable by using the lame patcher tool (http://aluigi.altervista.org/mytoolz/lpatch.zip) with the fesl patch (http://aluigi.altervista.org/patches/fesl.lpatch) (TODO - ELIMINATE THE NEED FOR THIS - this is to be included in OnlineMod)
2. Install NFSC_OnlineMod from the repository by following the instructions included in the directory. With it you can set your custom overrides for the server IP addresses.


TODO LIST
-----------
- Add accompanying ASI code for SSL patching
- GDAT currently crashes
- PlayNow / pnow (PlasmaClient) - this needs a lot of research to make matchmaking functional
- More EA Messenger backend code
- lots and lots of testing
- Python3 conversion or even a rewrite entirely?
- Support for multiple lobbies?
