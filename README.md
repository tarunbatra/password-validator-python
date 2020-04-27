# password-validator

This is a python port of `npm` package [password-validator](https://github.com/tarunbatra/password-validator)

## Install
`pip install password-validator`

## Usage
```py
from password_validator import PasswordValidator

# Create a schema
schema = PasswordValidator()

# Add properties to it
schema\
.min(8)\
.max(100)\
.has().uppercase()\
.has().lowercase()\
.has().digits()\
.has().no().spaces()\

# Validate against a password string
print(schema.validate('validPASS123'));
# => True
print(schema.validate('invalidPASS'));
# => False
```

## Rules
Rules supported as of now are:

|     Rules      |               Descriptions                                       |
|:---------------|:-----------------------------------------------------------------|
|**digits()**    | specifies password must include digits                           |
|**letters()**   | specifies password must include letters                          |
|**lowercase()** | specifies password must include lowercase letters                |
|**uppercase()** | specifies password must include uppercase letters                |
|**symbols()**   | specifies password must include symbols                          |
|**spaces()**    | specifies password must include spaces                           |
|**min(len)**    | specifies minimum length                                         |
|**max(len)**    | specifies maximum length                                         |
|**no([regex])**| inverts the result of validations applied next                    |
|**has([regex])**| inverts the effect of _**no()**_ and applies a regex (optional)  |

## License
[MIT License](https://choosealicense.com/licenses/mit/)
