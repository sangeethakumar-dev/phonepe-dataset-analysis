import pandas as pd
import json
import os


#Now lets extracting data from top--> user-->district wise

top_user_dist_path = "data/pulse/data/top/user/country/india/state/"
top_state_list=os.listdir(top_user_dist_path)

#To print the state line by line

#for state in top_state_list:
 #   print(state)


col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'District_Name':[],
      'Registered_Users':[]}


for state in top_state_list:
    state_path= top_user_dist_path+state+"/"
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
                col_names['District_Name'].append(i['name'])
                col_names['Registered_Users'].append(i['registeredUsers'])

#Done extracting the  top-->transaction data -->district

#Now lets convert that into data frame

top_dist_user= pd.DataFrame(col_names)

#print(top_dist_user.sample(5))


#So its done extracting data from top-->user-->district

#Function to return the above dataframe

def get_top_user_dist_data():
    return top_dist_user    


if __name__ == "__main__": 
    print(top_dist_user.sample(5))