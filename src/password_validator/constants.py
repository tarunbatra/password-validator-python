import re

error = {
    'length': 'Length should be a valid positive number',
    'password': 'Password should be a valid string'
}

regex = {
    'digits': re.compile(r'\d+'),
    'letters': re.compile(r'[a-zA-Z]+'),
    'symbols': re.compile(r'[`~\!@#\$%\^\&\*\(\)\-_\=\+\[\{\}\]\\\|;\:\'",<.>\/\?\€\£\¥\₹]+'),
    'spaces': re.compile(r'[\s]+')
}
