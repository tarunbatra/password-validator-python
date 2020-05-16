| |logo|

| |pypi version| |build| |coverage| |format| |status| |python version|

password_validator
==================

This is a python port of ``npm`` package
`password-validator <https://github.com/tarunbatra/password-validator>`__.

Install
-------

``pip install password-validator``

Usage
-----

.. code:: py

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

Rules
-----

Rules supported as of now are:

+--------------------+-------------------------------------------------------------------+
| Rules              | Descriptions                                                      |
+====================+===================================================================+
| **digits()**       | specifies password must include digits                            |
+--------------------+-------------------------------------------------------------------+
| **letters()**      | specifies password must include letters                           |
+--------------------+-------------------------------------------------------------------+
| **lowercase()**    | specifies password must include lowercase letters                 |
+--------------------+-------------------------------------------------------------------+
| **uppercase()**    | specifies password must include uppercase letters                 |
+--------------------+-------------------------------------------------------------------+
| **symbols()**      | specifies password must include symbols                           |
+--------------------+-------------------------------------------------------------------+
| **spaces()**       | specifies password must include spaces                            |
+--------------------+-------------------------------------------------------------------+
| **min(len)**       | specifies minimum length                                          |
+--------------------+-------------------------------------------------------------------+
| **max(len)**       | specifies maximum length                                          |
+--------------------+-------------------------------------------------------------------+
| **no([regex])**    | inverts the result of validations applied next                    |
+--------------------+-------------------------------------------------------------------+
| **has([regex])**   | inverts the effect of **no()** and applies a regex (optional)     |
+--------------------+-------------------------------------------------------------------+

License
-------

`MIT License <https://choosealicense.com/licenses/mit/>`__

.. |pypi version| image:: https://img.shields.io/pypi/v/password-validator?color=blue&logo=password_validator&style=flat-square
   :target: https://pypi.org/project/password-validator
.. |python version| image:: https://img.shields.io/pypi/pyversions/password-validator?color=red&logo=version&style=flat-square
.. |format| image:: https://img.shields.io/pypi/format/password-validator?color=orange&style=flat-square
.. |status| image:: https://img.shields.io/pypi/status/password-validator?logo=status&style=flat-square
.. |logo| image:: https://res.cloudinary.com/tbking/image/upload/v1490803400/password-validator/logo.png
.. |build| image:: https://img.shields.io/github/workflow/status/tarunbatra/password-validator-python/CI?logo=github&style=flat-square
    :target: https://github.com/tarunbatra/password-validator-python/actions?query=workflow%3ACI
.. |coverage| image:: https://img.shields.io/codecov/c/gh/tarunbatra/password-validator-python?logo=codecov&style=flat-square
    :target: https://codecov.io/gh/tarunbatra/password-validator-python