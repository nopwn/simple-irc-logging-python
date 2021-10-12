import ssl
import socket 
import sys

server="CHANGE THIS"
channel="CHANGE THIS"
botnick="CHANGE THIS"
port="6667"

isSSL = input("Does the server use SSL (1) no (2) yes\n")

if (isSSL == 1):
  ctx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  irc = ctx.wrap_socket(sock)
else:
  irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
port = input("What is the port?\n")
print("Connecting to: "+server+ "\\" + port + "\n")
irc.connect((server, port))
print("Connected\n")
irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :Dont worry\n", "UTF-8"))
irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

while True:
  text=irc.recv(2040)
  with open('irclog.log', 'a') as chat:
    chat.write(str(text) + "\n")
