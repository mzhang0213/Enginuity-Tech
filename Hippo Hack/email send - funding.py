#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE


#BEFORE SENDING, DO A) A TEST WITH MZ DIDI ACC B) HIGHLIGHT sendData.txt INSPECT FOR WHITE SPACES AND ANYTHING WEIRD OTHER THAN \t STUFF




import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime, time, sys

def send_email(subject, body, sender, recipient, password, name):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    for i in name:
        attachment = open(i, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        ind=0
        for j in range(len(i)-1,0,-1):
            if i[j]=='/':
                ind=len(i)-(j+1)
                break        
        p.add_header('Content-Disposition', "attachment", filename=i[-ind:])
        msg.attach(p)
    context = ssl.create_default_context()
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender,password)
    session.sendmail(sender,recipient,msg.as_string())
    session.quit()



#format of rawData
#  recipient's name (teacher / first name) \t recipient's school \t recipient's club \t recipient email \n ...



rawData = open("C:/Users/Michael Zhang/Desktop/Enginuity-Tech/Hippo Hack/sendData - funding.txt","r").readlines()
for i in range(len(rawData)):
    if rawData[i][-1:]=="\n":
        rawData[i]=rawData[i][:-1]
    rawData[i]=rawData[i].split("\t")
subject = "Hippo Hack Sponsorship Inquiry! TESTING TESTING TESTING"
sender = "enginuitytech@gmail.com"
password = "rysemsfrldxnhder" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is rysemsfrldxnhder


#get date want to send
mm=input("input month you want to send:\n")
if mm=="":mm=datetime.datetime.now().strftime("%m")
dd=input("input day you want to send:\n")
if dd=="":dd=datetime.datetime.now().strftime("%d")
yy=datetime.datetime.now().strftime("%Y")
mins=input("input @ what min you want to send:\n")
secs=input("input @ what sec you want to send:\n")

sendDate = datetime.datetime(int(yy),int(mm),int(dd),int(mins),int(secs))
finalConfirm=input("\nschedule sending for "+sendDate.strftime("%c")+". ABORT TYPE IN \"N\"\n")
if finalConfirm=="N":
    print("abort mission")
    sys.exit()


#confirm email msgs
body=""
names=["C:/Users/Michael Zhang/Desktop/Enginuity-Tech/Hippo Hack/Hippo Hack Prospectus.pdf"] #file names of all attachments, on this drive

print("reviewing messages, starting on following line:\n\n")
for i in range(len(rawData)):
    
    body = (
    	"Hi "+rawData[i][0]+","
        +"\n\nMy name is Michael, and I am a junior at the Acton-Boxborough Regional High School. I am a founder of Enginuity Tech, a nonprofit organization that offers "
        +"students free STEM classes and organizes local hackathons in the Massachusetts area for all students of any programming expertise. "
        +"This year we are hosting Hippo Hack, a free, in-person hackathon hosted here in Massachusetts for all students in grades 6-12 "
        +"interested in computer science. Students will work in groups and broaden their skills while employing their creativity to "
        +"create a one-of-a-kind project! We are interested in whether you could help sponsor us for this year’s Hippo Hack as well a "
        +"many other tech-related events in the future! For additional details regarding sponsorship, refer to the attached prospectus."
        
        +"\n\nYour help would be greatly appreciated."
        
        +"\n\nSincerely,"
        +"\nMichael Zhang"
    )
    
    print(body)
    print()
    finalconfirmation=input("DO YOU ACTUALLY WANT TO SEND, N TO DECLINE (any key accept)\n")
    if finalconfirmation=="N":
        print("abort mission")
        sys.exit()


#delay
print("delaying, ctrl c if want to stop")
time.sleep(sendDate.timestamp()-time.time())


#send emails
print("ok ready to go, sending in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("sending in process...")

for i in range(len(rawData)):
    
    body = (
    	"Hi "+rawData[i][0]+","
        +"\n\nMy name is Michael, and I am a junior at the Acton-Boxborough Regional High School. I am a founder of Enginuity Tech, a nonprofit organization that offers "
        +"students free STEM classes and organizes local hackathons in the Massachusetts area for all students of any programming expertise. "
        +"This year we are hosting Hippo Hack, a free, in-person hackathon hosted here in Massachusetts for all students in grades 6-12 "
        +"interested in computer science. Students will work in groups and broaden their skills while employing their creativity to "
        +"create a one-of-a-kind project! We are interested in whether you could help sponsor us for this year’s Hippo Hack as well a "
        +"many other tech-related events in the future! For additional details regarding sponsorship, refer to the attached prospectus."
        
        +"\n\nYour help would be greatly appreciated."
        
        +"\n\nSincerely,"
        +"\nMichael Zhang"
    )
    
    recipient = rawData[i][1]
    send_email(subject, body, sender, recipient, password, names)
print("finished sending :)")

#confirmation
body="SENT EMAIL ON '" + sendDate.strftime("%c") + "'\nheres the last (sample) message:\n\n--------------------------------------------------\n\n"+body
send_email("confirmation sent "+len(rawData)+"emails | "+subject, body, sender, "24zhangm@abschools.org", password, names)