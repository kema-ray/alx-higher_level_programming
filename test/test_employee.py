import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Smith', 50000)
        self.emp_2 = Employee('Rachel', 'Oyondi', 60000)

    def tearDown(self):
        print('teardown\n')

    def test_email(self):
        print('test_email')
        # emp_1 = Employee('Corey', 'Smith', 50000)
        # emp_2 = Employee('Rachel', 'Oyondi', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Rachel.Oyondi@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Smith@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Oyondi@email.com')

    def test_fullname(self):
        print('test fullname')
        # emp_1 = Employee('Corey', 'Smith', 50000)
        # emp_2 = Employee('Rachel', 'Oyondi', 60000)

        self.assertEqual(self.emp_1.fullname, 'Corey Smith')
        self.assertEqual(self.emp_2.fullname, 'Rachel Oyondi')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Oyondi')

    def test_apply_raise(self):
        print('test apply_raise')
        # emp_1 = Employee('Corey', 'Smith', 50000)
        # emp_2 = Employee('Rachel', 'Oyondi', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Oyondi/June')
            self.assertEqual(schedule, 'Bad Response!')
