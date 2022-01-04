from gevent.server import StreamServer

from mprpc import RPCServer, RPCClient


class BorrowServer(RPCServer):

    def borrow(self, code_mely, n_account):
        Bankـreturnـcheck = self.server2(self, code_mely, n_account)
        Deferred_installment = self.server3(self, code_mely, n_account) # gest_mavaghe
        return Bankـreturnـcheck, Deferred_installment

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
server.serve_forever()