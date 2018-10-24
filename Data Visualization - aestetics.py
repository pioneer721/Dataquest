### Percentages of men and women per degree over time

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    ax.set_title(major_cats[sp]) #title per chart 
    ax.tick_params(bottom="off", top="off", left="off", right="off") #Removing Ticks

    #Setting x and y
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)

    #Removing Boundaries 
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    
    #Putting text(labels) within chart. 근데 별로 쓸모 없는듯. 
     if sp==0:
        ax.text(2005, 87, "Men")  # (x, y, "text")
        ax.text(2002, 8, "Women")
    if sp==5:
        ax.text(2005, 62, "Men")
        ax.text(2001, 35, "Women")
    
 

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()



