import requests
import json

url = "http://localhost:8002/"
headers = {'content-type': 'application/json'}

print('Вызов метода avg_rate:')
payload={"method": "avg_rate", "jsonrpc": "2.0",  "id": 0,}
response = json.loads(requests.post(url, data=json.dumps(payload), headers=headers).text)
print('jsonrpc: {}\nОтвет:{}'.format(response['jsonrpc'], response['result']))
print('------------------------------------------------\n')


print('Вызов метода get_studio:')
payload={  "method": "get_studio","id": 1,"params": [1], "jsonrpc": "2.0"}
response = json.loads(requests.post(url, data=json.dumps(payload), headers=headers).text)
print('jsonrpc: {}\nОтвет: {}'.format(response['jsonrpc'], response['result']))
print('------------------------------------------------\n')

print('Вызов метода get_sum_actions:')

payload={  "method": "get_sum_actions","id": 2, "jsonrpc": "2.0"}
response = json.loads(requests.post(url, data=json.dumps(payload), headers=headers).text)
print('jsonrpc: {}\nОтвет: {}'.format(response['jsonrpc'], response['result'][0]['Сборы']))







