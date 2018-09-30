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




### Clearning price_euros column ###
       #a) replace decimal commans with decimal points
       #b) convert to float              

laptops["price_euros"] = (laptops["price_euros"]
                          .str.replace("," , ".")
                          .astype(float)
                         )

price_describe= laptops["price_euros"].describe()
                                     


    
        
 
