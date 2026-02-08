import pandas as pd
import json
import os

map_user_path = "data/pulse/data/map/user/hover/country/india/state/"
map_state_list=os.listdir(map_user_path)

#To print the state line by line

#for state in map_state_list:
 #   print(state)

col_names={'State':[],
           'Year':[],
           'Quarter':[],
           'District':[],
           'Registered_Users':[],
           'App_Opens':[]
}


for state in map_state_list:
    state_path= map_user_path+state+"/"
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
            dist=D['data']['hoverData']
            for i in dist:
                users=dist[i]['registeredUsers']
                app=dist[i]['appOpens']
                distr=i
                
                col_names['State'].append(state)
                col_names['Year'].append(year)
                col_names['Quarter'].append(int(quarter.strip('.json')))
                col_names['District'].append(distr)
                col_names['Registered_Users'].append(users)
                col_names['App_Opens'].append(app)

#Done extracting the map user data 

#Now lets convert that into data frame

map_user = pd.DataFrame(col_names)

#print(map_user.head())

#So its done extracting data from map--> user

#Function to return the above dataframe

def get_map_user_data():
    return map_user    

if __name__ == "__main__":
    print(map_user.head())