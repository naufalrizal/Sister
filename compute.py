def loadPickle(filename):
	import pickle
	f = open(filename,'rb')
	data = pickle.loads(f.read())
	return data

def euclidean_distance(data,centroid):
	import socket
	from scipy import spatial
	host = socket.gethostname()
	temp = []
	for i in xrange(len(centroid)):
		val = spatial.distance.euclidean(data,centroid[i])
		temp.append(val)
	ind = temp.index(min(temp))+1
	return (host,ind)

if __name__ == '__main__':
    	import dispy, random,numpy
	centroid = loadPickle('centroid.csv')
	test = loadPickle('testdata.csv')
	datatest = numpy.array(test)
	hasil = []
    	cluster = dispy.JobCluster(euclidean_distance,nodes=['192.168.56.101','192.168.56.102'])
    	jobs = []
    	for n in range(10000):
        	job = cluster.submit(datatest[n],centroid)
        	job.id = n
        	jobs.append(job)
    	for job in jobs:
        	host, n = job() # waits for job to finish and returns results
		      hasil.append(n)
        	print '%s executed data test %s class %s' % (host, job.id, n)
    	cluster.stats()
	print len(hasil)
