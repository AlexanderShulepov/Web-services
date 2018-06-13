from flask import Flask, jsonify, abort,make_response, request,Response
import json
import psycopg2
import postgresql
app = Flask(__name__)

conn_string = "host='localhost' dbname='films' user='postgres' password='842839'"
conn = psycopg2.connect(conn_string)
conn.set_client_encoding('UNICODE')
cursor = conn.cursor()

def query(query):
	cursor.execute("SELECT "+query)
	records = cursor.fetchall()
	return records[0][0]
def jsonit(data):
	return json.dumps(data,ensure_ascii=False)

##################################################################################################################
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)
#############################

@app.route('/api/studios', methods=['GET'])
def get_studios():
    print('11111111111111111')
    args=request.args
    studios=None
    if 'order' in args:
        studios=query("get_ord_studios('{}')".format(args['order']))
    elif 'filter' in args:
        studios=query("get_filter_studios('{}')".format(args['filter']))
    elif 'pagination' in args:
        studios=query("get_page_studios('{}')".format(args['pagination']))
    else:
        studios=query("get_studios()")

    return  make_response(jsonit(studios),200)
#############################

@app.route('/api/studios/<int:id>', methods=['GET'])
def get_studio(id):
    studio=query("get_studio("+str(id)+")")
    print(studio)
    if studio['code']==404:
        abort(404)
    return  make_response(jsonit(studio),200)
#############################

@app.route('/api/studios', methods=['POST'])
def set_studio():
    if not request.json :
         abort(400)
    try:
    studio=query("add_studio('{}','{}','{}')".format( str(request.json['name']),str(request.json['country']),str(request.json['city']) ))

    return  make_response(jsonit(studio),200)

#############################
@app.route('/api/studios/<int:id>', methods=['PUT'])
def update_studio(id):
    if not request.json :
         abort(400)
    studio=query("update_studio({},'{}','{}','{}')".format(
        id,
        str(request.json['name']),
        str(request.json['country']),
        str(request.json['city']) ))
    print(studio)
    return  make_response(jsonit(studio),200)
#############################

@app.route('/api/studios/<int:id>', methods=['DELETE'])
def delete_studio(id):
    try:
        studio=query("delete_studio("+str(id)+")")
    except:
        return  make_response(json.dumps({"error":"tables are referenced "}),406)
    return  make_response(jsonit(studio),201)
#############################

@app.route('/api/studios/avg_rate', methods=['GET'])
def avg_rate():
    studios=query("avg_rate_studios()")
    return  make_response(jsonit(studios),200)


if __name__ == '__main__':
    app.run(debug=True,port=8001)