#!/usr/bin/python

import socket, re, subprocess, os, time, threading, sys, datetime, random, math, pprint #Import some necessary libraries.

#Some basic variables used to configure the bot        
server = "freeno"                                   #Server
channel = "#english"                                    #Channel
botnick = "bot-en"                                      #Your bots nick

class youthbot:
  def __init__(self, nick, server, port):
    self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.ircsock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    self.ircsock.connect((server, port))                         #Here we connect to the server using the port 6667
    self.ircsock.send(bytes("USER "+ nick +" " + nick + " " + nick + " :" + nick +"\r\n",'utf-8')) # user authentication
    self.ircsock.send(bytes("NICK "+ nick +"\n",'utf-8'))     #assign the nick to the bot
    self.ircsock.send(bytes("NS identify 0p3nt3d\n", 'utf-8'))

  def ping(self, input):
    self.ircsock.send(bytes("PONG :"+input+"\r\n",'utf-8'))

  def join(self, channel):
    self.ircsock.send(bytes("JOIN "+channel+"\r\n",'utf-8'))

  def part(self, channel):
    self.ircsock.send(bytes("PART "+channel+"\r\n",'utf-8'))

  def gettext(self):
    msg = self.ircsock.recv(1024)
    msg = str(msg.strip(bytes('\n\r','utf-8'))).strip("b'")
    return msg

  def start(self):
    ready = False
    while ready == False:
      msg = self.gettext()
      print(msg)
      if msg.find(":End of ") != -1:
        ready = True

  def run(self):
    msg = self.gettext()
    if msg.find("PING :") != -1:
      self.ping(msg.split(':')[1])
    return msg

  def quickrun(self):
    if self.gettext():
      msg = self.gettext()
      if msg.find("PING :") != -1:
        self.ping(msg.split(':')[1])
      return msg

  def mode(self, channel, mode):
    self.ircsock.send(bytes("MODE "+channel+" "+mode+"\r\n",'utf-8'))

  def ban(self, channel, user):
    self.mode(channel, "+b "+user)

  def unban(self, channel, user):
    self.mode(channel, "-b "+user)

  def message(self, channel, msg):
    self.ircsock.send(bytes("PRIVMSG "+channel+" :"+msg+"\r\n",'utf-8'))

  def modes(self, data):
    if data.find('353') >= 10 and data.find('353') <= 30:
      channel = data.split('#')[1].split(':')[0].strip()
      
      

class Channel:
  def __init__(self, name, bot):
    chan_name = name
    chan_users = 1
    chan_luser = [bot]
    chan_modes = ""

  def start_modes(self, modes):
    self.chan_modes = modes
    

# main functions of the bot
def main():
  youth.start()
  youth.join("#english-trivia")
  while 1: 
    msg = youth.run()
    print(msg)
    youth.message("#english-trivia", "This is a test")
    
#startmain function
youth = youthbot('youthframe', 'chat.freenode.net', 6667)

