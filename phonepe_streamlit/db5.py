
import pandas as pd


from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

#----------------------------5th Business Case Study--------------------------------------

#------------------5) User Registration Analysis----------------------------
    
# ---------- Analysis 1 : State-Level User Registration Performance Overview ----------

#Evaluates total registered users aggregated at the state level to identify high-performing states.
#Highlights regional adoption patterns and leading contributors to overall user growth.1

#Chart 1 Query

def fetch_total_count_state_year_quarter_higher():
    query = """  
SELECT "State","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "State","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 10;
        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 2 : District-Level User Registration Analysis ----------

#Examines cumulative user registrations across districts to determine top-performing regions.
#Provides insights into localized growth concentration within states.

#Chart 1 Query

def fetch_total_count_district_year_quarter_higher():
    query = """  
SELECT "District","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "District","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 10;
        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 3 : PIN Code-Level User Registration Concentration Study ----------

#Analyzes registered users at the PIN code level to uncover high-density micro-markets.
#Reveals granular adoption trends and areas with strong user penetration.

#Chart 1 Query

def fetch_total_count_pincode_year_quarter_higher():
    query = """  
SELECT "Pincode","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM top_user_pincode
GROUP BY "Pincode","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 10;

        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 4 : Quarterly User Registration Trend Analysis ----------

#Tracks user registration growth over year and quarter to identify temporal trends.
#Highlights seasonal patterns and periods of accelerated user acquisition.

#Chart 1 Query

def fetch_year_quarter_trend():
    query = """  
SELECT "Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "Year","Quarter"
ORDER BY "Year","Quarter";

        """
    
    df=pd.read_sql(query,engine)
    return df


# ---------- Analysis 5 : State Contribution to Total User Registration----------

#Assesses each state's proportional contribution to overall registered users.
#Helps understand regional dominance and distribution of user base nationwide.

#Chart 1 Query

def fetch_total_contribution_state_higher():
    query = """  
SELECT "State",
SUM("Registered_Users") AS state_registered_count,
ROUND(SUM("Registered_Users")*100 / (SELECT SUM("Registered_Users") FROM map_user),2) AS contribution_percentage
FROM map_user
GROUP BY "State"
ORDER BY contribution_percentage DESC;
        """
    
    df=pd.read_sql(query,engine)
    return df