from suds.client import Client
####soap метод 
c = Client('http://127.0.0.1:8001?wsdl')
print(c.service.get(str(11)))


