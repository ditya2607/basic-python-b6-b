import smtplib #https://www.youtube.com/watch?v=bXRYJEKjqIM
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = str(input("Email : "))
password = input("Password : ")
file = open("receiver_list.txt",'r')
rec_email = file.read()
file.close()

subject = str(input("Insert subject : "))

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = rec_email
msg['Subject'] = subject

body = str(input("Message : "))
msg.attach(MIMEText(body,'plain'))

filename = 'Docs.txt'
attachments = open(filename,'rb') #read as binary

part = MIMEBase('application','octet-stream') #binary file (https://kb.iu.edu/d/agtj)
part.set_payload((attachments).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename = "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)

server.sendmail(sender_email,rec_email,text)
server.quit()
