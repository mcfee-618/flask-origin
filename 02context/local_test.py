import threading
from local import *


local = Local()

def run():
    global local
    print(threading.get_ident())
    local.acdd = 222


def test_local():
    global local
    local.ac = '333'
    print(type(local))
    th = threading.Thread(target=run)
    th.start()
    for items in local:
        print(items)


test_local()
