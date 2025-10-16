# imports EmailMessage class from email module
from email.message import EmailMessage
# ssl = secure sockets kayer.Used for encrytption.
import ssl
#smtplib = simple mail transfer protocal lib used to login into email server and disconnecti after mail is sent
import smtplib
from hi import password
email_sender = "vasumargana2028@gmail.com"
email_password = password
email_reciever = "Aveenashvasu2024@gmail.com"
subject = "Nothing bro"
body = "Just telling hi"
#Creating an instance for EmailMessage class
em = EmailMessage()
em['From'] = email_sender
em["To"]  = email_reciever
em["Subject"] = subject
em.set_content(body)
context = ssl.create_default_context()
#used to go into email server and maintain and nice connection
with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
