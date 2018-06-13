
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.model.complex import Array
from lxml import etree
from spyne.protocol.soap import Soap11
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication

import psycopg2
conn_string = "host='localhost' dbname='films' user='postgres' password='842839'"
conn = psycopg2.connect(conn_string)
conn.set_client_encoding('UTF-8')
cursor = conn.cursor()
 

class Soap(ServiceBase):
    @rpc(Unicode, _returns=Array(Unicode))
    def get(ctx, id):
        #print(etree.tostring(ctx.in_document))
        cursor.execute("SELECT  get_studio("+str(id)+")")
        records = cursor.fetchall()
        records=records[0][0]
        print (records)
        if not records['code']:
            return ['Error']
        return [records[u'cname'],records[u'ccountry'],records[u'ccity']]


app = Application([Soap], tns='Translator',
                          in_protocol=Soap11(validator='lxml'),
                         out_protocol=Soap11())
application = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()