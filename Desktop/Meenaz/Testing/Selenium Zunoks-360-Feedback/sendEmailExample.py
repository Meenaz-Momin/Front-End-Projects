# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender = "momin.meenaz29@gmail.com"
receiver = ["meenaz.riyaz@apsissolutions.com", "amaan.khan@apsissolutions.com"]
for to in receiver:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = "HRMS-360 Alpha Testing"
    body = "Alpha Testing : HR Manager Dashboard/Login Module"
    msg.attach(MIMEText(body, 'plain'))
    filename = "report.html"
    attachment = open(
        "/home/fladdra/Desktop/Meenaz/Testing/Selenium Zunoks-360-Feedback/reports/*", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, "nxzjuoccxvzwrwec")
    text = msg.as_string()
    s.sendmail(sender, to, text)
    print("Email sent")
    s.quit()
