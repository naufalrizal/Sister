import Pyro4

uri=raw_input("What is the Pyro uri of the greeting object? ").strip()
cityname=raw_input("Masukan nama kota : ").strip()

isSearch = Pyro4.Proxy(uri)
print isSearch.is_search()

