import pandas as pd
data = pd.read_csv("STUDENT.csv")



print("")
d1=data.head()
print(d1)
print("*"*40)

print("")
d2=data.head(3)
print(d2)
print("*"*40)

print("")
d3=data.tail()
print(d3)
print("*"*40)

print("")
d4=data.tail(3)
print(d4)
print("*"*40)

print("")
d5=data[:]
print(d5)
print("*"*40)

print("")
d6=data[::]
print(d6)
print("*"*40)

print("")
d7=data[2:]
print(d7)
print("*"*40)

print("")
d8=data[::2]
print(d8)
print("*"*40)

print("")
d9=data[:3]
print(d9)
print("*"*40)

print("")
d10=data[::-1]
print(d10)
print("*"*40)

#filtering
print("students staying in mumbai")
d11=data[data['LOCATION']=='MUMBAI']
print(d11)
print("*"*40)

print("students whose age is >= 19")
d12=data[data['AGE']>=19]
print(d12)
print("*"*40)

print("students who stay in mumbai and age is 19")
d13=data[ (data['LOCATION']=='MUMBAI') & (data['AGE']>=19)]
print(d13)
print("*"*40)

print("highest marks in school")
m1=data['SUB1'].max()
print(m1)
print("*"*40)

print("complete info abt student scoring highest marks in school")
m1=data['SUB1'].max()
d14=data[data['SUB1'] == m1]
print(d14)
