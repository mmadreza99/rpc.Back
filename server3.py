from gevent.server import StreamServer

from mprpc import RPCServer


class Server3(RPCServer):

    def Deferred_installment(self, code_mely, n_account):
        result = True
        return result


server = StreamServer(('127.0.0.1', 6002), Server3())
print('server3 is ready')
server.serve_forever()