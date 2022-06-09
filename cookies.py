from target import target
import requests

def cookie():
    session = requests.Session()
    response = session.get(target.var)
    cookie.var = response.cookies.get_dict()

