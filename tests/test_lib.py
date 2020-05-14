import unittest
from password_validator import lib

class TestLib(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(lib.minimum('TestPass', True, 8), True, 'should return True if pwd length is 8')
        self.assertEqual(lib.minimum('TestPasss', True, 8), True, 'should return True if pwd length is > 8')
        self.assertEqual(lib.minimum('TestPas', True, 8), False, 'should return False if pwd length is < 8')

    def test_maximum(self):
        self.assertEqual(lib.maximum('TestPass', True, 8), True, 'should return True if pwd length is > 8')
        self.assertEqual(lib.maximum('TestPasss', True, 8), False, 'should return False if pwd length is > 8')
        self.assertEqual(lib.maximum('TestPas', True, 8), True, 'should return True if pwd length is > 8')

    def test_letters(self):
        self.assertEqual(lib.letters('qwerTy', True), True, 'should return True if pwd has letters')
        self.assertEqual(lib.letters('qwe123', True), True, 'should return True if pwd has letters and digits')
        self.assertEqual(lib.letters('12344', True), False, 'should return False if pwd doesn\'t have letters')

        self.assertEqual(lib.letters('qwerTy', False), False, 'should return False if pwd has letters and check is negative')
        self.assertEqual(lib.letters('qwe123', False), False, 'should return False  if pwd has letters and digits, and check is negative')
        self.assertEqual(lib.letters('12344', False), True, 'should return True if pwd doesn\'t have letters and check is negative')

    def test_digits(self):
        self.assertEqual(lib.digits('12344', True), True, 'should return True if pwd has digits')
        self.assertEqual(lib.digits('qwe123', True), True, 'should return True if pwd has digits and letters')
        self.assertEqual(lib.digits('qwerTy', True), False, 'should return False if pwd doesn\'t have digits')

        self.assertEqual(lib.digits('12344', False), False, 'should return False if pwd has digits and the check is negative')
        self.assertEqual(lib.digits('qwe123', False), False, 'should return False if pwd has digits and letters, and the check is negative')
        self.assertEqual(lib.digits('qwerTy', False), True, 'should return True if pwd doesn\'t have digits and the check is negative')

    def test_symbols(self):
        self.assertEqual(lib.symbols('qwe$u', True), True, 'should return True if pwd has symbols')
        self.assertEqual(lib.symbols('qwe£u', True), True, 'should return True if pwd has non-USD currency symbols')
        self.assertEqual(lib.symbols('qweu', True), False, 'should return False if pwd doesn\'t have symbols')

        self.assertEqual(lib.symbols('qwe$u', False), False, 'should return False if pwd has symbols and check is negative')
        self.assertEqual(lib.symbols('qwe£u', False), False, 'should return False if pwd has non-USD currency symbols and check is negative')
        self.assertEqual(lib.symbols('qweu', False), True, 'should return True if pwd doesn\'t have symbols and check is negative')


    def test_spaces(self):
        self.assertEqual(lib.spaces('word1 word2', True), True, 'should return True if pwd has spaces')
        self.assertEqual(lib.spaces('word', True), False, 'should return False if pwd has no space')

        self.assertEqual(lib.spaces('word1 word2', False), False, 'should return False if pwd has spaces and check is negative')
        self.assertEqual(lib.spaces('word', False), True, 'should return True if pwd has no space and check is negative')

    def test_uppercase(self):
        self.assertEqual(lib.uppercase('upperCase', True), True, 'should return True if pwd has uppercase letters')
        self.assertEqual(lib.uppercase('lowercase', True), False, 'should return False if pwd has no uppercase letters')

        self.assertEqual(lib.uppercase('uppserCase', False), False, 'should return False if pwd has uppercase letters and check is negative')
        self.assertEqual(lib.uppercase('lowercase', False), True, 'should return True if pwd has no uppercase letters and check is negative')

    def test_lowercase(self):
        self.assertEqual(lib.lowercase('lowerCase', True), True, 'should return True if pwd has lowercase letters')
        self.assertEqual(lib.lowercase('UPPERCASE', True), False, 'should return False if pwd has no lowercase letters')

        self.assertEqual(lib.lowercase('lowerCase', False), False, 'should return False if pwd has lowercase letters and check is negative')
        self.assertEqual(lib.lowercase('UPPERCASE', False), True, 'should return True if pwd has no lowercase letters and check is negative')

    def test_applyRegexp(self):
        self.assertEqual(lib.applyRegexp('somePassword123', True, r'^[a-zA-Z]+\d{3}'), True, 'should return True if pwd has matches regex')
        self.assertEqual(lib.applyRegexp('somePassword123', True, r'^[a-zA-Z]+\d{4}'), False, 'should return False if pwd doesn\'t match regex')

        self.assertEqual(lib.applyRegexp('somePassword123', False, r'^[a-zA-Z]+\d{3}'), False, 'should return False if pwd has matches regex and check is negative')
        self.assertEqual(lib.applyRegexp('somePassword123', False, r'^[a-zA-Z]+\d{4}'), True, 'should return True if pwd doesn\'t match regex and check is negative')

if __name__ == '__main__':
    unittest.main()
