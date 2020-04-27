import unittest;
from Register import Register;

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.user = {
            'username': 'Testing',
            'email': 'testing@gmail.com',
            'password': '12345678'
        }

    def tearDown(self):
        self.args = None

    def test_register(self):
        expected = "Registration successful."
        result = Register().start(self.user)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()