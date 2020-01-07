import socket 
import requests
try:
	socket.create_connection(("www.google.com",80))
	res=requests.get("https://ipinfo.io/")
	print(res)
	data = res.json()
	print(data)
	country = data['country']
	print("country name",country)
	loc=data['loc']
	print(loc)
	latlon = loc.split(",")
	lat=latlon[0]
	lon=latlon[1]
	print("latitude",lat)
	print("longitude",lon)	
	city = data['city']
	print("city name",city)
	city=input(city)
	a1="https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1 +a2 +a3
	res1=requests.get(api_address)
	print(res1)
	data=res1.json()
	print(data)
	main=data['main']
	temp=main['temp']
	print("aaj ka temperature",temp)
except OSError as e:
	print("check network")
