import requests
from pprint import pprint


class Dero(object):
    _headers = {'Connection': 'close'}

    _get_info = {'jsonrpc': '2.0', 'id': '1', 'method': 'get_info'}
    _get_height = {'jsonrpc': '2.0', 'id': '1', 'method': 'getheight'}
    _get_block_count = {'jsonrpc': '2.0', 'id': '1', 'method': 'getblockcount'}

    _get_address = {'jsonrpc': '2.0', 'id': '1', 'method': 'getaddress'}

    def __init__(self, rpc_url='http://localhost:20209/json_rpc'):
        self.rpc_url = rpc_url

    def _post_request(self, payload):
        r = requests.post(self.rpc_url,
                          json=payload,
                          headers=self._headers)
        try:
            return r.json()
        except Exception as e:
            raise Exception(f'dero exception: {e}')

    def get_info(self):
        return self._post_request(self._get_info)

    def get_height(self):
        return self._post_request(self._get_height)

    def get_block_count(self):
        return self._post_request(self._get_block_count)

    def get_address(self):
        '''wallet'''
        return self._post_request(self._get_address)

