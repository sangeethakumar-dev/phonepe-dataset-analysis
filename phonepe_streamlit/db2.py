
import pandas as pd


from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

#----------------------------2nd Business Case Study--------------------------------------

#------------------2) Device Dominance and User Engagement Analysis----------------------------

#--------------Analysis 1 :Overall Brand-wise User Base and Engagement Analysis ---------------------------------
 
#This analysis evaluates overall device brand dominance by aggregating user base and app engagement across all states and reporting periods. 
#It highlights the brands with the strongest market presence and user interaction levels.

#Chart 1 Query

def fetch_registered_users_count_device_higher():
    query = """
       SELECT "Device_Brand",
       SUM("Device_Count") AS total_brand_users
FROM aggregated_user
GROUP BY "Device_Brand"
ORDER BY total_brand_users DESC
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 2 Query

def fetch_app_usage_count_device_higher():
    query = """
        SELECT "Device_Brand",
       SUM("Device_Count") AS engagement_score
FROM aggregated_user
GROUP BY "Device_Brand"
ORDER BY engagement_score DESC
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df


#--------------Analysis 2 : State-wise Device Adoption Trends ---------------------------------
 
#Examines registered users and app opens by device brand across states.
#Highlights regional preferences and device penetration patterns.


#Chart 1 Query

def fetch_device_count_state_higher():
    query = """
    SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_device_count DESC
    LIMIT 5 ;
    """
    df = pd.read_sql(query, engine)
    return df


#Chart 2 Query

def fetch_device_count_state_lower():
    query = """
    SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_device_count ASC
    LIMIT 5;
    """
    df = pd.read_sql(query, engine)
    return df


#Chart 3 Query

def fetch_app_opens_state_higher():
    query = """
    SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_app_opens DESC
    LIMIT 5;
    """
    df = pd.read_sql(query, engine)
    return df



#Chart 4 Query

def fetch_app_opens_state_lower():
    query = """
    SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    HAVING SUM("App_Opens")>0
    ORDER BY total_app_opens ASC
    LIMIT 5;
    """
    df = pd.read_sql(query, engine)
    return df


#--------------Analysis 3 : Quarterly Device Performance Analysis ---------------------------------
 
#Evaluates how device brands perform across different quarters.
#Identifies seasonal or time-based growth trends in user registrations and app activity



#Chart 1 Query

def fetch_registered_users_count_device_quarter_higher():
    query = """
     SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_device_count DESC;
        """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 2 Query

def fetch_registered_users_count_device_quarter_lower():
    query = """
     SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_device_count ASC;

        """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 3 Query

def fetch_app_usage_count_device_quarter_higher():
    query = """
    SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_app_opens DESC;

        """
    
    df=pd.read_sql(query,engine)
    return df


#Chart 4 Query

def fetch_app_usage_count_device_quarter_lower():
    query = """  
SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_app_opens ASC;
        """
    
    df=pd.read_sql(query,engine)
    return df

#--------------Analysis 4 : State-wise User Registration & App Activity Overviews ---------------------------------

#Provides a comparative view of user registrations and app opens across states.
#Helps identify high-growth and high-engagement regions.


 #Chart 1 Query

def fetch_registered_users_count_state_lower():
    query = """  
SELECT "State",
SUM("Device_Count") AS registered_users_count
FROM aggregated_user
GROUP BY  "State"
ORDER BY registered_users_count DESC
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

 #Chart 2 Query

def fetch_app_usage_count_state_higher():
    query = """  
SELECT "State",
SUM("App_Opens") AS app_usage_count
FROM aggregated_user
GROUP BY  "State"
ORDER BY app_usage_count DESC 
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df


#--------------Analysis 5: Multi-Dimensional Device Usage Analysis ---------------------------------

#Analyzes device brand performance across states and quarters simultaneously.
#Offers deep insights into geographic and temporal usage behavior patterns.


 #Chart 1 Query

def fetch_registered_users_count_state_device_quarter_higher():
    query = """  
SELECT 
    "State",
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    MAX("Registered_Users") AS registered_users,
    MAX("App_Opens") AS app_opens
FROM aggregated_user
GROUP BY "State","Device_Brand","Quarter"
ORDER BY total_device_count DESC
LIMIT 10;

        """
    
    df=pd.read_sql(query,engine)
    return df