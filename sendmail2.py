import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "collinsefe@gmail.com"
toaddr = "collinsefe@yahoo.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PYTHON TRAINING TASK 2"
 
body = "I am really loving this Python Training now Thanks Segun"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("collinsefe@gmail.com", "Quality12")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
