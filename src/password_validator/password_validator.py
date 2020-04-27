
import re

from . import lib
from .constants import error


class PasswordValidator:

    def __init__(self):
        self.properties = []
        self.positive = True

    def validate(self, pwd):
        password = str(pwd)
        return all(self.__isPasswordValidFor(prop, password) for prop in self.properties)

    def __registerProperty(self, func, args=[]):
        self.properties.append({
            'method': func,
            'positive': self.positive,
            'arguments': args
        })

    def __isPasswordValidFor(self, prop, password):
        return prop['method'](password, prop['positive'], *prop['arguments'])

    def __validateNum(self, num):
        assert (type(num) == 'int' or num > 0), error['length']

    def has(self, regexp=None):
        self.positive = True
        if regexp:
            self.__registerProperty(lib.applyRegexp, [re.compile(regexp)])
        return self

    def no(self, regexp=None):
        self.positive = not self.positive
        if regexp:
            self.__registerProperty(lib.applyRegexp, [re.compile(regexp)])
        return self

    def uppercase(self):
        self.__registerProperty(lib.uppercase)
        return self

    def lowercase(self):
        self.__registerProperty(lib.lowercase)
        return self

    def letters(self):
        self.__registerProperty(lib.letters)
        return self

    def digits(self):
        self.__registerProperty(lib.digits)
        return self

    def min(self, length):
        self.__validateNum(length)
        self.__registerProperty(lib.minimum, [length])
        return self

    def max(self, length):
        self.__validateNum(length)
        self.__registerProperty(lib.maximum, [length])
        return self

    def spaces(self):
        self.__registerProperty(lib.spaces)
        return self

    def symbols(self):
        self.__registerProperty(lib.symbols)
        return self


schema = PasswordValidator()
schema.has().letters()
schema.validate('DDD4$')
schema.validate('4$')