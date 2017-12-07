import unittest
import MentorLogin
import testAdminLogin
import CreateEmployee
import DeleteEmployee
import Studentadd
import StudentReport
import StudentSearch
import Mentor_Edit
import Archive_test
import addMentor


# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(MentorLogin))
suite.addTests(loader.loadTestsFromModule(testAdminLogin))
suite.addTests(loader.loadTestsFromModule(CreateEmployee))
suite.addTests(loader.loadTestsFromModule(DeleteEmployee))
suite.addTests(loader.loadTestsFromModule(StudentReport))
suite.addTests(loader.loadTestsFromModule(StudentSearch))
suite.addTests(loader.loadTestsFromModule(Studentadd))
suite.addTests(loader.loadTestsFromModule(Mentor_Edit))
suite.addTests(loader.loadTestsFromModule(Archive_test))
suite.addTests(loader.loadTestsFromModule(addMentor))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)