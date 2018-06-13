from flask import Flask, request, Response
from jsonrpcserver import methods

app = Flask(__name__)

@methods.add
def ping(param=None):
    return '11111111111111111111'

@app.route('/', methods=['POST'])
def index():
    req = request.get_data().decode()
    response = methods.dispatch(req)
    return Response(str(response), response.http_status,
                    mimetype='application/json')

if __name__ == '__main__':
    app.run(port=8002)