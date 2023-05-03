

#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE



#REMOVE THE TESTING MESSAGE IN SUBJECT LINE






import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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
    print("Message starting on following line:\n")
    print(body)
    print()
    finalconfirmation=input("DO YOU ACTUALLY WANT TO SEND, N TO DECLINE (any key accept)\n")
    if finalconfirmation!="N":
        session.sendmail(sender,recipient,msg.as_string())
    session.quit()

'''

test test test


subject = "Hippo Hack - hackathon for your students!1"
sender = "mzhang0213@gmail.com"
body="HIIIIIIII"
password = "nyttoksinrsxpubl" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is rysemsfrldxnhder
recipient = "mzhang0213@gmail.com"
arrg=["C:/Users/Michael Zhang/Desktop/pooped on p2.png","C:/Users/Michael Zhang/Desktop/CorpSearchView.pdf"]
send_email(subject, body, sender, recipient, password, arrg)

'''

#format of rawData
#  recipient's name (teacher / first name) \t recipient's school \t recipient's club \t recipient email \n ...


rawData = open("C:/Users/Michael Zhang/Desktop/sendData.txt","r").readlines()
for i in range(len(rawData)):
    if rawData[i][-1:]=="\n":
        rawData[i]=rawData[i][:-1]
    rawData[i]=rawData[i].split("\t")
subject = "Hippo Hack - hackathon for your students! TESTING TESTING TESTING"
sender = "enginuitytech@gmail.com"
password = "rysemsfrldxnhder" #generated "App Password" from myaccount.google.com/apppasswords
#michael's password is nyttoksinrsxpubl
#enginuity's password is rysemsfrldxnhder

for i in range(len(rawData)):
    
    body = (
    	"Hi "+rawData[i][0]+","
    	+"\n\nMy name is Michael and I am a junior at the Acton-Boxborough Regional High School. "
        +"I am a part of Enginuity Tech, a nonprofit organization, and we are hosting the Hippo Hack! "
    	+"Would you help me pass along the following information along with the flyer to your students in your "+rawData[i][2]+"?"
     #info
    	+"\n\n\nHippo Hack is a free, in-person hackathon hosted here in Massachusetts for all students in grades 6-12 who have "
        +"interest in computer science and want to show their creativity and learn more in computer science. "
        +"If you are interested in participating, please check out their website at enginuitytech.org/hippohack"
		+"\n\nThanks so much for your help!"
		+"\nMichael Zhang"
    )
    
    recipient = rawData[i][3]
    names=["C:/Users/Michael Zhang/Desktop/hippoHackFlyer draft.pdf"] #file names of all attachments, on this drive
    send_email(subject, body, sender, recipient, password, names)
