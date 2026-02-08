#Lets Extract data from map-->transaction

import pandas as pd
import json
import os


#Now lets extracting data from aggregated--> insurance

map_trans_path = "data/pulse/data/map/transaction/hover/country/india/state/"
map_state_list=os.listdir(map_trans_path)

#To print the state line by line

#for state in map_state_list:
 #   print(state)


col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'District':[],
      'Count':[],    
      'Amount':[]}


for state in map_state_list:
    state_path= map_trans_path+state+"/"
    map_year= os.listdir(state_path)
    for year in map_year:
        year_path =  state_path+year+"/"
        map_quarter= os.listdir(year_path)
        for quarter in map_quarter:
            quater_path= year_path+quarter
            try:
                with open(quater_path,'r') as data:
                    D=json.load(data)
            except:
                continue
            for i in D['data']['hoverDataList']:
                dist=i['name']
                count=i['metric'][0]['count']
                amount=i['metric'][0]['amount']
                col_names['Year'].append(year)
                col_names['State'].append(state)
                col_names['Quarter'].append(int(quarter.strip('.json')))
                col_names['District'].append(dist)
                col_names['Count'].append(count)
                col_names['Amount'].append(amount)

#Done extracting the state level map-->transaction data 

#Now lets convert that into data frame

map_trans= pd.DataFrame(col_names)

#print(map_trans.head())


#So its done extracting data from map-->transaction

#Function to return the above dataframe

def get_map_trans_data():
    return map_trans    

if __name__ == "__main__":
    print(map_trans.head())