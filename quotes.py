#!/usr/bin/python
# -*- coding: utf-8 -*-
# Quotes
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Quotes

import os, sys, time, json

try:
        import requests
except ConnectionError:
        os.system('clear')
        os.system('reset')
        o = input('\033[0m[\033[92;1m+\033[0m] \033[1;77mInstall modul requests \033[0m[Y/n] \033[1;77m: ')
        if o =="":
                print("\033[0m[\033[1;91m!\033[0m] \033[1;77mPilihan salah\033[0m\n")
                exit(1)
        elif o.strip() in 'y Y'.split():
                os.system('pip2 install requests')
                exit(1)
        elif o.strip() in 'n N'.split():
                sys.exit(1)
        else:
                print("\033[0m[\033[96;1m/\033[0m] \033[1;77mPilih \033[0m[Y/n]: \033[0m")
                time.sleep(1)
                os.sys.exit(1)

from requests.exceptions import ConnectionError

logo = """\033[0;1;77m
      ______ ______        \033[0;100;77;1m[=   Enjoy Your Life   =]\033[0m
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\\\     \033[0m[\033[91;1m-\033[0m] My Quotes\033[0;77m
  // ~ ~ ~~ | ~~~ ~~ \\\    \033[0m[\033[92;1m#\033[0m] Coded by Nedi Senja\033[0;77m
 //________.|.________\\\   \033[0m[\033[94;1m*\033[0m] My Github: @stepbystepexe\033[0;77m
`----------`-'----------'
"""

def start():
        try:
                os.system('clear')
                os.system('reset')
                time.sleep(1)
                print(logo)
                r = requests.get("http://quotes.stormconsultancy.co.uk/random.json")
                q = json.loads(r.text)
                print("\033[0;1;77m")
                msg = q["quote"]
                auth = q["author"]
                link = q["permalink"]
                print(58*"_")
                print()
                print(msg)
                print(58*"_")
                print()
                print("\n\n\n")
                print("\033[0m[\033[1;92m~\033[0m] \033[1;77mAuthor\033[0m "+auth)
                print("\033[0m[\033[1;95m#\033[0m] \033[1;77mLink\033[0m "+link)
                input("\n\033[0m[\033[1;93m*\033[0m] \033[1;77mTekan Enter: ")
                start()
        except KeyboardInterrupt:
                print()
                print("\033[0m[\033[91;1m!\033[0m] \033[1;77mKeluar dari program!\033[0m")
                print()
                sys.exit(1)
        except requests.exceptions.ConnectionError:
                print()
                print("\033[0m[\033[91;1m!\033[0m] \033[1;77mTidak ada koneksi\033[0m")
                print()
                sys.exit(1)
start()
