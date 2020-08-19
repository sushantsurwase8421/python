#!/usr/bin/python
import urllib.request
import smtplib
import os

#host = "http://www.stackoverflow.com"
#port = 80
#emails = ["surwase.sushant.d@gmail.com"] 

result = urllib.request.urlopen("http://www.go-oogle.com").getcode()
if result == 200:
    print("Good")
else:
    print("Bad")

#    if result == 200:
#        print("pod-service is running")
#    else:
#        print("pod-service is NOT running")
#else:
#    print("Jenkisn job")