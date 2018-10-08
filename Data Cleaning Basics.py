"""
### Cleaning "storage" column: reading data and putting each into appropriate new column ###  
EX: 
76                 2TB HDD
77    128GB SSD +  1TB HDD
78                 1TB HDD

Objective: make 4 columns, storage_1_capacity_gb, storage_1_type, storage_2_capacity_gb,storage_2_type
"""

#1. Figure out which types there are
#print(laptops["storage"].unique())


#2. Remove GB, TB
laptops["storage"] = (laptops["storage"]
                      .str.replace("GB", "")
                      .str.replace("TB", "000")
                     )
#print(laptops["storage"].head(10))

#3. Split "storage" column into two columns
laptops[["storage_1","storage_2"]]= laptops["storage"].str.split("+", expand= True) 


#4. clean both columns using for loop
for s in laptops[["storage_1", "storage_2"]]:
    # name for the new columns
    s_capacity = s + "_capacity_gb"
    s_type = s + "_type"
    
    #Creating new columns for capacity and type!
    laptops[[s_capacity, s_type]] = laptops[s].str.split(n=1, expand= True) 
    
    #changing capacity into float (can't be int cuz of missing values)
    laptops[s_capacity] = laptops[s_capacity].astype(float)         

    #Removing extra white spaces
    laptops[s_type]= laptops[s_type].str.strip() 
    

#5 Remove unneeded 
laptops.drop(["storage", "storage_1", "storage_2"], axis=1, inplace=True)    


### Conclude: REORDERING
#New order of the columns
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer',  'cpu_speed', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']

#Applying the order to dataframe
laptops=laptops[cols] 

#saving laptops into a csv file, and reading it 
laptops.to_csv("laptops_cleaned.csv", index= False)
laptops_cleaned = pd.read_csv('laptops_cleaned.csv')

#Looking at data types of the new csv file 
laptops_cleaned_dtypes = laptops_cleaned.dtypes

# ----------------------------------------------------------------------------------#
                                     

#### Are laptops made by Apple more expensive than those by other manufacturers? ###

#Average price of apple 
apple= laptops[laptops["manufacturer"] == "Apple"]
apple_avg= apple["price_euros"].mean() 
print("apple avg price: ", apple_avg)

#Average price of other manufacturers
others= laptops[laptops["manufacturer"] != "Apple"]
others_avg= others["price_euros"].mean() 
print("others avg price: ", others_avg)

print("Laptops made by Apple are more expensive than those by others!")


# ----------------------------------------------------------------------------------#


#### Which laptop has the most storage space? ###
 
#Making a simpler dataframe with just the columns i need
laptops2= laptops[["model_name","storage_1_capacity_gb","storage_2_capacity_gb"]]

#Converting the NaN values in storage_2_capacity_gb into zero so I can do calculations 
null_storage2= laptops2[laptops2["storage_2_capacity_gb"].isnull()]
null_storage2["storage_2_capacity_gb"] = 0        

#Calculating total capacity of each laptop
laptops2["total_capacity"] = laptops2["storage_1_capacity_gb"] + laptops2["storage_2_capacity_gb"]

#Declaring the dataframe's total capacity part as "capacity"
capacity= laptops2["total_capacity"]

#Finding the elements that have the same capacity as the greatest capasity 
highest_storage= laptops2[capacity ==  capacity.max()]

print(highest_storage)


# ----------------------------------------------------------------------------------#


### Cleaning "weight" column ###
    # a) remove non-digit
    # b) convert to float
    # c) rename column 

laptops["weight"]= (laptops["weight"]
                    .str.replace("kg" , "") # removing kg
                    .str.replace("s" , "")  # removing s cuz one had s 
                    #(Without this, ERROR cuz can't convert to float since 4.54kgs would turn into 4.54s)
                    .astype(float)
                   )

laptops.rename( {"weight" : "weight_kg"}, axis=1, inplace= True)
weight_describe= laptops["weight_kg"].describe()

# Checking if weight column has letter s anywhere
# print(laptops.loc[laptops["weight"].str.contains('s'), "weight"]   )


# ----------------------------------------------------------------------------------#


### EXTRACTING MANUFATURER NAME AND CREATING A NEW COLUMN FOR IT ###
"""
The Series.str.split() method accepts an argument n, which controls the maximum number of splits allowed. 
By using n=1, the method will make a single split on the first whitespace

expand=True argument expands series of lists into a dataframe:
"""

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"]= ( laptops["cpu"]
                              .str.split(n=1, expand=True)
                              .iloc[:,0]
                             )

print(laptops.cpu.head(6))
print()
print(laptops.cpu_manufacturer.head(6))


"""
OUTPUT

0          Intel Core i5 2.3GHz
1          Intel Core i5 1.8GHz
2    Intel Core i5 7200U 2.5GHz
3          Intel Core i7 2.7GHz
4          Intel Core i5 3.1GHz
5       AMD A9-Series 9420 3GHz
Name: cpu, dtype: object

0    Intel
1    Intel
2    Intel
3    Intel
4    Intel
5      AMD
Name: cpu_manufacturer, dtype: object
"""


# ----------------------------------------------------------------------------------#




    
        
 
