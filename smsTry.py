import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from member import member

msg=MIMEMultipart("alternative")

msg['Subject']="Test Run Feel Free to delete"
msg['From']='phideltworks@gmail.com'

text=MIMEText("this is the email you will recieve for washer and dryer sytems","plain")

names=open('names.txt','r')
receivers=['ebaetiong2@gmail.com']
count=0
for line in names:
	count+=1
	name=line.split(" ")
	email=name[2]
	i=0
	for i in range(len(email)-1):
		if(email[i-1]=='e'and email[i]=='d' and email[i+1]=='u'):
			receivers.append(email[1:i+2])
		else:
			i+=1
msg['To'] = ", ".join(receivers)
print(msg)
msg.attach(text)
s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
s.login()#taken out for reasons
s.send_message(msg)
s.quit()
