from gevent.server import StreamServer

from mprpc import RPCServer, RPCClient


class BorrowServer(RPCServer):

    def server1(self, code_mely, n_account):
        s2 = self.server2(code_mely, n_account)
        s3 = self.server3(code_mely, n_account)
        return bool(s2 == s3)

    def server2(self, code_mely, n_account):
        client = RPCClient('127.0.0.1', 6001)
        result = client.call('Bankـreturnـcheck', code_mely, n_account)
        print(result)
        return result

    def server3(self, code_mely, n_account):
        client = RPCClient('127.0.0.1', 6002)
        result = client.call('Deferred_installment', code_mely, n_account)
        print(result)
        return result


server = StreamServer(('127.0.0.1', 6000), BorrowServer())
print('server1 is ready')
server.serve_forever()