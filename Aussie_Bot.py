#!/usr/local/bin/python

import socket
import ssl
import time
import weatherdefine
import timelookup
import admin
import sys
## Settings
### IRC
server = "chat.freenode.net"
port = 6697
channel = "##aussies"
botnick = ""
password = ""
admin = ""

### Tail
tail_files = [
    'love.txt'
]

irc_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
irc = ssl.wrap_socket(irc_C)

print "Establishing connection to [%s]" % (server)
# Connect
irc.connect((server, port))
irc.setblocking(False)
#irc.send("PASS %s\n" % (password))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :meLon-Test\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (botnick, password))
time.sleep(10)
irc.send("JOIN "+ channel +"\n")



with open("wordlist.txt") as f:
    my_lines = f.readlines()
print my_lines

while True:

    reload(timelookup)
    reload(weatherdefine)
    try:
        text=irc.recv(2040)
        print(text)
        user = text.split("!")
        user = user[0].strip(":")

        if text.find('my place') != -1:
            print(user)
            irc.send("PRIVMSG "+ channel +" :" + weatherdefine.weather(user) + '\r\n')

        if text.find('!t') != -1:
            city = text.split("!t")
            city = city[1]
            print (city)
            irc.send("PRIVMSG "+ channel +" :" + timelookup.get_localized_time(city) + '\r\n')


        '''if text.find(":hi") !=-1:
            user = text.split("!")
            user = user[0].strip(":")
            print user
            irc.send("PRIVMSG "+ channel +" :Hello!\r\n")'''
            

            



            

        # Prevent Timeout
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')
            print("PONG")

    except Exception:
        continue

