import Pyro4
import pickle


url = "http://www.reddit.com/r/python/.rss"
parser_maker=Pyro4.Proxy("PYRONAME:example.greeting")
g = parser_maker.parsefeed(url)

feed = pickle.loads(g)
print "Feed Title : " + feed['feed']['title']
print "Feed Link  : " + feed['feed']['link']  
for e in feed.entries:
	print(e.title)
	print(e.link)
	print(e.description)
	print("\n")