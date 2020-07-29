import bs4
import requests
import datetime

res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res)
	
soup = bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})
print(quote)

text=quote['alt']
print("text of the day",text)

photo_url = "https://www.brainyquote.com" + quote['data-img-url']
print(photo_url)

res=requests.get(photo_url)
d=datetime.datetime.now().date()
file_name = str(d)+ ".jpg"
with open(file_name,"wb") as f:
				f.write(res.content)
				print("file downloaded")
