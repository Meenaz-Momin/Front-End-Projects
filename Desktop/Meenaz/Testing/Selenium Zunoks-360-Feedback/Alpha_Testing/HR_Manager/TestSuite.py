import unittest
from Login import LOGIN
from Competency import COMPETENCY
from Questions import QUESTIONS
from Employee import EMPLOYEE
from StandardResponse import STANDARDRESPONSE
from AssessmentArea import ASSESSMENTAREA
from Department import DEPARTMENT
from Designation import DESIGNATION
from Raters import RATERS

login = unittest.TestLoader().loadTestsFromTestCase(LOGIN)
competency = unittest.TestLoader().loadTestsFromTestCase(COMPETENCY)
questions = unittest.TestLoader().loadTestsFromTestCase(QUESTIONS)
employee = unittest.TestLoader().loadTestsFromTestCase(EMPLOYEE)
standard_response = unittest.TestLoader().loadTestsFromTestCase(STANDARDRESPONSE)
assessment_area = unittest.TestLoader().loadTestsFromTestCase(ASSESSMENTAREA)
department = unittest.TestLoader().loadTestsFromTestCase(DEPARTMENT)
designation = unittest.TestLoader().loadTestsFromTestCase(DESIGNATION)
raters = unittest.TestLoader().loadTestsFromTestCase(RATERS)

test_suite = unittest.TestSuite([login, competency, questions, employee,
                                standard_response, assessment_area, department, designation, raters])

unittest.TextTestRunner(verbosity=2).run(test_suite)
