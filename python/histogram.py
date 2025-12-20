import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel("FSI-2023-DOWNLOAD.xlsx")


x=data['Country']
bins=[1.1,2.5,3.5,4.5,5.5,6.5,7.5]

plt.hist(x,bins, rwidth=0.6,label="numbers",color="green")

plt.title("Graph of number")
plt.xlabel("Scale")
plt.ylabel("Parameters")
plt.legend()
plt.show()
