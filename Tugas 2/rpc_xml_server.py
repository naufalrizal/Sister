import xmlrpclib, urllib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from xml.dom import minidom

dict={}
list=[]

def is_open():
	opener = urllib.FancyURLopener({})
	f = opener.open("http://data.bmkg.go.id/cuaca_indo_1.xml")
	data = f.read()
	return data

def write(data):
	file = open("cuaca_indo.xml", "w")
	file.write(data)
	file.close()

def process():
#	data = is_open()
#	write(data)
	xmldoc = minidom.parse('cuaca_indo.xml')
	itemlist = xmldoc.getElementsByTagName('Row')
	for item in itemlist:
		kota = item.getElementsByTagName('Kota')
		cuaca = item.getElementsByTagName('Cuaca') 
		suhumin = item.getElementsByTagName('SuhuMin')
		suhumax = item.getElementsByTagName('SuhuMax')
		kelembapanmin = item.getElementsByTagName('KelembapanMin')
		kelembapanmax = item.getElementsByTagName('KelembapanMax')
		dict = {}
		dict['kota'] = kota[0].childNodes[0].nodeValue
		dict['cuaca'] = cuaca[0].childNodes[0].nodeValue
		dict['suhumin'] = suhumin[0].childNodes[0].nodeValue
		dict['suhumax'] = suhumax[0].childNodes[0].nodeValue
		dict['kelembapanmin'] = kelembapanmin[0].childNodes[0].nodeValue
		dict['kelembapanmax'] = kelembapanmax[0].childNodes[0].nodeValue
		list.append(dict)

def is_search(cityname):
	process()
	#hasil = ''
	for l in list:
		#hasil = hasil + l['kota'] 
		if l['kota'] == cityname :
			hasil = 'Kota : ' + l['kota'] + '\nCuaca : ' + l['cuaca'] + '\nSuhu Minimum : ' + l['suhumin'] + '\nSuhu Maximum : ' + l['suhumax'] + '\nKelembapan Minimum : ' + l['kelembapanmin'] + '\nKelembapan Maximum : ' + l['kelembapanmax']
		else:
			hasil = 'Tidak Ada Kota Yang Dimaksud'
	return list

def is_list():
	process()
	hasil = ''
	for l in list:
			hasil = hasil + 'Kota : ' + l['kota'] + '\nCuaca : ' + l['cuaca'] + '\nSuhu Minimum : ' + l['suhumin'] + '\nSuhu Maximum : ' + l['suhumax'] + '\nKelembapan Minimum : ' + l['kelembapanmin'] + '\nKelembapan Maximum : ' + l['kelembapanmax'] + '\n\n'
	return hasil

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(is_list, "is_list")
server.serve_forever()
