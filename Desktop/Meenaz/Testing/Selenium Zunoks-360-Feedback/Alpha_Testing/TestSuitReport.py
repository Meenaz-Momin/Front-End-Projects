import unittest
import HtmlTestRunner
import os
from HR_Manager.Login import LOGIN
from HR_Manager.Competency import COMPETENCY
from HR_Manager.Questions import QUESTIONS
from HR_Manager.Employee import EMPLOYEE
from HR_Manager.StandardResponse import STANDARDRESPONSE
from HR_Manager.AssessmentArea import ASSESSMENTAREA
from HR_Manager.Department import DEPARTMENT
from HR_Manager.Designation import DESIGNATION
from HR_Manager.Raters import RATERS
from System_Admin.Login import LOGIN_ADMIN
from System_Admin.Competency import COMPETENCY_ADMIN
from System_Admin.Questions import QUESTIONS_ADMIN
from System_Admin.Tenant import TENANT
from System_Admin.Users import USERS
from System_Admin.AssessedArea import ASSESSMENTAREA_ADMIN
from System_Admin.Industry import INDUSTRY
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time

login = unittest.TestLoader().loadTestsFromTestCase(LOGIN)
competency = unittest.TestLoader().loadTestsFromTestCase(COMPETENCY)
questions = unittest.TestLoader().loadTestsFromTestCase(QUESTIONS)
employee = unittest.TestLoader().loadTestsFromTestCase(EMPLOYEE)
standard_response = unittest.TestLoader().loadTestsFromTestCase(STANDARDRESPONSE)
assessment_area = unittest.TestLoader().loadTestsFromTestCase(ASSESSMENTAREA)
department = unittest.TestLoader().loadTestsFromTestCase(DEPARTMENT)
designation = unittest.TestLoader().loadTestsFromTestCase(DESIGNATION)
raters = unittest.TestLoader().loadTestsFromTestCase(RATERS)

login_admin = unittest.TestLoader().loadTestsFromTestCase(LOGIN_ADMIN)
competency_admin = unittest.TestLoader().loadTestsFromTestCase(COMPETENCY_ADMIN)
questions_admin = unittest.TestLoader().loadTestsFromTestCase(QUESTIONS_ADMIN)
tenant = unittest.TestLoader().loadTestsFromTestCase(TENANT)
users = unittest.TestLoader().loadTestsFromTestCase(USERS)
areaAssessment_admin = unittest.TestLoader(
).loadTestsFromTestCase(ASSESSMENTAREA_ADMIN)
industry = unittest.TestLoader().loadTestsFromTestCase(INDUSTRY)

# test_suite1 = unittest.TestSuite([login])
test_suite1 = unittest.TestSuite([login, competency, questions, employee,
                                  standard_response, assessment_area, department, designation, raters])

test_suite2 = unittest.TestSuite(
    [login_admin, competency_admin, questions_admin, tenant, users, areaAssessment_admin, industry])

outfile = open("SeleniumPythonTestSummary.html", "w")

runner = HtmlTestRunner.HTMLTestRunner(
    stream=outfile, descriptions="Alpha Testing")

# unittest.TextTestRunner(verbosity=2).run(test_suite)

folder = "/home/fladdra/Desktop/Meenaz/Testing/Selenium Zunoks-360-Feedback/Alpha_Testing/reports//"
for file_name in os.listdir(folder):
    source = folder + file_name
    if os.path.isfile(source):
        os.remove(source)

runner.run(test_suite1)
time.sleep(10)
runner.run(test_suite2)

list_of_files = []
folder = "/home/fladdra/Desktop/Meenaz/Testing/Selenium Zunoks-360-Feedback/Alpha_Testing/reports//"
for file_name in os.listdir(folder):
    source = folder + file_name
    if os.path.isfile(source):
        list_of_files.append(source)

sender = "meenaz.riyaz@apsissolutions.com"
receiver = ["meenaz.riyaz@apsissolutions.com", "amaan.khan@apsissolutions.com"]
for to in receiver:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = to
    msg['Subject'] = "HRMS-360 Alpha Testing"
    body = "Alpha Testing : HR Manager Dashboard/Login Module"
    msg.attach(MIMEText(body, 'plain'))
    filename = "report.html"
    for f in list_of_files:  # add files to the message
        file_path = os.path.join(f)
        attachment = MIMEApplication(
            open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header(
            'Content-Disposition', 'attachment', filename=os.path.splitext(f)[0])
        msg.attach(attachment)
    s = smtplib.SMTP('smtp.outlook.com', 587)
    s.starttls()
    s.login(sender, "Zunoks@360")
    text = msg.as_string()
    s.sendmail(sender, to, text)
    print("Email sent")
    s.quit()
