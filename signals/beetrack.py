import ipdb
from flask import session

def before_commit(object):
    ipdb.set_trace()
    shop = session["shop"]
    print(object)