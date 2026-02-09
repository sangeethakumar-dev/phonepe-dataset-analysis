import pandas as pd
import json
import os


#Now lets extracting data from top--> user-->pincode

top_user_pin_path = "data/pulse/data/top/user/country/india/state/"
top_state_list=os.listdir(top_user_pin_path)

#To print the state line by line

#for state in top_state_list:
 #   print(state)

col_names={'State':[],
      'Year':[],
      'Quarter':[],
      'Pincode':[],
      'Registered_Users':[]   
      }


for state in top_state_list:
    state_path= top_user_pin_path+state+"/"
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

            for i in D['data']['pincodes']:
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))
                col_names['Pincode'].append(i['name'])
                col_names['Registered_Users'].append(i['registeredUsers'])

#Done extracting the  top-->user data -->pincode

#Now lets convert that into data frame

top_pin_user= pd.DataFrame(col_names)

#print(top_pin_user.sample(5))


#So its done extracting data from top--> user-->pincode

#Function to return the above dataframe

def get_top_user_pin_data():
    return top_pin_user    

if __name__ == "__main__":
    print(top_pin_user.sample(5))