# 2 types of Modules: Built-in and External Modules
# - Built in Modules: https://docs.python.org/3/py-modindex.html

import math
import os   # color of os is blurred because i have only imported this module and didnt use in vs code.


print(math.sqrt(16)) # sqrt is a function in math module

# create your own module  mymodule.py

import mymodule
mymodule.abc()

# External Modules : can be installed using pip utility
# pip install requests and then
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

# https://pypi.org/project/requests/
# https://docs.python.org/3/library/http.html





