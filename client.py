#!/usr/bin/env python

"""
Client yang akan meminta request data dari server
"""

import socket
import sys
import pickle
import shutil

host = 'localhost'
port = 50000
server_address = (host,port)
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

while 1:
    	print "input berupa nama hari atau semua"
	line = raw_input(">> ")
	s.send(line)
    	data = s.recv(size)
	data2 = pickle.loads(data)
	if type(data2) is list:
		for i in xrange(len(data2)):
			print data2[i]
	else:
		print data2
s.close()