import colorama
import random
import time
import hashlib
import sys
import os
import uuid
import glob
import serial.tools.list_ports

print(colorama.Fore.LIGHTGREEN_EX + "Starting HCK-1 . . . ")
alphabet = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","z","Z","x","X","k","J"]
mid_text = ["Unpacking","Loading","Compiling","Starting","Library Compilig","Error Checking","Cryptering","Decompiling","Incoding","Proxying","Executing","Setting","Configurating","Signing"]
path = ["compile.dll","dll32.zlib","run.bat","_crypter_.crypt","library64.zip","hck.exe","GUI.exe","Syquence.gh","CatRoot","mui.EXE","aadjcsp.dll","aadtb.dll","AarSvc.dll","aclui.dll","ipnathlp.dll","IPSECSVC.DLL","ISM.exe","Chakra.dll","chkntfs.exe","ChxAPDS.dll","xactengine3_3.dll","wwapi.dll","WWAHost.exe","WsmTxt.xsl","PFRO.log","csup.txt","bfsvc.exe","AcGeneral.dll","AcLayers.dll","appwiz.cpl","AtBroker.exe","attrib.exe","BitLockerCsp.dll","BitsProxy.dll","C_G18030.DLL","c_GSM7.DLL","C_IS2022.DLL","cdp.dll","cero.rs","catsrv.dll","certenc.dll","chartv.dll","ChatApis.dll","clfsw32.dll","Win32.cert","Colab.cert"]
encrypt_method = ["sha256","sha128","md5","BASE64","AES","DES","RSA","Blowfish","Twofish","Triple DES","3DES","FPE","ECC","TLS","SSL"]
binary_list = [".......",".A.H.C.",".HCK.1.","..A....","...1.0.",".0..1..","MZ!..1.","..1..A.","Z...A.H","..P..K.",".1..0.0",".A.S..K","....S..","A.J.C..","..A.Z..","...a...","...d...","...e...","...i...",".C..o..","a...p..",".a...cm"]
binary_scale = ["00000","00001","00011","00111","01111","11111","10000","11000","11100","11110","10101","01010","01101"]
RAC_URL = ["https://rtac.io","https://github.io","https://rctac.try","https://hackertyper.com","https://windows97.net","https://windows93.net","https://microsoft.com","about:blank","https://ninjaflex.com","https://bitnami.com","https://escapefromtarkov.com","LOCAL WINDOWS SERVER 11011","LOCAL WINDOWS SERVER 11211","LOCAL WINDOWS SERVER 1145","LOCAL WINDOWS SERVER 21341"]
LOG_MESSAGE = ["WinPort 11011-12022 checked","WinPort 25565-25565 checked!","WinServer Attacking NES 1","DDOS WinPort 1-2455",random.choice(path)+" Used :: DDOS Attacking",random.choice(path)+" Used :: DOS Attacking",random.choice(path)+" Used :: Hulk-DOS Attacking",random.choice(path)+" Used :: Ethical Attacking"]
dir_t_text  = ["1111000 111000 110110 101101 1101110 1100101 1110100  ",
               "1111000 111000 110110 101101 1101110 1100101 1110100  ",
               "110000 110001 110000 110001 101101 110100 1100110     ",
               "1111000 1100111 1101000 101101 1101101 1000111 1100010",
               "1001000 101101 1111000 111000 110110 101110 1101101   ",
               "1101001 1100011 1110010 1101111 1110011 1101111       ",
               "1101111 1100110 1111000 111000 101101 110100 1100110  ",
               "1111000 1100111 1101000 101101 1101101 1000111 1100010",
               "1101001 1100011 1110010 1101111 1110011 1101111       ",
               "1100110 1110100 101110 1110011 1110100 1101111 1110010",
               "1100110 1111000 110101 101101 110001 110000 1110011   ",
               "1100110 1111000 1111000 111000 110110 101101 1101110  ",
               ]

def loading():
    for i in range(random.randint(12,18)):
        print("Unpackaging Pack : " + uuid.uuid4().hex)
        time.sleep(0.05)
    print(colorama.Back.MAGENTA + "FINISHED LOADING" + colorama.Back.RESET + colorama.Fore.GREEN)

def mid_loading():
    for i in range(random.randint(25,56)):
        print(random.choice(mid_text) + " " + random.choice(path))
        time.sleep(0.05)
    print(colorama.Back.MAGENTA + "FINISHED Stage 2" + colorama.Back.RESET + colorama.Fore.GREEN)

def final_loading():
    print("\nStarting Encryption")
    for i in range(random.randint(21,34)):
        print("Encrypting : " + random.choice(path) + " Method : " + random.choice(encrypt_method))
        time.sleep(0.04)
    print(colorama.Back.MAGENTA + "ENCRYPTION FINISHED" + colorama.Back.RESET + colorama.Fore.GREEN)

def main():
    os.system("cls")
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
    
    for i in range(random.randint(25,55)):
        i = i + 1
        print("COM" , i , ': 통신 포트(COM1) [ACPI/PNP0501\0]')
        time.sleep(0.02)
        print(colorama.Back.MAGENTA + "CONNECTION PORT CHECK FINISHED" + colorama.Back.RESET + colorama.Fore.GREEN)

def MAIN_CONSOLE():
    os.system("cls")
    c_lst = ["0","1","1"]
    c = random.choice(c_lst)
    for i in range(8000):
        RAC_SYSTEM = ["Executed "+random.choice(path),"RAC SYSTEM downloaded Data from " + random.choice(RAC_URL)]
        print(colorama.Back.MAGENTA + "                                  HCK-1 HACK SYSTEM                                             " + colorama.Back.RESET)
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(f"       "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" "+random.choice(c_lst)+" " + random.choice(binary_list) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + "       " +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " [LOG] " + random.choice(LOG_MESSAGE))
        print(colorama.Back.MAGENTA + "  BINARY Ethical DECOMPILER                       Execute Logger                                 " + colorama.Back.RESET)
        print(f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " " + random.choice(RAC_SYSTEM))
        print(f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " " + random.choice(RAC_SYSTEM))
        print(f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " " + random.choice(RAC_SYSTEM))
        print(f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " " + random.choice(RAC_SYSTEM))
        print(f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) + f" " + random.choice(binary_scale) +  colorama.Back.MAGENTA + "   " + colorama.Back.RESET + " " + random.choice(RAC_SYSTEM))
        print(colorama.Back.MAGENTA + "       File LIST                                    RAC SYSTEM                                   " + colorama.Back.RESET)
        print("USAGE : ",random.randint(1,100),"% FILE   :: " + random.choice(path) + " ::         " + colorama.Back.GREEN + "   ⟫⟩⟩" + colorama.Back.RESET)
        print("USAGE : ",random.randint(1,100),"% FILE   :: " + random.choice(path) + " ::         " + colorama.Back.GREEN + "   ⟫⟩⟩" + colorama.Back.RESET)
        print(colorama.Back.MAGENTA + "                                      KPC : BTC                                                  " + colorama.Back.RESET)
        print(f" " + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet)+ random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet)+ random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + " BTC Public Wallet ʣPro")
        print(colorama.Back.MAGENTA + "                              SQL LIMITER SYSTEM                                                 " + colorama.Back.RESET)
        defend_lst = ["Port 11011","Port 20221","Port 1222","Port 2222","Port 12933","Port 2011","Port 9834"]
        print('LAYER 1 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 1 :: Advanced RAM from KSK/KGB         " + colorama.Back.RESET)
        print('LAYER 2 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 2 :: Advanced RAM from KSG/KSG         " + colorama.Back.RESET)
        print('LAYER 3 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 3 :: Advanced RAM from KSK/GmBH-K      " + colorama.Back.RESET)
        print('LAYER 4 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 4 :: Advanced RAM from KSK/HCK/Lithium " + colorama.Back.RESET)
        print('LAYER 5 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 5 :: Advanced RAM from KSK/Lithium-KS  " + colorama.Back.RESET)
        print('LAYER 6 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 6 :: Advanced RAM from KSK/LSK/sWK     " + colorama.Back.RESET)
        print('LAYER 7 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 7 :: Advanced RAM from KSK/KGB/SERV-1  " + colorama.Back.RESET)
        print('LAYER 8 ▬▬▬▬▬▬▬▬▬ ' + uuid.uuid4().hex + "  " + colorama.Back.LIGHTCYAN_EX + "LAYER 8 :: Advanced RAM from KSK/PkpAS       " + colorama.Back.RESET)
        print(colorama.Back.GREEN + "                                                                                                 " + colorama.Back.RESET)
        print("LAYER 1 USAGE : ",random.randint(1,100),"% LAYER SIZE : 8 GB DDR4")
        print("LAYER 2 USAGE : ",random.randint(1,100),"% LAYER SIZE : 16 GB DDR4 EU/US SERVER")
        print("LAYER 3 USAGE : ",random.randint(1,100),"% LAYER SIZE : 32 GB DDR4 CONNECT")
        print("LAYER 4 USAGE : ",random.randint(1,100),"% LAYER SIZE : 4 GB DDR4 Non-Type")
        print("LAYER 5 USAGE : ",random.randint(1,100),"% LAYER SIZE : 2 GB DDR4 Non-Type")
        print("LAYER 6 USAGE : ",random.randint(1,100),"% LAYER SIZE : 64 GB DDR4 CONNECT")
        print("LAYER 7 USAGE : ",random.randint(1,100),"% LAYER SIZE : 128 GB DDR4 SERVER")
        print("LAYER 8 USAGE : ",random.randint(1,100),"% LAYER SIZE : 2048 MB DDR4 LOCAL SERVER")
        print(colorama.Back.GREEN + "            SQL SYSTEM ATTACK DEFENDER             " + colorama.Back.RESET)
        print("[LOG] Defended " + random.choice(defend_lst))
        print("[LOG] Defended " + random.choice(defend_lst))
        ("[LOG] Defended " + random.choice(defend_lst))
        print("[LOG] Defended " , random.randint(1233,22333) , "WinPort")
        print("[LOG] Defended " , random.randint(1,25574) , "WinPort")
        print(colorama.Back.MAGENTA + "                 DIR TREE   ( BINARY )             " + colorama.Back.RESET)
        print(random.choice(dir_t_text))
        time.sleep(0.05)
        os.system("cls")


loading()
mid_loading()
final_loading()
main()

MAIN_CONSOLE()