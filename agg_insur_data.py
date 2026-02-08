from db_connection import engine

import pandas as pd
import json
import os


#Now lets extracting data from aggregated--> insurance

agg_insur_path = "data/pulse/data/aggregated/insurance/country/india/state/"
agg_state_list=os.listdir(agg_insur_path)

#To print the state line by line

#for state in agg_state_list:
 #   print(state)


col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'Transaction_type':[],
      'Transaction_count':[],    
      'Transaction_amount':[]}


for state in agg_state_list:
    state_path= agg_insur_path+state+"/"
    agg_year= os.listdir(state_path)
    for year in agg_year:
        year_path =  state_path+year+"/"
        agg_quarter= os.listdir(year_path)
        for quarter in agg_quarter:
            quater_path= year_path+quarter
            try:
                with open(quater_path,'r') as data:
                    D=json.load(data)
            except:
                continue
            for i in D['data']['transactionData']:
                name=i['name']
                count=i['paymentInstruments'][0]['count']
                amount=i['paymentInstruments'][0]['amount']
                col_names['Transaction_type'].append(name)
                col_names['Transaction_count'].append(count)
                col_names['Transaction_amount'].append(amount)
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))


#Done extracting the state level aggregated-->insurance data 

#Now lets convert that into data frame

agg_insur= pd.DataFrame(col_names)

#print(agg_insur.head())


#So its done extracting data from aggregated--> insurance

#Function to return the above dataframe

def get_agg_insur_data():
    return agg_insur

if __name__ == "__main__":
    print(agg_insur.head())