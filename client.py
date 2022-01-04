from mprpc import RPCClient


def call():
    client = RPCClient('127.0.0.1', 6000)
    print(client.call('server1', 410669237, 3000698778))


call()
