import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
print proxy.is_list()
