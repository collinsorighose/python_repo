#!/bin/python

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("collinsefe@gmail.com", "Quality12")
 
msg = "PYTHON TRAINING MAIL TASK CONFIRMED!"
server.sendmail("collinsefe@gmail.com", "collinsefe@yahoo.com", msg)
server.quit()

