import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, event
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID



a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleventh = STRING11
twelve = STRING12
thirteen = STRING13
fourteen  = STRING14
fifteen = STRING15
sixteen = STRING16
seventeen = STRING17
eighteen = STRING18
nineteen = STRING19
twenty = STRING20
twentyone = STRING21
twentytwo = STRING22
twentythree = STRING23
twentyfour = STRING24
twentyfive = STRING25
twentysix = STRING26
twentyseven = STRING27
twentyeight = STRING28
twentynine = STRING29
thirty = STRING30


str1 = ""
str2 = ""
str3 = ""
str5 = ""
str4 = ""
str6 = ""
str7 = ""
str8 = ""
str9 = ""
str10 = ""
str11 = ""
str12 = ""
str13 = ""
str14 = ""
str15 = ""
str16 = ""
str17 = ""
str18 = ""
str19 = ""
str20 = ""
str21 = ""
str22 = ""
str23 = ""
str24 = ""
str25 = ""
str26 = ""
str27 = ""
str28 = ""
str29 = ""
str30 = ""


que = {}

SMEX_USERS = [658876201]
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_yukki():
    global str1
    global str2
    global str3
    global str5
    global str4
    global str6
    global str7
    global str8
    global str9
    global str10
    global str11
    global str12
    global str13
    global str14
    global str15
    global str16
    global str17
    global str18
    global str19
    global str20
    global str21
    global str22
    global str23
    global str24
    global str25
    global str26
    global str27
    global str28
    global str29
    global str30
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        str1 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await str1.start()
            botme = await str1.get_me()
            await str1(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str1(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str1 = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        str1 = TelegramClient(session_name, a, b)
        try:
            await str1.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        str2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await str2.start()
            await str2(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str2(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        str2 = TelegramClient(session_name, a, b)
        try:
            await str2.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        str3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  str3.start()
            await str3(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str3(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        str3 = TelegramClient(session_name, a, b)
        try:
            await str3.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        str4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await str4.start()
            await str4(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str4(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        str4 = TelegramClient(session_name, a, b)
        try:
            await str4.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        str5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await str5.start()
            await str5(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str5(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        str5 = TelegramClient(session_name, a, b)
        try:
            await str5.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        str6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await str6.start()
            await str6(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str6(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        str6 = TelegramClient(session_name, a, b)
        try:
            await str6.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        str7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await str7.start()
            await str7(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str7(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        str7 = TelegramClient(session_name, a, b)
        try:
            await str7.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        str8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await str8.start()
            await str8(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str8(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        str8 = TelegramClient(session_name, a, b)
        try:
            await str8.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        str10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await str10.start()
            await str10(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str10(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        str10 = TelegramClient(session_name, a, b)
        try:
            await str10.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        str9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await str9.start()
            await str9(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str9(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        str9 = TelegramClient(session_name, a, b)
        try:
            await str9.start()
        except Exception as e:
            pass 
    if eleventh:
        session_name = str(eleventh)
        print("String 11 Found")
        str11 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await str11.start()
            botme = await str11.get_me()
            await str11(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str11(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str11 = "eleventh"
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        str11 = TelegramClient(session_name, a, b)
        try:
            await str11.start()
        except Exception as e:
            pass
   
    if twelve:
        session_name = str(twelve)
        print("String 12 Found")
        str12 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await str12.start()
            await str12(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str12(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        str12 = TelegramClient(session_name, a, b)
        try:
            await str12.start()
        except Exception as e:
            pass

    if thirteen:
        session_name = str(thirteen)
        print("String 13 Found")
        str13 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await  str13.start()
            await str13(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str13(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        str13 = TelegramClient(session_name, a, b)
        try:
            await str13.start()
        except Exception as e:
            pass

    if fourteen:
        session_name = str(fourteen)
        print("String 14 Found")
        str14 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await str14.start()
            await str14(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str14(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        str14 = TelegramClient(session_name, a, b)
        try:
            await str14.start()
        except Exception as e:
            pass

    if fifteen:
        session_name = str(fifteen)
        print("String 15 Found")
        str15 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await str15.start()
            await str15(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str15(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        str15 = TelegramClient(session_name, a, b)
        try:
            await str15.start()
        except Exception as e:
            pass
                  
    if sixteen:
        session_name = str(sixteen)
        print("String 16 Found")
        str16 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await str16.start()
            await str16(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str16(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        pass
        session_name = "startup"
        str16 = TelegramClient(session_name, a, b)
        try:
            await str16.start()
        except Exception as e:
            pass

    if seventeen:
        session_name = str(seventeen)
        print("String 17 Found")
        str17 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await str17.start()
            await str17(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str17(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        pass
        session_name = "startup"
        str17 = TelegramClient(session_name, a, b)
        try:
            await str17.start()
        except Exception as e:
            pass    
        
    
    if eighteen:
        session_name = str(eighteen)
        print("String 18 Found")
        str18 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await str18.start()
            await str18(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str18(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        pass
        session_name = "startup"
        str18 = TelegramClient(session_name, a, b)
        try:
            await str18.start()
        except Exception as e:
            pass   
        
    if nineteen:
        session_name = str(nineteen)
        print("String 19 Found")
        str19 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await str19.start()
            await str19(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str19(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        pass
        session_name = "startup"
        str19 = TelegramClient(session_name, a, b)
        try:
            await str19.start()
        except Exception as e:
            pass   
        
    
  
    if twenty:
        session_name = str(twenty)
        print("String 20 Found")
        str20 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await str20.start()
            await str20(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str20(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        pass
        session_name = "startup"
        str20 = TelegramClient(session_name, a, b)
        try:
            await str20.start()
        except Exception as e:
            pass   
        

    if twentyone:
        session_name = str(twentyone)
        print("String 21 Found")
        str21 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await str21.start()
            botme = await str21.get_me()
            await str21(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str21(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str21 = "twentyone"
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        str21 = TelegramClient(session_name, a, b)
        try:
            await str21.start()
        except Exception as e:
            pass
   
    if twentytwo:
        session_name = str(twentytwo)
        print("String 22 Found")
        str22 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await str22.start()
            await str22(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str22(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "startup"
        str22 = TelegramClient(session_name, a, b)
        try:
            await str22.start()
        except Exception as e:
            pass

    if twentythree:
        session_name = str(twentythree)
        print("String 23 Found")
        str23 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await  str23.start()
            await str23(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str23(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "startup"
        str23 = TelegramClient(session_name, a, b)
        try:
            await str23.start()
        except Exception as e:
            pass

    if twentyfour:
        session_name = str(twentyfour)
        print("String 24 Found")
        str24 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await str24.start()
            await str24(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str24(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "startup"
        str24 = TelegramClient(session_name, a, b)
        try:
            await str24.start()
        except Exception as e:
            pass

    if twentyfive:
        session_name = str(twentyfive)
        print("String 25 Found")
        str25 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await str25.start()
            await str25(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str25(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "startup"
        str25 = TelegramClient(session_name, a, b)
        try:
            await str25.start()
        except Exception as e:
            pass
                  
    if twentysix:
        session_name = str(twentysix)
        print("String 26 Found")
        str26 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await str26.start()
            await str26(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str26(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "startup"
        str26 = TelegramClient(session_name, a, b)
        try:
            await str26.start()
        except Exception as e:
            pass

    if twentyseven:
        session_name = str(twentyseven)
        print("String 27 Found")
        str27 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await str27.start()
            await str27(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str27(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        str27 = TelegramClient(session_name, a, b)
        try:
            await str27.start()
        except Exception as e:
            pass    
        
    
    if twentyeight:
        session_name = str(twentyeight)
        print("String 28 Found")
        str28 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await str28.start()
            await str28(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str28(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        str28 = TelegramClient(session_name, a, b)
        try:
            await str28.start()
        except Exception as e:
            pass   
        
    if twentynine:
        session_name = str(twentynine)
        print("String 29 Found")
        str29 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await str29.start()
            await str29(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str29(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        str29 = TelegramClient(session_name, a, b)
        try:
            await str29.start()
        except Exception as e:
            pass   
        
    
  
    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        str30 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await str30.start()
            await str30(functions.channels.JoinChannelRequest(channel="@QNROTUSCHAT"))
            await str30(functions.channels.JoinChannelRequest(channel="@QNR_OTUS"))
            botme = await str30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        str30 = TelegramClient(session_name, a, b)
        try:
            await str30.start()
        except Exception as e:
            pass 




loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass




        

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target



@str1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.join"))       
async def _(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "𝙹𝙾𝙸𝙽𝙸𝙽𝙶..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.leave"))       
async def _(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗟𝗲𝗮𝘃𝗲×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "𝙻𝙴𝙰𝚅𝙸𝙽𝙶....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 !!\n           〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        




@str1.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@str1.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@str1.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗕𝗶𝗴𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@str1.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗥𝗮𝗶𝗱×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@str1.on(events.NewMessage(incoming=True))
@str2.on(events.NewMessage(incoming=True))
@str3.on(events.NewMessage(incoming=True))
@str4.on(events.NewMessage(incoming=True))
@str5.on(events.NewMessage(incoming=True))
@str6.on(events.NewMessage(incoming=True))
@str7.on(events.NewMessage(incoming=True))
@str8.on(events.NewMessage(incoming=True))
@str9.on(events.NewMessage(incoming=True))
@str10.on(events.NewMessage(incoming=True))
@str11.on(events.NewMessage(incoming=True))
@str12.on(events.NewMessage(incoming=True))
@str13.on(events.NewMessage(incoming=True))
@str14.on(events.NewMessage(incoming=True))
@str15.on(events.NewMessage(incoming=True))
@str16.on(events.NewMessage(incoming=True))
@str17.on(events.NewMessage(incoming=True))
@str18.on(events.NewMessage(incoming=True))
@str19.on(events.NewMessage(incoming=True))
@str20.on(events.NewMessage(incoming=True))
@str21.on(events.NewMessage(incoming=True))
@str22.on(events.NewMessage(incoming=True))
@str23.on(events.NewMessage(incoming=True))
@str24.on(events.NewMessage(incoming=True))
@str25.on(events.NewMessage(incoming=True))
@str26.on(events.NewMessage(incoming=True))
@str27.on(events.NewMessage(incoming=True))
@str28.on(events.NewMessage(incoming=True))
@str29.on(events.NewMessage(incoming=True))
@str30.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n           〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n【﻿Command :】\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!! ᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!!\nᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@str1.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 !!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f".🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n          〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
        
        


@str1.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "【﻿ＲＥＳＴＡＲＴＩＮＧ】!!!\nPʟᴇᴀꜱᴇ Wᴀɪᴛ Tɪʟʟ lᴛ Rᴇʙᴏᴏᴛꜱ..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await str1.disconnect()
        except Exception as e:
            pass
        try:
            await str2.disconnect()
        except Exception as e:
            pass
        try:
            await str3.disconnect()
        except Exception as e:
            pass
        try:
            await str4.disconnect()
        except Exception as e:
            pass
        try:
            await str5.disconnect()
        except Exception as e:
            pass
        try:
            await str6.disconnect()
        except Exception as e:
            pass
        try:
            await str7.disconnect()
        except Exception as e:
            pass
        try:
            await str8.disconnect()
        except Exception as e:
            pass
        try:
            await str10.disconnect()
        except Exception as e:
            pass
        try:
            await str9.disconnect()
        except Exception as e:
            pass
        try:
            await str11.disconnect()
        except Exception as e:
            pass
        try:
            await str12.disconnect()
        except Exception as e:
            pass
        try:
            await str13.disconnect()
        except Exception as e:
            pass
        try:
            await str14.disconnect()
        except Exception as e:
            pass
        try:
            await str15.disconnect()
        except Exception as e:
            pass
        try:
            await str16.disconnect()
        except Exception as e:
            pass
        try:
            await str17.disconnect()
        except Exception as e:
            pass
        try:
            await str18.disconnect()
        except Exception as e:
            pass
        try:
            await str19.disconnect()
        except Exception as e:
            pass
        try:
            await str20.disconnect()
        except Exception as e:
            pass
        try:
            await str21.disconnect()
        except Exception as e:
            pass
        try:
            await str22.disconnect()
        except Exception as e:
            pass
        try:
            await str23.disconnect()
        except Exception as e:
            pass
        try:
            await str24.disconnect()
        except Exception as e:
            pass
        try:
            await str25.disconnect()
        except Exception as e:
            pass
        try:
            await str26.disconnect()
        except Exception as e:
            pass
        try:
            await str27.disconnect()
        except Exception as e:
            pass
        try:
            await str28.disconnect()
        except Exception as e:
            pass
        try:
            await str29.disconnect()
        except Exception as e:
            pass
        try:
            await str30.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n.alive\n.restart\n.join\n.pjoin\n.leave\n\n【﻿𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n.raid\n.replyraid\n.dreplyraid\n.spam\n.bigspam\n.delayspam\nFor More Help Regarding Usage Of Plugins Type Plugins Name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """𝗤𝗡𝗥 𝗦𝗣𝗔𝗠𝗠𝗘𝗥 𝗕𝗢𝗧"""

print(text)
print("")
print("DONE! 〄 ╔»⟦★𝗤𝗡𝗥★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄 STARTED.\nNOW ADD YOUR SPAMMERBOT IN ONE GROUP THEM TYPE .alive With Sudo Account")
if len(sys.argv) not in (1, 3, 4):
    try:
        str1.disconnect()
    except Exception as e:
        pass
    try:
        str2.disconnect()
    except Exception as e:
        pass
    try:
        str3.disconnect()
    except Exception as e:
        pass
    try:
        str4.disconnect()
    except Exception as e:
        pass
    try:
        str5.disconnect()
    except Exception as e:
        pass
    try:
        str6.disconnect()
    except Exception as e:
        pass
    try:
        str7.disconnect()
    except Exception as e:
        pass
    try:
        str8.disconnect()
    except Exception as e:
        pass
    try:
        str9.disconnect()
    except Exception as e:
        pass
    try:
        str10.disconnect()
    except Exception as e:
        pass
    try:
        str11.disconnect()
    except Exception as e:
        pass
    try:
        str12.disconnect()
    except Exception as e:
        pass
    try:
        str13.disconnect()
    except Exception as e:
        pass
    try:
        str14.disconnect()
    except Exception as e:
        pass
    try:
        str15.disconnect()
    except Exception as e:
        pass
    try:
        str16.disconnect()
    except Exception as e:
        pass
    try:
        str17.disconnect()
    except Exception as e:
        pass
    try:
        str18.disconnect()
    except Exception as e:
        pass
    try:
        str19.disconnect()
    except Exception as e:
        pass
    try:
        str20.disconnect()
    except Exception as e:
        pass
    try:
        str21.disconnect()
    except Exception as e:
        pass
    try:
        str22.disconnect()
    except Exception as e:
        pass
    try:
        str23.disconnect()
    except Exception as e:
        pass
    try:
        str24.disconnect()
    except Exception as e:
        pass
    try:
        str25.disconnect()
    except Exception as e:
        pass
    try:
        str26.disconnect()
    except Exception as e:
        pass
    try:
        str27.disconnect()
    except Exception as e:
        pass
    try:
        str28.disconnect()
    except Exception as e:
        pass
    try:
        str29.disconnect()
    except Exception as e:
        pass
    try:
        str30.disconnect()
    except Exception as e:
        pass
else:
    try:
        str1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str30.run_until_disconnected()
    except Exception as e:
        pass

