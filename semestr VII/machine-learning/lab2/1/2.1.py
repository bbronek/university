import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data2.csv", header=None)

selected_column1 = 2
selected_column2 = 3

column2 = data.columns[selected_column1]
column3 = data.columns[selected_column2]

plt.scatter(data[selected_column1], data[selected_column2])
plt.xlabel(column2 + 1)
plt.ylabel(column3 + 1)
plt.title("Dot plot between the third and fourth columns")

plt.show()
