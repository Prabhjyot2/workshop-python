import socket
import requests
try:
	city=input("enter location name ")
	socket.create_connection(("www.google.com",80))
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
