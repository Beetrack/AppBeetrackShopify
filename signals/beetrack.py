import ipdb

def before_commit(session):
    ipdb.set_trace()
    print("Hola")
    print(session)