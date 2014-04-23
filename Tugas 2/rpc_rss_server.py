import feedparser
from SimpleXMLRPCServer import SimpleXMLRPCServer

dict = {}
list = []

def process() :
	d = feedparser.parse('http://www.reddit.com/r/python/.rss')
	for i in xrange(len(d.entries)):
		dict = {}
		dict['title'] = d['entries'][i]['title']
		dict['published'] = d['entries'][i]['published']
		dict['link'] = d['entries'][i]['link']
		list.append(dict)

def is_list() :
	process()
	hasil = ''
	for l in list :
		hasil = hasil + 'Title : ' + l['title'] + '\nPublished : ' + l['published'] + '\nLink : ' + l['link'] + '\n\n\n'
	return hasil

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(is_list, "is_list")
server.serve_forever()
