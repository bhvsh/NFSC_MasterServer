NFS Carbon FESL Server Emulator
=================================================

Based on [Battlefield: Bad Company 2 Master Server Emulator](https://github.com/Tratos/BFBC2_MasterServer) by [Tratos / B1naryKill3r](https://github.com/Tratos)

![Need for Speed: Carbon Cover](https://upload.wikimedia.org/wikipedia/en/a/a4/Need_for_Speed_Carbon_Game_Cover.jpg "Need for Speed: Carbon Cover")


Legal notes
-----------

- The project aren't containing *any* of the original code from the game!!! 
- It is an emulated program!
- That are imitating original server
- It is completely legal to use this code!
 

Requirements
------------

- Need for Speed Carbon
- Redirects from the official FESL servers (TODO - add override ASI code and links)

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

Setting up Client and Server (TODO - THESE INSTRUCTIONS AREN'T 100% VALID YET FOR NFS CARBON)
----------------------------

There are 2 different methods you can choose from to set them up

1. Using the dinput8.dll hook

1.1. Simply put the "dinput8.dll" file in the root directory of the Client/Server (where the executable is located)

2. Manually modifying the binaries and redirect the IP's over the hosts file

2.1. First remove the SLL verification of the executable by using the lame patcher tool (http://aluigi.altervista.org/mytoolz/lpatch.zip) with the fesl patch (http://aluigi.altervista.org/patches/fesl.lpatch)

2.2. Add this to your hosts file:

    # redirect client ip's
    xxx nfs-pc.fesl.ea.com
    xxx nfs-pc.theater.ea.com

*Where 'xxx' stands for the IP of the PC that hosts the emulator.*


TODO LIST
-----------
- Add accompanying ASI code for ingame overrides (and SSL patching)
- GLST currently crashes
- More EA Messenger backend code
- lots and lots of testing
