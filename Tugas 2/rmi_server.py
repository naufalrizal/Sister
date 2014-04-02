import Pyro4
import urllib
from xml.dom import minidom

dict = {}
list = []

def is_open():
	opener = urllib.FancyURLopener({})
	f = opener.open("http://data.bmkg.go.id/cuaca_mingguan.xml")
	data = f.read()
	#print data
	return data

def process():
	#is_open()		
	#xmldoc = minidom.parse(data)
	xmldoc = minidom.parse('cuaca_indo.xml')
	itemlist = xmldoc.getElementsByTagName('Row')
	for item in itemlist:
		kota = item.getElementsByTagName('Kota')
		cuaca = item.getElementsByTagName('Cuaca') 
		suhumin = item.getElementsByTagName('SuhuMin')
		suhumax = item.getElementsByTagName('SuhuMax')
		kelembapanmin = item.getElementsByTagName('KelembapanMin')
		kelembapanmax = item.getElementsByTagName('KelembapanMax')
		dict['kota'] = kota[0].childNodes[0].nodeValue
		dict['cuaca'] = cuaca[0].childNodes[0].nodeValue
		dict['suhumin'] = suhumin[0].childNodes[0].nodeValue
		dict['suhumax'] = suhumax[0].childNodes[0].nodeValue
		dict['kelembapanmin'] = kelembapanmin[0].childNodes[0].nodeValue
		dict['kelembapanmax'] = kelembapanmax[0].childNodes[0].nodeValue
		list.append(dict)

class isSearch(object):
	def is_search(cityname):
		process()
		for l in list:
			if l['kota'] == cityname :
				hasil = 'Kota : ' + l['kota'] + '\nCuaca : ' + l['cuaca'] + '\nSuhu Minimum : ' + l['suhumin'] + '\nSuhu Maximum : ' + l['suhumax'] + '\nKelembapan Minimum : ' + l['kelembapanmin'] + '\nKelembapan Maximum : ' + l['kelembapanmax']
			else:
				hasil = "Tidak Ada Kota Yang Dimaksud"
			return hasil
		
isSearch = isSearch()
daemon = Pyro4.Daemon()
uri = daemon.register(isSearch)
print "Ready. Object uri =", uri     
daemon.requestLoop()  


