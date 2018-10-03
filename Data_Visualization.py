#BASICS 
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE']) #converting the DATE column into a Series of datetime values.

first_twelve= unrate[:12] 
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])

plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

plt.show()
