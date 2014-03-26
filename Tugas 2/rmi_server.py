import urllib

opener = urllib.FancyURLopener({})
f = opener.open("http://data.bmkg.go.id/cuaca_mingguan.xml")
data = f.read()
print data