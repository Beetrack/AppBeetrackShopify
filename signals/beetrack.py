import ipdb

def after_commit(session):
    ipdb.set_trace()
    print(session)