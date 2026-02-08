import pandas as pd
import json
import os

agg_user_path = "data/pulse/data/aggregated/user/country/india/state/"
agg_state_list=os.listdir(agg_user_path)

#To print the state line by line

#for state in agg_state_list:
 #   print(state)

col_names={'State':[],
           'Year':[],
           'Quarter':[],
           'Registered_Users':[],
           'App_Opens':[],
           'Device_Brand':[],
           'Device_Count':[],
           'Device_Percentage':[]
}

for state in agg_state_list:
    state_path= agg_user_path+state+"/"
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
            
            user=D['data']['aggregated']['registeredUsers']
            appopens=D['data']['aggregated']['appOpens']
            devices = D['data'].get('usersByDevice')
            if devices is not None:
                for i in devices:
                    brand=i['brand']
                    count=i['count']
                    percentage=i['percentage']
                col_names['Registered_Users'].append(user)
                col_names['App_Opens'].append(appopens)
                col_names['Device_Brand'].append(brand)
                col_names['Device_Count'].append(count)
                col_names['Device_Percentage'].append(percentage)
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))

#Done extracting the state level user data 

#Now lets convert that into data frame

agg_user = pd.DataFrame(col_names)

#print(agg_user.head())

#So its done extracting data from aggregated--> user

#Function to return the above dataframe

def get_agg_user_data():
    return agg_user

if __name__ == "__main__":
    print(agg_user.head())