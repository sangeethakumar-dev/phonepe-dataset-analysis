
import pandas as pd


from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

def map_func():
    query= """
SELECT "State" AS "State",
SUM("Registered_Users") AS "Value"
FROM aggregated_user
GROUP BY "State"
"""
    df=pd.read_sql(query,engine)

    state_mapping = {
    "andaman-&-nicobar-islands": "Andaman and Nicobar",
    "andhra-pradesh": "Andhra Pradesh",
    "arunachal-pradesh": "Arunachal Pradesh",
    "assam": "Assam",
    "bihar": "Bihar",
    "chandigarh": "Chandigarh",
    "chhattisgarh": "Chhattisgarh",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli",
    "delhi": "Delhi",
    "goa": "Goa",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "himachal-pradesh": "Himachal Pradesh",
    "jammu-&-kashmir": "Jammu and Kashmir",
    "jharkhand": "Jharkhand",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "lakshadweep": "Lakshadweep",
    "madhya-pradesh": "Madhya Pradesh",
    "maharashtra": "Maharashtra",
    "manipur": "Manipur",
    "meghalaya": "Meghalaya",
    "mizoram": "Mizoram",
    "nagaland": "Nagaland",
    "odisha": "Odisha",
    "puducherry": "Puducherry",
    "punjab": "Punjab",
    "rajasthan": "Rajasthan",
    "sikkim": "Sikkim",
    "tamil-nadu": "Tamil Nadu",
    "telangana": "Telangana",
    "tripura": "Tripura",
    "uttar-pradesh": "Uttar Pradesh",
    "uttarakhand": "Uttarakhand",
    "west-bengal": "West Bengal"
}

    df["State"] = df["State"].map(state_mapping)
    df['State']=df['State'].replace({'Odisha':'Orissa'})
    return df


#----------------------------1st Business Case Study--------------------------------------

#------------------1. Decoding Transaction Dynamics on PhonePe----------------------------

#--------------Analysis 1 : State-wise Transaction Summary ---------------------------------

# Analyze state-wise transaction dynamics by aggregating total transaction count
# and total transaction amount to identify regional usage patterns.


def fetch_total_transaction_amount_higher_state():
    query = """
        SELECT "State",
        SUM("Transaction_count") AS total_transaction_count,
        SUM("Transaction_amount") AS total_transaction_amount
        FROM aggregated_transaction
        GROUP BY "State"
        ORDER BY total_transaction_amount DESC
        LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_amount_lower_state():
    query = """
    SELECT "State",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "State"
    ORDER BY total_transaction_amount 
    LIMIT 5;

        """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_count_higher_state():
    query = """
    SELECT "State",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "State"
    ORDER BY total_transaction_count DESC
    LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_count_lower_state():
    query = """
    SELECT "State",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "State"
    ORDER BY total_transaction_count
    LIMIT 5;
        """
    
    df=pd.read_sql(query,engine)
    return df

#--------------Analysis 2 : Quarter-wise Transaction Summary ---------------------------------

#This analysis aggregates total transaction count and transaction amount across all quarters


def fetch_total_transaction_amount_higher_quarter():
    query = """
    SELECT "Quarter",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "Quarter"
    ORDER BY total_transaction_amount DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df


def fetch_total_transaction_count_higher_quarter():
    query = """
    SELECT "Quarter",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "Quarter"
    ORDER BY total_transaction_count DESC;

    """
    
    df=pd.read_sql(query,engine)
    return df


#--------------Analysis 3 : Payment Category Analysis ---------------------------------

#This analysis aggregates transactions by payment type to evaluate overall transaction volume and value.



def fetch_total_transaction_amount_transaction_type():
    query = """
    SELECT "Transaction_type",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "Transaction_type"
    ORDER BY total_transaction_amount DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_count_transaction_type():
    query = """
    SELECT "Transaction_type",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "Transaction_type"
    ORDER BY total_transaction_count DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df


#--------------Analysis 4 : State-wise Payment Category Performance Analysis ---------------------------------

#This analysis examines how different payment categories perform across states using transaction volume and transaction value.
#It helps identify dominant payment modes and underperforming regions for strategic insights.

def fetch_total_transaction_amount_state_transaction_type_higher():
    query = """
    SELECT "State","Transaction_type",
    SUM("Transaction_count") AS total_transaction_count,
    SUM("Transaction_amount") AS total_transaction_amount
    FROM aggregated_transaction
    GROUP BY "State","Transaction_type"
    ORDER BY total_transaction_amount DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df


def fetch_total_transaction_amount_state_transaction_type_lower():
    query = """
SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_amount;
    """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_count_state_transaction_type_higher():
    query = """
SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_count DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df

def fetch_total_transaction_count_state_transaction_type_lower():
    query = """
SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_count;
    """
    
    df=pd.read_sql(query,engine)
    return df


#--------------Analysis 5 : State–Quarter Transaction Comparison ---------------------------------

#This analysis compares transaction count and transaction amount across states, quarters, and transaction types.
#It helps understand digital payment distribution and performance patterns across different regions and periods.

#Chart 1

def fetch_total_transaction_count_state_transaction_type_quarter_higher():
    query = """
SELECT "State","Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter"
ORDER BY total_transaction_count DESC
    """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 2

def fetch_total_transaction_count_state_transaction_type_quarter_lower():
    query = """
SELECT "State","Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_count;
    """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 3

def fetch_total_transaction_amount_state_transaction_type_quarter_higher():
    query = """
SELECT "State","Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_amount DESC;
    """
    
    df=pd.read_sql(query,engine)
    return df

#Chart 4

def fetch_total_transaction_amount_state_transaction_type_quarter_lower():
    query = """
SELECT "State","Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_amount;
    """
    
    df=pd.read_sql(query,engine)
    return df