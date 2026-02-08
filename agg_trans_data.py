import pandas as pd
import json
import os

agg_trans_path = "data/pulse/data/aggregated/transaction/country/india/state/"
agg_state_list=os.listdir(agg_trans_path)

#To print the state line by line

#for state in agg_state_list:
#    print(state)

col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'Transacion_type':[],
      'Transacion_count':[],    
      'Transacion_amount':[]}

#We have to extract data from only aggregated-->transaction,insurance,user (state level)

#And map-->transaction,insurance,user(state level)

#And top--> transaction,insurance,user(state level)

#So totally 9 DataFrames

#Now lets extracting data from aggregated--> transaction (statelevel)

for state in agg_state_list:
    state_path= agg_trans_path+state+"/"
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
                col_names['Transacion_type'].append(name)
                col_names['Transacion_count'].append(count)
                col_names['Transacion_amount'].append(amount)
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))

#Done extracting the state level transaction data 

#Now lets convert that into data frame

agg_trans = pd.DataFrame(col_names)

#print(agg_trans.head())

#So its done extracting data from aggregated--> transaction

#Function to return the above dataframe

def get_agg_trans_data():
    return agg_trans


if __name__ == "__main__":
    print(agg_trans.head())


