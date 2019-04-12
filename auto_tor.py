#!/usr/bin/python

import os
import time


os.system("clear")
print("""
    _         _          _____          
   / \  _   _| |_ ___   |_   _|__  _ __ 
  / _ \| | | | __/ _ \    | |/ _ \| '__|
 / ___ \ |_| | || (_) |   | | (_) | |   
/_/   \_\__,_|\__\___/    |_|\___/|_|   
                                    
""")

print("Coded By D7OOM Al-kurdi")
tools = input('first u need install some tools (Y) or (N):')
if tools == 'Y' or tools == 'y':
    os.system("sudo apt-get install tor")
    os.system("sudo apt-get install privoxy")
    time.sleep(10)
    print ('Tool Been Installed !')
    os.system('service tor start')
if tools == 'N' or tools == 'n':
    os.system('service tor start')
print ('Please Change Your Proxy To 127.0.0.1 and Change Port To 9050 \n')
os.system('service tor start')
ip = input("Type oF Change Ip Addres In Secend Example:60:")
ip = int(ip)
ip_time = input("How Many Change Ip in Your Ip Addres (Max=100):")
ip_time = int(ip_time)

for i in range(ip_time):
    print ("We Are Kurdish Grey Hacker")
    time.sleep(ip)
    ip = int(ip)
    os.system("service tor reload")
    print("Ip Been Changed (Ip Godra)")