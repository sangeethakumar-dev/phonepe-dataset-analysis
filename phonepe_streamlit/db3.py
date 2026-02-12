
import pandas as pd


from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

#----------------------------3rd Business Case Study--------------------------------------

#------------------3) Insurance Penetration and Growth Potential Analysis----------------------------


# ---------- Analysis 1 : State-wise Insurance Adoption Performance ----------

#Analyzes average transaction amount and transaction count across states to identify high-performing and low-performing insurance markets.
#Highlights regional disparities in insurance penetration and adoption intensity.

#Chart 1 Query

def fetch_avg_insurance_state_higher():
    query = """
       SELECT "State",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "State"
ORDER BY average_insurance_value DESC
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 2 Query

def fetch_avg_insurance_state_lower():
    query = """
       SELECT "State",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "State"
ORDER BY average_insurance_value
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 2 : Yearly Insurance Growth Trend Analysis ----------

#Evaluates yearly average transaction amount and transaction count to understand insurance adoption trends over time.
#Identifies peak growth years and periods of slower market expansion.


#Chart 1 Query

def fetch_avg_insurance_year_higher():
    query = """
       SELECT "Year",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Year"
ORDER BY average_insurance_value DESC
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df


#Chart 2 Query

def fetch_avg_insurance_year_lower():
    query = """
       SELECT "Year",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Year"
ORDER BY average_insurance_value
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 3 :  Quarterly Insurance Demand Pattern ----------

#Examines quarter-wise average transaction metrics to detect seasonal insurance purchasing behavior.
#Reveals high-activity quarters and short-term adoption fluctuations.


#Chart 1 Query

def fetch_avg_insurance_quarter_higher():
    query = """
       SELECT "Quarter",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Quarter"
ORDER BY average_insurance_value DESC
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df


#Chart 2 Query

def fetch_avg_insurance_quarter_lower():
    query = """
       SELECT "Quarter",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Quarter"
ORDER BY average_insurance_value
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 4 :  State-wise Insurance Volume Concentration ----------

#Aggregates total transaction count by state to determine overall insurance volume distribution.
#Identifies dominant markets and underpenetrated regions based on total policy purchases.


#Chart 1 Query

def fetch_total_transaction_count_state_higher():
    query = """
       SELECT "State",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State"
ORDER BY total_transaction_count DESC
LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df


#Chart 2 Query

def fetch_total_transaction_count_state_lower():
    query = """
       SELECT "State",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State"
ORDER BY total_transaction_count
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df


# ---------- Analysis 5 :  State-Year Insurance Growth Comparison ----------

#Analyzes transaction count growth across states over different years to assess expansion patterns.
#Highlights consistently growing states and regions with declining or stagnant adoption.


#Chart 1 uery

def fetch_total_transaction_count_state_year_higher():
    query = """
       SELECT "State","Year",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State","Year"
ORDER BY total_transaction_count DESC
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 2 Query

def fetch_total_transaction_count_state_year_lower():
    query = """
       SELECT "State","Year",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State","Year"
ORDER BY total_transaction_count 
LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df













