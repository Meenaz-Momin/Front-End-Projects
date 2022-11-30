# import smtplib

# with smtplib.SMTP('smtp.gmail.com",587') as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     sender = "momin.meenaz29@gmail.com"
#     password = ""
#     receiver = "meenazm61@gmail.com"
#     smtp.login(sender, password)
#     subject = "HRMS-360 Automatic Testing"
#     message = f"subject:{subject}\n"
#     smtp.sendmail(sender, receiver, message)
#     print("Email Sent")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


mail_host = "smtp.gmail.com"
mail_user = "testing"
mail_pass = "testing"

sender = 'momin.meenaz29@gmail.com'
receivers = ['meenazm61@gmail.com']

message = MIMEMultipart()
message['From'] = Header("Hello2", 'utf-8')
message['To'] = Header("World2", 'utf-8')

subject = 'Python SMTP Testing'
message['Subject'] = Header(subject, 'utf-8')

att1 = MIMEText(open('/home/fladdra/Desktop/Meenaz/Testing/Selenium Zunoks-360-Feedback/reports/',
                'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'

att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('Sent...')
except:
    print('Error: ')
