from gevent.server import StreamServer
from mprpc import RPCServer


class Server2(RPCServer):

    def Bankـreturnـcheck(self, code_mely, n_account):
        result = False
        return result


server = StreamServer(('127.0.0.1', 6001), Server2())
print('server2 is ready')
server.serve_forever()