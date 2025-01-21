import smtplib 
email = input ("send email")
receiver_email = input("receiver email")

sub = input("SUBJECT")
mass = input("MASSAGE")

text = f"Subject :{sub}\n\n{mass}"

server = smtplib.SMTP("smpt.gmail.com", 578)
server.starttls()

server.login(email,"5367")
server.sendmail(email,receiver_email,text)
print("email snd to",receiver_email)



