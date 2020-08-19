#!/usr/bin/python

import socket
import smtplib

ip = "localhost"
port = 80
emails = ["uname@gmail.com","uname@gmail.com"] 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip, port))

if result == 0:
   print("pod-service is running")
else:
   print("pod-service is not running")
   
   for dest in emails: 
       s = smtplib.SMTP('smtp.gmail.com', 587) 
       s.starttls() 
       s.login("uname@gmail.com", "email_pwd") 
       SUBJECT = "POD DOWN"   
       TEXT = "Trigger new one"
       message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
       s.sendmail(emails,dest, message) 
       s.quit() 
