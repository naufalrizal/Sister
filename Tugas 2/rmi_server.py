import Pyro4
import pickle
import feedparser


class FeedParserMaker(object):
    def parsefeed(self, url):
    	f = feedparser.parse(url)
    	g = pickle.dumps(f)
    	return g
	

parser_maker=FeedParserMaker()
daemon=Pyro4.Daemon() 
ns = Pyro4.locateNS()                
uri=daemon.register(parser_maker)
ns.register("example.greeting", uri)   
print "Ready."					    	
daemon.requestLoop()                  
