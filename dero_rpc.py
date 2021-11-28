import requests
from pprint import pprint
'''
INFO[0001] P2P  will listen on 0.0.0.0:20202             com=P2P
INFO[0001] RPC  will listen on 0.0.0.0:20209             com=RPC
'''
class Dero:

    _get_info = {'jsonrpc': '2.0', 'id': '1', 'method': 'get_info'}
    _get_height = {'jsonrpc': '2.0', 'id': '1', 'method': 'getheight'}
    _get_block_count = {'jsonrpc': '2.0', 'id': '1', 'method': 'getblockcount'}

    # def __init__(self, rpc_url='http://0.0.0.0:80/json_rpc'):
    # def __init__(self, rpc_url='http://127.0.0.1:20209/json_rpc'):
    def __init__(self, rpc_url='http://localhost:20209/json_rpc'):
    # def __init__(self, rpc_url='http://0.0.0.0:80/json_rpc'):

        self.rpc_url = rpc_url

    def _post_request(self, payload):
        r = requests.post(self.rpc_url,
                          json=payload, 
                          headers={'Connection': 'close'}
                          )

        if r.status_code == requests.codes.ok:
            d = r.json()

    def get_info(self):
        return self._post_request(self._get_info)

    # def get_height(self):
    #     return self._post_request(self._get_height)

    # def get_block_count(self):
    #     return self._post_request(self._get_block_count)


d = Dero()
d.get_info()
# d.get_height()
# d.get_block_count()

