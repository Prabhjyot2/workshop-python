import socket 
import requests
try:
	socket.create_connection(("www.google.com",80))
	res=requests.get("https://ipinfo.io/")
	print(res)
	data = res.json()
	print(data)
	city = data['city']
	print("city name",city)
	country = data['country']
	print("country name",country)
	loc=data['loc']
	print(loc)
	latlon = loc.split(",")
	lat=latlon[0]
	lon=latlon[1]
	print("latitude",lat)
	print("longitude",lon)
except OSError as e:
	print("check network")
