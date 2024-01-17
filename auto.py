import smtplib

sender="xx@gmail.com"
receiver="yy@gmail.com"
password="**********"
Subject="this mail is automated"
body="This is my first automated mail."

message=f"""from: COC{sender}
to: you {receiver}
subject:{Subject}\n
{body}"""

server= smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender,password)
print("loggedin")

server.sendmail(sender,receiver,message)
print("email has been sent")