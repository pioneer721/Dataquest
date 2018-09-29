##### Exploring Data with Pandas

### Company with highest employees per country ###
top_employer_by_country= {} 
countries= f500["country"].unique()

for c in countries:
    selected_rows= f500[f500["country"]==c]
    sorted_rows= selected_rows.sort_values("employees", ascending= False) 
    top_employer= sorted_rows.iloc[0]
    employer_name= top_employer.loc["company"] 
    top_employer_by_country[c]= employer_name
    

### Company with highest ROA per each sector ###
f500["roa"]= f500["profits"] / f500["assets"]
top_roa_by_sector= {} 

for sector in f500["sector"].unique():
    is_sector= f500["sector"]==sector					# BOOL 
    sector_companies= f500.loc[is_sector]				# selecting rows that satisfy bool	
    top_company= sector_companies.sort_values("roa", ascending= False).iloc[0]	
    	#1- sort sector companies by "roa" descendingly. 
	#2- iloc[0] -> the first of the slice, which is the highest roa
    company_name= top_company.loc["company"] 			# company's name 					
    top_roa_by_sector[sector]= company_name			# Adding name to dictionary 			
