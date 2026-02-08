import pandas as pd
import json
import os


#Now lets extracting data from top--> insurance-->district wise

top_insur_dist_path = "data/pulse/data/top/insurance/country/india/state/"
top_state_list=os.listdir(top_insur_dist_path)

#To print the state line by line

#for state in top_state_list:
 #   print(state)

col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'District_Name':[],
      'Count':[],    
      'Amount':[]}

for state in top_state_list:
    state_path= top_insur_dist_path+state+"/"
    top_year= os.listdir(state_path)
    for year in top_year:
        year_path =  state_path+year+"/"
        top_quarter= os.listdir(year_path)
        for quarter in top_quarter:
            quater_path= year_path+quarter
            try:
                with open(quater_path,'r') as data:
                    D=json.load(data)
            except:
                continue

            for i in D['data']['districts']:
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))
                col_names['District_Name'].append(i['entityName'])
                col_names['Count'].append(i['metric']['count'])
                col_names['Amount'].append(i['metric']['amount'])

#Done extracting the  top-->insurance data 

#Now lets convert that into data frame

top_dist_insur= pd.DataFrame(col_names)

#print(top_dist_insur.head())



#So its done extracting data from top--> insurance

#Function to return the above dataframe

def get_top_insur_dist_data():
    return top_dist_insur    

if __name__ == "__main__":
    print(top_dist_insur.head())