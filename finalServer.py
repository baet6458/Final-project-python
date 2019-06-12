import socket
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from member import member
import thread
from socket import AF_INET

def on_new_client(clientsocket,addr):
        print("we made it to the thread")
        while True:
                msg=clientsocket.recv(1024)
		response=msg.split(',')
		if(response[0]!=None and response[0]!=""):
			print("first thing back is "+response[0])
                if(response[0] =='s'):
			message=""
                        for member in machines:
                        #send out current users
                        	message+=member.messageInfo()+"\n"
			message+="end\n"
                        print("message sent"+ message)
                        clientsocket.send(message)
                elif(response[0]=='r'):
                        #reset machine blank
			print('message: '+response[1])
                        for member in machines:
				print(member.getMachine())
				print(str(member.getMachine())==response[1])
                                if str(member.getMachine()) == response[1]:
                                        print("removing")
					machines.remove(member)
			for member in machines:
				print(member)
                elif(response[0]=='a'):
                        #need to add a person to machine
			for member in members:
				print(str(member.getBondNumber())+" "+str(response[1]==member.getBondNumber()))
				if  (response[1]==member.getBondNumber()):
					print(response[2])
					member.setMachine(response[2])
					print(member.messageInfo())
					machines.append(member)
        
                
#global variables
machines=[]
members=[]

#Grab all the info from the file
names=open('name.csv','r')
for line in names:
	temp=line.split(',')
	bondNumber=temp[0]
	name=temp[1]
	email=temp[2]
	phoneNumber=temp[3]
	temp=member(bondNumber,name,email,phoneNumber,0)
	#add it to the members list
	members.append(temp)

machines.append(member(1302,'Elijsha Baetiong','baet6458@kettering.edu','999999999',2));
machines.append(members[5])
#create a socket

serverSocket=socket.socket(AF_INET,socket.SOCK_STREAM)

serverPort=12000

serverSocket.bind(('',serverPort))
serverSocket.listen(1)


#handle everything on the socket
while 1:
        print("in while loop")
        c, addr =serverSocket.accept()
        print("client accepted")
        thread.start_new_thread(on_new_client,(c,addr))

s.close()
