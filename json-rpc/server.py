from flask import Flask, request, Response
from jsonrpcserver import methods
import postgresql
import json
connector = postgresql.open('pq://postgres:842839@localhost:5432/films')

def query(query):	#postgresq query
	return json.loads(connector.query("select "+ query)[0][0])



app = Flask(__name__)



########################################
@methods.add
def avg_rate():
    studios=query("avg_rate_studios()")
    return  studios

@methods.add
def get_studio(id):
    studio=query("get_studio("+str(id)+")")
    print(studio)
    if studio['code']==404:
        return {'error': 'Not found'}, 404
    return  studio

@methods.add
def get_sum_actions():
    studios=query("top_actions()")
    return  studios

@app.route('/', methods=['POST'])
def index():
    req = request.get_data().decode()
    response = methods.dispatch(req)
    return Response(str(response), response.http_status,
                    mimetype='application/json')

if __name__ == '__main__':
    app.run(port=8002)