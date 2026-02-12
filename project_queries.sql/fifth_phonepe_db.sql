--8. User Registration Analysis
--Scenario
--PhonePe aims to conduct an analysis of user registration data to identify the top states, districts, and pin codes from which the most users registered during a specific year-quarter combination. This analysis will provide insights into user engagement patterns and highlight potential growth areas.


SELECT *FROM map_user;


--head()

SELECT *FROM map_user
LIMIT 5; 

--sample()

SELECT *FROM map_user
ORDER BY RANDOM()
LIMIT 5;

--tail()

SELECT *FROM map_user
ORDER BY "Year" DESC, "Quarter" DESC
LIMIT 5;

--column_names

SELECT column_name,data_type
FROM information_schema.columns
WHERE table_name = 'map_user';


--Checking null values

SELECT COUNT(*) FROM map_user
WHERE "State" is NULL;


SELECT COUNT(*) FROM map_user
WHERE "District" is NULL;

--OVERALL inspection

SELECT COUNT(*) AS total_rows,
COUNT(DISTINCT "State") AS unique_states,
COUNT(DISTINCT "District") AS unique_district,
MIN("Year") AS min_year,
MAX("Year") AS max_year
FROM map_user;

--------------------------------------------------------------------------------------

--No.1 Analysis


--Lets group by state and aggregating the sum of registered users and see the high performing state

SELECT "State","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "State","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 3;

--SO the top performing states based on sum of total registered counts are

-->"maharashtra"	"2024"	4	71807805
-->"maharashtra"	"2024"	2	70597223
-->"uttar-pradesh"	"2024"	4	70474113

--------------------------------------------------------------------------------------

--No.2 Analysis


--Lets group by district and aggregating the sum of registered users and see the high performing state

SELECT "District","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "District","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 3;

--SO the top performing districts based on sum of total registered counts are

-->"bengaluru urban district"	"2024"	2	18127475
-->"bengaluru urban district"	"2024"	4	18101416
-->"bengaluru urban district"	"2024"	3	17566351

--------------------------------------------------------------------------------------

--No.3 Analysis


--Lets group by pincode and aggregating the sum of registered users and see the high performing state from the table top_user_pincode

SELECT * FROM
top_user_pincode
LIMIT 5;

SELECT "Pincode","Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM top_user_pincode
GROUP BY "Pincode","Year","Quarter"
ORDER BY total_registered_count DESC 
LIMIT 3;

--So the top performing pincode based on sum of total registered counts are

-->"201301"	"2024"	2	1021560
-->"201301"	"2024"	1	984239
-->"201301"	"2024"	4	964283

--------------------------------------------------------------------------------------

--No.4 Analysis

--Lets find out user registration trend over time

SELECT "Year","Quarter",
SUM("Registered_Users") AS total_registered_count
FROM map_user
GROUP BY "Year","Quarter"
ORDER BY "Year","Quarter";

--We can see that User Registrations show a consistent upward trend over time, with higher registrations observed in Q3 and Q4 quarters indicating increasing adoption of PhonePe.

--------------------------------------------------------------------------------------

--No 5 Analysis

--Let we analyse State wise contribution to Total user Registration

SELECT "State",
SUM("Registered_Users") AS state_registered_count,
ROUND(SUM("Registered_Users")*100 / (SELECT SUM("Registered_Users") FROM map_user),2) AS contribution_percentage
FROM map_user
GROUP BY "State"
ORDER BY contribution_percentage DESC;

--so high contributors are 
-->"maharashtra"	1140138243	12.86
-->"uttar-pradesh"	942334146	10.63
-->"karnataka"		733674236	8.28

--and low contributors are
-->"mizoram"					2701061		0.03
-->"ladakh"						2271369		0.03
-->"andaman-&-nicobar-islands"	1842465		0.02
-->"lakshadweep"				142697		0.00

--Insights :-

--> Only a smalll number of states contribute a significant share of total user registrations , highlighting key regions that drive overall platform growth.

--insights overall 

--The Analysis shows that user registrations have increased steadily over time, with the highest growth observed in 2024, especially in Q4. Maharastra and BEngaluru Urban District consistently emerge as top contributors to user registration . However several states show very low contribution, indiacting uneven regional adoption of the platform

--Business Decision

-->Decision 1: Strengthen Presence in high-performaing regions
-->Focus Marketting , partnerships and premium offereing in maharashtra, Uttar Pradesh and Karnataka especially urban centres like Bangalore

-->These regions already show strong adoption and can delivee maximum ROI

-->Desicion 2: Target low-performing states with awareness campaigns

-->Launch localized campaigns , language - specific on boarding and incentive based offers in low-contribution states like Northeast regions , island territories and hill states

--> This can help balance regional growth and expand the user base.

-------------------------------DONE-------------------------------------