import re

from . import lib
from .constants import error


class PasswordValidator:
    ''' Class to generate schema of password definitions

    Example:
        >>> schema = PasswordValidator()
        >>> schema.has().letters().has().digits().no().spaces()
        <src.password_validator.password_validator.PasswordValidator object at ...>
        >>> schema.validate('testPassword123')
        True

    Returns:
        PasswordValidator: Schema object
    '''

    def __init__(self):
        self.properties = []
        self.positive = True


    def validate(self, pwd):
        ''' Validates `pwd` against the schema and returns the result

        Example:
            >>> PasswordValidator().letters().validate('123')
            False
            >>> PasswordValidator().letters().validate('abc')
            True

        Args:
            pwd (str): Password to validate against the schema
        Returns:
            boolean: Result of the validation
        '''

        password = str(pwd)
        return all(self.__isPasswordValidFor(prop, password) for prop in self.properties)

    def __registerProperty(self, func, args=[]):  # pylint: disable=dangerous-default-value
        self.properties.append({
            'method': func,
            'positive': self.positive,
            'arguments': args
        })

    def __isPasswordValidFor(self, prop, password):
        return prop['method'](password, prop['positive'], *prop['arguments'])

    def __validateNum(self, num):
        assert (type(num) == 'int' or num > 0), error['length'] # pylint: disable=unidiomatic-typecheck

    def has(self, regexp=None):
        ''' Inverts the effect of :func:`~no` and applies a :mod:`regex <python:re>` if provided
            to the schema. Works with:
            :func:`~letters`, :func:`~digits`, :func:`~uppercase`, :func:`~lowercase`,
            :func:`~symbols` and :func:`~spaces`.

        Example:
            >>> PasswordValidator().no().letters().has().digits().validate('123')
            True
            >>> PasswordValidator().has(r'[a-z]+').validate('test')
            True

        Args:
            regexp (str, optional): The regular expression or string to mandate on the password
        Returns:
            PasswordValidator: Updated schema object
        '''

        self.positive = True
        if regexp:
            self.__registerProperty(lib.applyRegexp, [re.compile(regexp)])
        return self

    def no(self, regexp=None):
        ''' Inverts the effect of all the next rules unless countered by a
            :func:`has` and applies a
            negative check of the regular expression provided. Works with:
            :func:`~letters`, :func:`~digits`, :func:`~uppercase`, :func:`~lowercase`,
            :func:`~symbols` and :func:`~spaces`.

        Example:
            >>> PasswordValidator().no().letters().digits().validate('123')
            False
            >>> PasswordValidator().no().letters().has().digits().validate('123')
            True
            >>> PasswordValidator().no(r'[a-z]+').validate('test')
            False

        Args:
            regexp (str, optional): The regex or str the password should not match to
        Returns:
            PasswordValidator: Updated schema object
        '''
        self.positive = not self.positive
        if regexp:
            self.__registerProperty(lib.applyRegexp, [re.compile(regexp)])
        return self

    def uppercase(self):
        ''' Mandates the presence/absense of uppercase letters.

        Example:
            >>> PasswordValidator().uppercase().validate('Test')
            True
            >>> PasswordValidator().uppercase().validate('test')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''
        self.__registerProperty(lib.uppercase)
        return self

    def lowercase(self):
        ''' Mandates the presence/absense of lowercase letters.

        Example:
            >>> PasswordValidator().lowercase().validate('Test')
            True
            >>> PasswordValidator().lowercase().validate('TEST')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''

        self.__registerProperty(lib.lowercase)
        return self

    def letters(self):
        ''' Mandates the presence/absense of letters.

        Example:
            >>> PasswordValidator().letters().validate('test')
            True
            >>> PasswordValidator().no().letters().validate('test')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''

        self.__registerProperty(lib.letters)
        return self

    def digits(self):
        ''' Mandates the presence/absense of digits.

        Example:
            >>> PasswordValidator().digits().validate('test')
            False
            >>> PasswordValidator().no().digits().validate('test123')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''

        self.__registerProperty(lib.digits)
        return self

    def min(self, length):
        ''' Sets the minimum length allowed.

        Example:
            >>> PasswordValidator().min(8).validate('testPassword')
            True
            >>> PasswordValidator().min(8).validate('test')
            False

        Args:
            length (int): Minimum length allowed
        Returns:
            PasswordValidator: Updated schema object
        '''

        self.__validateNum(length)
        self.__registerProperty(lib.minimum, [length])
        return self

    def max(self, length):
        ''' Sets the maximum length allowed.

        Example:
            >>> PasswordValidator().max(8).validate('testPassword')
            False
            >>> PasswordValidator().max(8).validate('test')
            True

        Args:
            length (int): Maximum length allowed
        Returns:
            PasswordValidator: Updated schema object
        '''
        self.__validateNum(length)
        self.__registerProperty(lib.maximum, [length])
        return self

    def spaces(self):
        ''' Mandates the presence/absense of whitespace.

        Example:
            >>> PasswordValidator().spaces().validate('a  bc')
            True
            >>> PasswordValidator().no().spaces().validate('a  bc')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''
        self.__registerProperty(lib.spaces)
        return self

    def symbols(self):
        ''' Mandates the presence/absense of special characters like `@`, `#`, `$`, etc.

        Example:
            >>> PasswordValidator().symbols().validate('@bc')
            True
            >>> PasswordValidator().no().symbols().validate('@bc')
            False

        Returns:
            PasswordValidator: Updated schema object
        '''
        self.__registerProperty(lib.symbols)
        return self
