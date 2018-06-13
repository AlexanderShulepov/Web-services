import psycopg2
conn_string = "host='localhost' dbname='films' user='postgres' password='842839'"
conn = psycopg2.connect(conn_string)
conn.set_client_encoding('UNICODE')
cursor = conn.cursor()

def query(query):
	cursor.execute("SELECT "+ query)
	records = cursor.fetchall()
	return records[0][0]


print(query("update_studio(1,'6','5','5')"))

        '''studio=query("update_studio({},'{}','{}','{}')".format(
        id,
        str(request.json['name']),
        str(request.json['country']),
        str(request.json['city']) ))'''