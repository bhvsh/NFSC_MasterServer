#include "stdafx.h"
#include "stdio.h"
#include "includes\injector\injector.hpp"
#include "includes\IniReader.h"

#define ONLINEMOD_DEF_LOGFILENAME "OnlineLog.txt"
#define ONLINEMOD_DEF_SITEIP "159.153.72.181"

char* PlasmaAddress;
char* TheaterAddress;
char* MessengerAddress;
//int PlasmaPort;
int TheaterPort;
int MessengerPort;
short int ListenPort;
char* HTTPBase;
char* Platform;

int ConnMgrAddress = 0;

bool bEnableOverrides = false;
bool bEnablePrinting = false;
bool bFileLog = false;
bool bForceSiteIP = false;

char* LogFileName = ONLINEMOD_DEF_LOGFILENAME;
bool bTriedToOpenLogFile = false;
FILE* LogFile = NULL;

char* ForcedSiteIP = ONLINEMOD_DEF_SITEIP;
char ForcedSiteIPIntStr[16];



unsigned int ip_to_int(const char * ip)
{
	/* The return value. */
	unsigned v = 0;
	/* The count of the number of bytes processed. */
	int i;
	/* A pointer to the next digit to process. */
	const char * start;

	start = ip;
	for (i = 0; i < 4; i++) {
		/* The digit being processed. */
		char c;
		/* The value of this byte. */
		int n = 0;
		while (1) {
			c = *start;
			start++;
			if (c >= '0' && c <= '9') {
				n *= 10;
				n += c - '0';
			}
			/* We insist on stopping at "." if we are still parsing
			the first, second, or third numbers. If we have reached
			the end of the numbers, we will allow any character. */
			else if ((i < 3 && c == '.') || i == 3) {
				break;
			}
			else {
				return -1;
			}
		}
		if (n >= 256) {
			return -1;
		}
		v *= 256;
		v += n;
	}
	return v;
}

void OnlinePrint(void* unk, char const* str)
{
	if (bEnablePrinting)
		printf("%s", str);

	if (bFileLog)
	{
		if (LogFile == NULL)
		{
			if (!bTriedToOpenLogFile)
			{
				LogFile = fopen(LogFileName, "w");
				bTriedToOpenLogFile = true;
				if (LogFile == NULL)
					printf("ERROR: Can't open %s for logging!\n", LogFileName);
			}
		}
		else
		{
			fprintf(LogFile, "%s", str);
			fflush(LogFile);
		}

	}
}

int __stdcall StuffInOverrides()
{
	//_asm mov ConnMgrAddress, ecx
	int ConnMgrDeRef = *(int*)0xBCB344;

	ConnMgrDeRef = (ConnMgrDeRef + 0x4C);

	*(int*)(ConnMgrDeRef + 8) = MessengerPort;
	//*(int*)(ConnMgrDeRef + 0xC) = TheaterPort;
	*(short int*)(ConnMgrDeRef + 0x38) = ListenPort;
	strcpy((char*)((ConnMgrDeRef + 0x58)), PlasmaAddress);
	strcpy((char*)((ConnMgrDeRef + 0x98)), MessengerAddress);
	//strcpy((char*)((ConnMgrDeRef + 0xD8)), TheaterAddress);
	strcpy((char*)((ConnMgrDeRef + 0x118)), HTTPBase);
	strcpy((char*)((ConnMgrDeRef + 0x398)), Platform);


	return ConnMgrDeRef;
}

//int(__thiscall* PingSite)(void* dis, int ip_addr, int unk1, int unk2) = (int(__thiscall*)(void*, int, int, int))0x94F5E0;
//int __stdcall PingSiteHijack(int ip_address, int unk1, int unk2)
//{
//	unsigned int TheThis = 0;
//	_asm mov TheThis, ecx
//	printf("Hijacking site to: %s\n", ForcedSiteIP);
//
//	return PingSite((void*)TheThis, IPtoInt(ForcedSiteIP), unk1, unk2);
//}

int(__thiscall* PingSite2)(void* dis, char* ip_addr, int unk1, int unk2) = (int(__thiscall*)(void*, char*, int, int))0x94F560;
int __stdcall PingSiteHijack(int ip_address, int unk1, int unk2)
{
	unsigned int TheThis = 0;
	_asm mov TheThis, ecx
	sprintf(ForcedSiteIPIntStr, "$%x", _byteswap_ulong(ip_to_int(ForcedSiteIP)));
	//printf("Hijacking site to: %s / %x\n", ForcedSiteIP, ip_to_int(ForcedSiteIP));

	return PingSite2((void*)TheThis, ForcedSiteIPIntStr, unk1, unk2);
}

int InitConfig()
{
	CIniReader inireader("");
	bEnableOverrides = inireader.ReadInteger("OnlineMod", "EnableOverrides", 0) == 1;
	bEnablePrinting = inireader.ReadInteger("OnlineMod", "EnablePrinting", 0) == 1;
	bForceSiteIP = inireader.ReadInteger("OnlineMod", "ForceSiteIP", 0) == 1;
	bFileLog = inireader.ReadInteger("OnlineMod", "FileLog", 0) == 1;
	LogFileName = inireader.ReadString("OnlineMod", "LogFilename", ONLINEMOD_DEF_LOGFILENAME);

	PlasmaAddress = inireader.ReadString("Overrides", "PlasmaAddress", "nfs-pc.fesl.ea.com");
	TheaterAddress = inireader.ReadString("Overrides", "TheaterAddress", "nfs-pc.theater.ea.com");
	MessengerAddress = inireader.ReadString("Overrides", "MessengerAddress", "messaging.ea.com");

	//PlasmaPort = inireader.ReadInteger("Overrides", "PlasmaPort", 18210);
	TheaterPort = inireader.ReadInteger("Overrides", "TheaterPort", 18215);
	MessengerPort = inireader.ReadInteger("Overrides", "MessengerPort", 13505);
	ListenPort = inireader.ReadInteger("Overrides", "ListenPort", 1042);

	HTTPBase = inireader.ReadString("Overrides", "HTTPBase", "80");

	Platform = inireader.ReadString("Overrides", "Platform", "PC");
	ForcedSiteIP = inireader.ReadString("Overrides", "ForcedSiteIP", ONLINEMOD_DEF_SITEIP);

	return 0;
}

int Init()
{
	InitConfig();

	if (bEnableOverrides)
		injector::MakeCALL(0x93E219, StuffInOverrides, true);

	if (bForceSiteIP)
	{
		injector::MakeCALL(0x94F960, PingSiteHijack, true);
		injector::MakeCALL(0x94FACA, PingSiteHijack, true);
	}
	injector::WriteMemory<int>(0x008345C6, (int)&OnlinePrint, true);

	return 0;
}

BOOL APIENTRY DllMain(HMODULE /*hModule*/, DWORD reason, LPVOID /*lpReserved*/)
{
	if (reason == DLL_PROCESS_ATTACH)
	{
		freopen("CON", "w", stdout);
		freopen("CON", "w", stderr);
		Init();
	}
	return TRUE;
}

