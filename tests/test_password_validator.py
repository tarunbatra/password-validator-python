import unittest
from password_validator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.schema = PasswordValidator()

    def test_validate(self):
        res = self.schema.min(8).validate('pwd')
        self.assertFalse(res, 'should return Boolean')

    def test_min(self):
        self.assertFalse(self.schema.min(8).validate(
            'pwd'), 'should return False is pwd is less than the length specified')
        self.assertTrue(self.schema.min(8).validate(
            'longPassword'), 'should return True is pwd is greater than the length specified')
        self.assertTrue(self.schema.min(8).validate(
            '12345678'), 'should return True is pwd is equal to the length specified')

    def test_max(self):
        self.assertTrue(self.schema.max(8).validate(
            'pwd'), 'should return True is pwd is less than the length specified')
        self.assertFalse(self.schema.max(8).validate(
            'longPassword'), 'should return False is pwd is greater than the length specified')
        self.assertTrue(self.schema.max(8).validate(
            '12345678'), 'should return True is pwd is equal to the length specified')

    def test_letters(self):
        self.assertTrue(self.schema.letters().validate(
            'pwd1234'), 'should return True is pwd has letters')
        self.assertFalse(self.schema.letters().validate(
            '1234'), 'should return False is pwd doesn\'t have letters')

    def test_digits(self):
        self.assertTrue(self.schema.digits().validate(
            'pwd1234'), 'should return True is pwd has digits')
        self.assertFalse(self.schema.digits().validate(
            'pwd'), 'should return False is pwd doesn\'t have digits')

    def test_symbols(self):
        self.assertTrue(self.schema.symbols().validate(
            'pwd$'), 'should return True is pwd has symbols')
        self.assertFalse(self.schema.symbols().validate(
            'pwd'), 'should return False is pwd doesn\'t have symbols')

    def test_spaces(self):
        self.assertTrue(self.schema.spaces().validate(
            'pwd 1234'), 'should return True is pwd has spaces')
        self.assertFalse(self.schema.spaces().validate(
            'pwd1234'), 'should return False is pwd doesn\'t have spaces')

    def test_uppercase(self):
        self.assertTrue(self.schema.uppercase().validate(
            'pWD1234'), 'should return True is pwd has uppercase letters')
        self.assertFalse(self.schema.uppercase().validate(
            'pwd1234'), 'should return False is pwd doesn\'t have uppercase letters')

    def test_lowercase(self):
        self.assertTrue(self.schema.lowercase().validate(
            'pWD1234'), 'should return True is pwd has lowercase letters')
        self.assertFalse(self.schema.lowercase().validate(
            'PWD1234'), 'should return False is pwd doesn\'t have lowercase letters')

    def test_has(self):
        self.assertTrue(self.schema.has().lowercase().validate(
            'pWD1234'), 'should return cause no difference if used without args')

    def test_has_with_string(self):
        self.assertTrue(self.schema.has('1234').validate(
            'pwd1234'), 'should return True if the pwd matches the regex passed in arg')
        self.assertFalse(self.schema.has('12345').validate(
            'pwd1234'), 'should return False if the pwd matches the regex passed in arg')

    def test_has_with_regex(self):
        self.assertTrue(self.schema.has(r'^p1').validate(
            'p1234'), 'should return True if the pwd matches the regex passed in arg')
        self.assertFalse(self.schema.has(r'12345$').validate(
            'p1234'), 'should return False if the pwd matches the regex passed in arg')

    def test_no(self):
        self.assertTrue(self.schema.no().lowercase().validate(
            'PWD1234'), 'should return cause no difference if used without args')

    def test_no_with_string(self):
        self.assertFalse(self.schema.no('1234').validate(
            'pwd1234'), 'should return False if the pwd has string passed in arg')

    def test_no_with_regex(self):
        self.assertTrue(self.schema.no(r'^12345$').validate(
            'p1234'), 'should return True if the pwd matches the regex passed in arg')


if __name__ == '__main__':
    unittest.main()
