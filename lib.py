from constants import regex, error
import re

def _process(password, positive, regexp):
    return bool(re.search(regexp, password)) == bool(positive)


def has(password, positive, symbol):
    return _process(password, positive, re.compile(symbol))

def no(password, positive, symbol):
    return _process(password, positive, re.compile(symbol))

def min(password, length):
    return password.length >= length

def max(password, length):
    return password.length <= length

def letters(password, positive):
    return _process(password, positive, regex['letters'])

def digits(password, positive):
    return _process(password, positive, regex['digits'])

def symbols(password, positive):
    return _process(password, positive, regex['symbols'])

def spaces(password, positive):
    return _process(password, positive, regex['spaces'])

def uppercase(password, positive):
    return (password != password.lower()) == positive

def lowercase(password, positive):
    return (password != password.upper()) == positive
