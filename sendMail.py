__author__ = "Andrew Nguyen"
__copyright = "Copyright April 29, 2015"

import smtplib
import sys
import os

# Specifying the from and to addresses

fromaddr = 'anguyen@hubcitymedia.com'
toaddrs  = 'jchen@hubcitymedia.com'

if len(sys.argv) < 2:
    sys.exit('Usage: sendMail.py <filename> <value-file> ')


nfile = sys.argv[1]

if nfile[0] == "-help":
 print "'Usage sendMail.py <filename>'"
 sys.exit()

else:
 print "Program will now send email"

f = open(nfile,"r")
contents = f.read()
f.close()

# Values

if len(sys.argv) >= 3:
 pfile = sys.argv[2]
 p = open(pfile,"r")
 values = p.read()
 p.close()

else:
 print "Enter values in file to send email. Program will now exit"
 sys.exit()

test = 'hello jon chen'

# Writing the message (this message will appear in the email)

msg = "\r\n".join([
  "From: surprise@test.com",
  "To: jchen@hubcitymedia.com, anguyen@hubcitymedia.com",
  #"cc: schang@hubcitymedia.com",
  "Subject: Another test",
  "",
  contents
  ])

# Gmail Login

username = 'anguyen@hubcitymedia.com'
password = values # Uses values stored in file

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
