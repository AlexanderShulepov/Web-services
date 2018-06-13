#import jsonrpcclient
#print(jsonrpcclient.request('http://localhost:5000/', 'ping'))
from jsonrpcclient.request import Request
from jsonrpcclient.http_client import HTTPClient
client = HTTPClient('http://localhost:5000/')
print(client.send(Request('ping','mama im coming home!' )))