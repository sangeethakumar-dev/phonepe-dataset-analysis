--3. Insurance Penetration and Growth Potential Analysis

--Scenario
--PhonePe has ventured into the insurance domain, providing users with options 
--to secure various policies. With increasing transactions in this segment, 
--the company seeks to analyze its growth trajectory and identify untapped 
--opportunities for insurance adoption at the state level. 
--This data will help prioritize regions for marketing efforts and 
--partnerships with insurers.

---------------HEALTH CHECK-----------------

SELECT *FROM aggregated_insurance;

--head()

SELECT *FROM aggregated_insurance
LIMIT 5;


--tail()

SELECT *FROM aggregated_insurance
ORDER BY "Year" DESC, "Quarter" DESC
LIMIT 5;

--sample()

SELECT *FROM aggregated_insurance
ORDER BY RANDOM()
LIMIT 5;


--column_names

SELECT column_name,data_type
FROM information_schema.columns
WHERE table_name = 'aggregated_insurance';

--get unique transaction type

SELECT DISTINCT "Transaction_type"
FROM aggregated_insurance;


--get the total number of transaction type

SELECT COUNT(DISTINCT "Transaction_type") AS unique_device_count
FROM aggregated_insurance;

--Checking null values

SELECT COUNT(*) FROM aggregated_insurance
WHERE "Transaction_type" is NULL;

SELECT COUNT(*) FROM aggregated_insurance
WHERE "State" is NULL;

--OVERALL inspection

SELECT COUNT(*) AS total_rows,
COUNT(DISTINCT "Transaction_type") AS unique_transaction_type,
COUNT(DISTINCT "State") AS unique_states,
MIN("Transaction_count") AS min_transaction_count,
MAX("Transaction_count") AS max_transaction_count,
MIN("Transaction_amount") AS min_transaction_amount,
MAX("Transaction_amount") AS max_transaction_amount
FROM aggregated_insurance;

--------------------------------------------------------------------------------------

--No.1 Query

--Lets group by states and aggregating average of transactionamount and transaction count
--and seeing the higher adoptiion state and lower one


--Here taking the average of transaction amounnt and transaction count
--As this will gives the equal weight to small and big populated states

SELECT "State",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "State"
ORDER BY average_insurance_value DESC
LIMIT 3;

--States like ladakh,arunachal-pradesh,sikkim are having higher average insurance value

--whereas 
SELECT "State",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "State"
ORDER BY average_insurance_value
LIMIT 3;

--States like andhra-pradesh,delhi,bihar are having lower average insurance value.


--------------------------------------------------------------------------------------

--No.2 Query

--Lets group by year and aggregating average of transaction amount and transaction count
--and seeing the higher adoption state and lower one


--Here taking the average of transaction amount and transaction count
--As this will gives the equal weight to small and big populated states

SELECT "Year",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Year"
ORDER BY average_insurance_value DESC
LIMIT 3;

--In the year order of 2024,2023,2022 the average insurance value are higher

--whereas 

SELECT "Year",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Year"
ORDER BY average_insurance_value
LIMIT 3;

--here in the year of order 2020,2021,2022 are having lower insurance value

--so the adoption rate of insurance are gradually increasing yera by year

--The average insurance transaction value shows a consistent upward trend from 2020 to 2024,
--indicating increasing user willingness to purchase higher - value  insuarance products over time

--------------------------------------------------------------------------------------

--No.3 Query

--Lets group by quarter and aggregating average of transaction amount and transaction count
--and seeing the higher adoption state and lower one


--Here taking the average of transaction amount and transaction count
--As this will gives the equal weight to small and big populated states

SELECT "Quarter",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Quarter"
ORDER BY average_insurance_value DESC
LIMIT 3;

--In the quarter order of 4,1,2 the average insurance value are higher

--whereas 

SELECT "Quarter",
SUM ("Transaction_count") AS total_transaction_count,
SUM ("Transaction_amount") AS total_transaction_amount,
(SUM ("Transaction_amount")/SUM ("Transaction_count")) AS average_insurance_value
FROM aggregated_insurance
GROUP BY "Quarter"
ORDER BY average_insurance_value
LIMIT 3;

--here in the quarter order of 3,2,1 are having lower insurance value

--Quarter wise analysis reveals that Q3 and Q4 record the highest average insurance values 
--suggesting that festive and year end periods drive increased insurance purchases
--likely due to financial planning and promotional offers


--------------------------------------------------------------------------------------

--No.4 Query

--Lets group by states and aggregating the sum of transaction count and see the
--insurance penetration

SELECT "State",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State"
ORDER BY total_transaction_count DESC
LIMIT 3;

--Finally i can see tamil nadu here ,
--states  like karnataka,maharashtra,tamil-nadu are having higher insurance counts

SELECT "State",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State"
ORDER BY total_transaction_count
LIMIT 3;

--states like lakshadweep,ladakh,mizoram are having lower actually very lower insuarance counts


--------------------------------------------------------------------------------------

--No.5 Query

--Lets group by states,year and aggregating the sum of transaction count and see the
--insurance penetration


SELECT "State","Year",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State","Year"
ORDER BY total_transaction_count DESC
LIMIT 3;

--Finally i can see tamil nadu here ,
--states  like karnataka[2024],maharashtra[2024],karnataka[2023] are having higher insurance counts

SELECT "State","Year",
SUM ("Transaction_count") AS total_transaction_count
FROM aggregated_insurance
GROUP BY "State","Year"
ORDER BY total_transaction_count 
LIMIT 3;

--states like lakshadweep[2020],lakshadweep[2021],ladakh[2020] are having lower actually very lower insuarance counts

--Insights

-->Smaleer states such as Ladakh , Arunachal pradesh and sikkim show highre average insurance values
--indicating presence for premium insurance products despite lower adoption. 
--In contrast , high population states like Tamil Nadu, Karnataka and Maharashtra drive overall
--insurance adoption with significantly higher transaction volumes , especially during Q3 and Q4
--and in 2024 reflecting growing maturity and seasonal demand

--Business Decisions

-->Phonepe should prioritize high volume states like Tamil Nadyu, Karnataka, and Maharashtra
--for large scale insurance partnerships and mass market campaigns particularly during Q3 and Q4 when 
--demand peaks. Simultaeneously, low- adoption but high value states such as Ladakh and 
--Arunachal Pradesh can be targeted with premium insurance products and localized awareness
--initiatives to unlock untapped revenue  potential.

---------------------DONE---------------
