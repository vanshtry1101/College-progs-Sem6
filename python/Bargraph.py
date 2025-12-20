import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel("FSI-2023-DOWNLOAD.xlsx")


x = data['Country']
y = data['P2: Public Services']

plt.bar(x,y,label="numbers",color="green")

plt.title("Graph of number")
plt.xlabel("Scale")
plt.ylabel("Parameters")
plt.legend()
plt.show()




















"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_excel("FSI-2023-DOWNLOAD.xlsx")

# Correct column access
x = data['Country']
y = data['P2: Public Services']

# Plot
plt.figure(figsize=(12, 6))
plt.bar(x, y, color="green")

plt.title("Public Services Score by Country")
plt.xlabel("Country")
plt.ylabel("P2: Public Services")
plt.xticks(rotation=90)        # Rotate labels for readability
plt.tight_layout()
plt.show()

"""
