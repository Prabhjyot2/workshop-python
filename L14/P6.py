import socket
import requests
try:
	socket.create_connection(("www.google.com",80))
	mn = input("enter movie name ")
	a1="http://www.omdbapi.com/?"
	a2="&apikey=b88add31"
	a3="&s="+mn
	res=requests.get(a1+a2+a3)
	print(res)
	data=res.json()
	print(data)	
	search = data['Search']
	for s in search:
		title=s['Title']
		year=s['Year']
		poster_url=s['Poster']
		print(title,"-->",year,"-->",poster_url)
		print("*"*40)
		if poster_url != "N/A":
			res=requests.get(poster_url)
			file_name = title+".jpg"
			with open(file_name,"wb") as f:
						f.write(res.content)
						print("file downloaded")

except OSError as e:
	print("check network")
