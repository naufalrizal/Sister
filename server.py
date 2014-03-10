import sys
import pickle
import socket
import select


hari = []
keterangan = []

filename = 'cuaca.txt'

f = open(filename,'rb')

strText=f.read()
data = strText.split('\n')

for i in data:
	temp = i.split(',')	
	hari.append(temp[0])
	keterangan.append(temp[1])	

# creating socket server object, bind, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 50000))
server_socket.listen(5)

# list to store accepted client
input_list = [server_socket]

try:
	while 1:
        	# serving multiple client alternately; one socket in a time
        	input, output, exception = select.select(input_list, [], [])
    
        	for socket in input:
            	# accept client and add it to list input
            		if socket == server_socket:
                		client_socket, client_address = server_socket.accept()
		                input_list.append(client_socket)
        		        print "Accepted client: ", client_address
            
            	# handle sending and receiving message
            		else:
				rcv_message = socket.recv(1024)
				for i in xrange(len(hari)):
					if hari[i] == rcv_message:
						message = hari[i] + ', ' + keterangan[i] 						
						message = pickle.dumps(message)
					elif rcv_message == 'all':
						message = pickle.dumps(data)	
	        		if message:
                    			socket.send(message)
                    			print "Send to client : ", client_address, message
                		else:
                    			socket.close()
                    			input_list.remove(socket)

# when user press CTRL + C (in Linux), close socket server and exit
except KeyboardInterrupt:
	server_socket.close()
	sys.exit(0)