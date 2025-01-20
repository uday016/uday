import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import time
def send_mail(tomail,fname,lname,gender,dob,mobile):
    subject = "Hello From Codegnan"
    body = f"First Name: {fname}\nLast Name: {lname}\nGender: {gender} \nDate of Birth: {dob} \nMobile Number: {mobile}"
    msg = MIMEMultipart()
    msg['From'] = "anugulaudai@gmail.com "
    msg['To'] = tomail
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("anugulaudai@gmail.com","mykt ptui xgey daxx")
    server.send_message(msg)
    server.quit()
f = open("uday.txt","r")
data = f.read()
data1 = data.split("\n")
maindata = {}
temp = 1
resdata = {}
for i in data1:
    maindata[temp] = i.split(",")
    temp = temp + 1
fnamepattern = r'^[A-Za-z ]+$'
lnamepattern = r'^[A-Z]+$'
genderpattern = r'^(MALE|FEMALE)$'
dobpattern = r'^\d{2}-\d{2}-\d{4}$'
mobilepattern = r'^\d{10}$'
emailpattern = r'^.+@gmail.com$'
for x in maindata:
    resdata[x] = []
    text = maindata[x][0]
    matches = re.findall(fnamepattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)
    text = maindata[x][1]
    matches = re.findall(lnamepattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)
    text = maindata[x][2]
    matches = re.findall(mobilepattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)
    text = maindata[x][3]
    matches = re.findall(dobpattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)

    text = maindata[x][4]
    matches = re.findall(genderpattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)
    text = maindata[x][5]
    matches = re.findall(emailpattern,text)
    if len(matches) == 0:
        resdata[x].append(False)
    else:
        resdata[x].append(True)
print(resdata)
for val in resdata:
    if False in resdata[val]:
        print(f"Email not sent to {maindata[val][-1]}")
        s=open("uncorrect.txt","a")
        x=maindata[val]
        data=s.write(f'{x}\n')
        time.sleep(2)
    else:
        tomail = maindata[val][5]
        fname = maindata[val][0]
        lname = maindata[val][1]
        gender = maindata[val][4]
        dob = maindata[val][3]
        mobile = maindata[val][2]
        send_mail(tomail,fname,lname,gender,dob,mobile)
        print(f"Mail Sent to {tomail}")
