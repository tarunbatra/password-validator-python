import unittest
import doctest
from src.password_validator import password_validator

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(password_validator, optionflags=doctest.ELLIPSIS))
    return tests