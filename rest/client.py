import requests as r

print(r.get('http://127.0.0.1:5000/api/studios').text.decode("utf-8"))