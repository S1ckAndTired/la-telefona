from target import target
from cookies import cookie

def proxy():
    if target.var != "":
        proxies = input("Wanna set proxies? Y-N: ")
        if proxies == "y":
            proxy.var = {'https': 'https://127.0.0.1:8080'}
        else:
            proxy.var = {'https': None}
            print("\n      ***Proceeding without proxies***")

