f500["roa"]= f500["profits"] / f500["assets"]

top_roa_by_sector= {} 

for sector in f500["sector"].unique():
    is_sector= f500["sector"]==sector      # BOOL 
    sector_companies= f500.loc[is_sector]
    top_company= sector_companies.sort_values("roa", ascending= False).iloc[0]
    company_name= top_company.loc["company"] 
    top_roa_by_sector[sector]= company_name
