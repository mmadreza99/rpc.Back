from mprpc import RPCClient


def call():
    client = RPCClient('127.0.0.1', 6000)
    result = client.call('borrow', 410669237, 3000698778)
    print(result)


call()
