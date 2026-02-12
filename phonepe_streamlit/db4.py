
import pandas as pd


from sqlalchemy import create_engine

engine=create_engine("postgresql+psycopg2://postgres:sachumas123@localhost:5432/phonepe_db")

print("Connected to PostgreSQL Successfully")

#----------------------------4th Business Case Study--------------------------------------

#------------------4) Transaction Analysis Across States and Districts----------------------------

# ---------- Analysis 1 : State-Level Transaction Performance Overview ----------

#Analyzes total transaction count and total transaction amount aggregated at the state level.
#Identifies the highest-performing states contributing maximum transaction volume and value.

#Chart 1 Query

def fetch_total_amount_state_higher():
    query = """  
SELECT "State",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;
        """
    
    df=pd.read_sql(query,engine)
    return df


# ---------- Analysis 2 : District-Level Transaction Performance Analysis ----------

#Evaluates transaction count and total transaction amount at the district level.
#Highlights top-performing districts driving regional transaction growth.

#Chart 1 Query

def fetch_total_amount_district_higher():
    query = """  
		SELECT "District",
	SUM("Count") AS total_count,
	SUM("Amount") AS total_amount
	FROM map_transaction
	GROUP BY "District"
	ORDER BY total_amount DESC,
	total_count DESC
	LIMIT 3;
        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 3 : PIN Code-Level Transaction Concentration Study ----------

#Aggregates transaction count and amount by PIN code to identify localized transaction hotspots.
#Reveals high-activity micro-markets contributing significantly to overall transactions.

#Chart 1 Query

def fetch_total_amount_pincode_higher():
    query = """  
	SELECT "Pincode",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM top_transaction_pincode
GROUP BY "Pincode"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;
        """
    
    df=pd.read_sql(query,engine)
    return df


# ---------- Analysis 4 : State-District-Year Transaction Trend Analysis ----------

#Examines yearly transaction performance across state and district combinations.
#Identifies which state-district pairs recorded peak transaction volume and value in specific years.

#Chart 1 Query

def fetch_total_count_state_district_year_higher():
    query = """  
	SELECT "State","District","Year",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State","District","Year"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;

        """
    
    df=pd.read_sql(query,engine)
    return df

# ---------- Analysis 5 : Quarterly Transaction Performance by Region ----------

#Analyzes transaction count and amount across state, district, year, and quarter dimensions.
#Provides insights into seasonal and quarterly transaction trends at the regional level.


#Chart 1 Query

def fetch_total_count_state_district_year_quarter_higher():
    query = """  
	SELECT "State","District","Year","Quarter",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State","District","Year","Quarter"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;
        """
    
    df=pd.read_sql(query,engine)
    return df