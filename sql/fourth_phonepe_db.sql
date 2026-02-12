--7. Transaction Analysis Across States and Districts
--Scenario
-->PhonePe is conducting an analysis of transaction data to identify the top-performing 
--states, districts, and pin codes in terms of transaction volume and value. 
--This analysis will help understand user engagement patterns and identify key areas 
--for targeted marketing efforts.

SELECT *
FROM "map_transaction";

--head()

SELECT *FROM map_transaction
LIMIT 5; 

--sample()

SELECT *FROM map_transaction
ORDER BY RANDOM()
LIMIT 5;

--tail()

SELECT *FROM map_transaction
ORDER BY "Year" DESC, "Quarter" DESC
LIMIT 5;

--column_names

SELECT column_name,data_type
FROM information_schema.columns
WHERE table_name = 'map_transaction';

--get uniques states

SELECT DISTINCT "State"
FROM map_transaction;


SELECT DISTINCT "District"
FROM map_transaction;

--get the total number of unique districts

SELECT COUNT(DISTINCT "District") AS unique_states_count
FROM map_transaction;

--yes there are 36 states in total

--And 843 districts in total

--To check no. of rows(df.shape())

SELECT COUNT(*) FROM map_transaction;

--get number of each unique states

SELECT "State", COUNT(*)
FROM map_transaction
GROUP BY "State";

--get number of each unique districts

SELECT "District", COUNT(*)
FROM map_transaction
GROUP BY "District";

--Checking null values

SELECT COUNT(*) FROM map_transaction
WHERE "State" is NULL;


SELECT COUNT(*) FROM map_transaction
WHERE "District" is NULL;

--OVERALL inspection

SELECT COUNT(*) AS total_rows,
COUNT(DISTINCT "State") AS unique_states,
COUNT(DISTINCT "District") AS unique_district,
MIN("Year") AS min_year,
MAX("Year") AS max_year
FROM map_transaction;

--------------------------------------------------------------------------------------

--No.1 Analysis


--Lets group by state and aggregating the sum of count and sum of amount and see the high
--performing state

SELECT "State",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;

--SO the top performing states based on sum of transaction amount and sum of 
--transaction are telangana,karnataka,maharashtra 

--------------------------------------------------------------------------------------

--No.2 Analysis


--Lets group by district and aggregating the sum of count and sum of amount 
--and see the high performing district

	SELECT "District",
	SUM("Count") AS total_count,
	SUM("Amount") AS total_amount
	FROM map_transaction
	GROUP BY "District"
	ORDER BY total_amount DESC,
	total_count DESC
	LIMIT 3;

--so the top performing districts are bengaluru urban district,hyderabad district,
--pune district

--------------------------------------------------------------------------------------

--No.3 Analysis


--Lets group by pincode and aggregating the sum of count and sum of amount 
--and see the high performing pincode

--and this is from the table top_transaction_pincode

SELECT *FROM "top_transaction_pincode"
LIMIT 5;

SELECT "Pincode",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM top_transaction_pincode
GROUP BY "Pincode"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;

--so the top performing pincodes are 500001, 500034,560001

-----------------------------------------------------------------------------------

--No 4 Analysis


SELECT "State","District","Year",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State","District","Year"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;

--top performing
-->"karnataka"	"bengaluru urban district"	"2024"
-->"karnataka"	"bengaluru urban district"	"2023"
-->"telangana"	"hyderabad district"	"2022"

--This analysis identifies the state and district combination that recorded the
--highest transaction value in each year, highlighting how transaction concentration 
--evolves over time


-----------------------------------------------------------------------------------

--No 5 Analysis


SELECT "State","District","Year","Quarter",
SUM("Count") AS total_count,
SUM("Amount") AS total_amount
FROM map_transaction
GROUP BY "State","District","Year","Quarter"
ORDER BY total_amount DESC,
total_count DESC
LIMIT 3;

--top performing
-->"karnataka"	"bengaluru urban district"	"2024"	4
-->"telangana"	"hyderabad district"		"2022"	4
-->"karnataka"	"bengaluru urban district"	"2024"	3

--This analysis examines state-district combination across quarters to
--identify seasonal peaks in transaction value, providing insights into temporal 
--transactionbehavior


--Insights

-->the analaysis reveleas that transaction activity is heavily concentrated in a few key regions, particularly Maharashtra, Karnataka, Telangana which consisitently emerge as top-performing states, districts and pincodes across multiple years and quarters. This consistent dominance indicates mature digital payment adoption and stable transaction behavior with identifiable temporal peaks suggesting periods of increased transaction activity.

--Business Decision 1

--> PhonPe can prioritize marketting campaigns , merchant partnerships and feature rollouts in consistently high performing regions to maximize return on investment

--Business Decision 2

--> Quarter level peak patterns can be leveraged to time promotional offers and cashback campaigns during high-transaction periods.

----------------------------------DONE---------------------------------------