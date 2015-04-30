import smtplib

# Specifying the from and to addresses

fromaddr = 'anguyen@hubcitymedia.com'
toaddrs  = 'jchen@hubcitymedia.com'

# Writing the message (this message will appear in the email)

msg = "\r\n".join([
  "From: surprise@test.com",
  "To: jchen@hubcitymedia.com, anguyen@hubcitymedia.com",
  "cc: schang@hubcitymedia.com",
  "Subject: Just a message",
  "",
  "Wooo"
  ])

# Gmail Login

username = 'anguyen@hubcitymedia.com'
password = '<password goese here>'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
