import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("STUDENT.csv")
mdata = data[data['LOCATION'] == 'MUMBAI'] 
print(mdata)

name=mdata['NAME'].tolist()
sub1=mdata['SUB1'].tolist()
print(name)
print(sub1)

plt.bar(name, sub1)
plt.savefig("mumbai.pdf")
plt.savefig("mumbai.png")
plt.show()
