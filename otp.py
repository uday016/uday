import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp = random.randint(1111,9999)
months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
name=input("Enter your name: ")
day=int(input("enter ur birth day:"))
month=int(input("enter ur birth month: "))
year=int(input("enter ur birth year: "))


tomail = input("Enter Mail id: ")
subject = "otp for validation"
body = f"Hello{name}!\n birth day={day}-{months[month]}-{year}\notp is{otp}"

msg = MIMEMultipart()
msg['FROM'] = "anugulaudai@gmail.com"
msg['To'] = tomail
msg['subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('anugulaudai@gmail.com','mykt ptui xgey daxx')
server.send_message(msg)
server.quit()

userinput = input("enter otp : ")
if userinput == str(otp):
    print("otp validation is Successful !")
else :
    print("Wrong otp Entered")







