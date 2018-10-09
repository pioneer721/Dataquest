##### BASICS ######

###Single plot
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

### Multiple plots
import matplotlib.pyplot as plt
fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)    #Upper plot
ax2 = fig.add_subplot(2,1,2)    #Bottom plot

#plotting the subplots! 
ax1.plot(unrate["DATE"][:12], unrate["VALUE"][:12])     # first 12 values 
ax2.plot(unrate["DATE"][12:24], unrate["VALUE"][12:24]) # 12~24 values

plt.show()
