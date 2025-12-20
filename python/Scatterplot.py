import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel("FSI-2023-DOWNLOAD.xlsx")

x=data["Country"][:5]
y=[1.1,2.5,3.5,4.5,5.5][:5]
ex=[0,0,0.3,0,0]
plt.pie(y,labels=y,autopct='%.2f%%',shadow=True,explode=ex)

##plt.title("Graph of number")
##plt.xlabel("Scale")
##plt.ylabel("Parameters")
plt.legend()
plt.show()
