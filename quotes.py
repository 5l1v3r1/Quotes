#!/usr/bin/python
# -*- coding: utf-8 -*-
# My Quotes
# Coded by Senja
# Github: github.com/stepbystepexe/Quotes

import os, sys, time, json
try:
        import requests
except ConnectionError:
        os.system('clear')
        os.system('reset')
        rqs = raw_input('\033[0m[\033[92;1m+\033[0m] \033[1;77mMust install first  requests \033[0m[Y/n] \033[1;77m: ')
        if rqs =="":
                print ("\033[0m[\033[1;91m!\033[0m] \033[1;77mNot empty\033[0m")
                exit(1)
        elif rqs =="y":
                os.system('pip2 install requests')
                exit(1)
        elif rqs =="Y":
                os.system('pip2 install requests')
                exit(1)
        elif rqs =="n":
                os.sys.exit(1)
        elif rqs =="N":
                os.sys.exit(1)
        else:
                print ("\033[0m[\033[96;1m/\033[0m] \033[1;77mSelect \033[0m[Y/n]: \033[0m")
                time.sleep(1)
                os.sys.exit(1)

from requests.exceptions import ConnectionError

logo = """\033[0;1;77m
      ______ ______        \033[0;100m Enjoy Yor Life \033[0m
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\\\     \033[0m[\033[94;1m#\033[0m] My Quotes\033[0;77m
  // ~ ~ ~~ | ~~~ ~~ \\\    \033[0m[\033[93;1m*\033[0m] Coded Senja\033[0;77m
 //________.|.________\\\   \033[0m[\033[96;1m&\033[0m] My Github: @thedarksec\033[0;77m
`----------`-'----------'
"""

def quotes():
        try:
                os.system('clear')
                os.system('reset')
                time.sleep(1)
                print (logo)
                r = requests.get("http://quotes.stormconsultancy.co.uk/random.json")
                q = json.loads(r.text)
                print ("\033[0;1;77m")
                msg = q["quote"]
                auth = q["author"]
                link = q["permalink"]
                print ("__________________________________________________________")
                print
                print (msg)
                print ("__________________________________________________________")
                print
                print ("\n\n\n")
                print ("\033[0m[\033[1;92m~\033[0m] \033[1;77mAuth\033[0m ")+auth
                print ("\033[0m[\033[1;95m#\033[0m] \033[1;77mSource\033[0m ")+link
                raw_input("\n\033[0m[\033[1;93m*\033[0m] \033[1;77mEnter to next: ")
                quotes()
        except KeyboardInterrupt:
                print
                print ("\033[0m[\033[91;1m!\033[0m] \033[1;77mExit the program!\033[0m")
                print
                exit(1)
        except requests.exceptions.ConnectionError:
                print
                print ("\033[0m[\033[91;1m!\033[0m] \033[1;77mNo connection network!\033[0m")
                print
                exit(1)

quotes()
