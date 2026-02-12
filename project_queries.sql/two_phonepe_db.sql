--2. Device Dominance and User Engagement Analysis
--Scenario
--PhonePe aims to enhance user engagement and improve app performance by understanding user 
--preferences across different device brands. The data reveals the number of registered users 
--and app opens, segmented by device brands, regions, and time periods. However, trends in 
--device usage vary significantly across regions, and some devices are disproportionately 
--underutilized despite high registration numbers.

--Intro to this query is 
--To analyze device dominance and user engagement , i performed five queries on the 
--aggregated_user table,examining device wise dominance, regional adoption , temporal trends 
--and cross analysis of device brands with states and time periods to derive actionable 
--insights for targetted campaigns.


SELECT *FROM aggregated_user;


--head()

SELECT *FROM aggregated_user
LIMIT 5;

--sample()

SELECT *FROM aggregated_user
ORDER BY RANDOM()
LIMIT 5;

--tail()

SELECT *FROM aggregated_user
ORDER BY "Year" DESC, "Quarter" DESC
LIMIT 5;

--column_names

SELECT column_name,data_type
FROM information_schema.columns
WHERE table_name = 'aggregated_user';

--get uniques DEVICE

SELECT DISTINCT "Device_Brand"
FROM aggregated_user;


--get the total number of unique devices

SELECT COUNT(DISTINCT "Device_Brand") AS unique_device_count
FROM aggregated_user;

--Checking null values

SELECT COUNT(*) FROM aggregated_user
WHERE "Device_Brand" is NULL;

SELECT COUNT(*) FROM aggregated_user
WHERE "State" is NULL;

--OVERALL inspection

SELECT COUNT(*) AS total_rows,
COUNT(DISTINCT "Device_Brand") AS unique_devices,
MIN("Registered_Users") AS min_user,
MAX("Registered_Users") AS max_user,
MIN("App_Opens") AS min_app_counts,
MAX("App_Opens") AS max_app_counts
FROM aggregated_user;

--------------------------------------------------------------------------------------

--No.1 Query

--Lets group by device brands and check the max of registerd users and app opens
SELECT "Device_Brand",
       SUM("Device_Count") AS total_brand_users
FROM aggregated_user
GROUP BY "Device_Brand"
ORDER BY total_brand_users DESC
LIMIT 5;


--So we can see that device brands
-->"Realme"	48227630	2570606469
-->"Vivo"	48227630	2570606469
-->"Tecno"	48227630	2570606469
--are higher in registered_users_count

SELECT "Device_Brand",
       SUM("Device_Count") AS engagement_score
FROM aggregated_user
GROUP BY "Device_Brand"
ORDER BY engagement_score DESC
LIMIT 5;


-->same device brands here too
-->"Realme"	48227630	2570606469
-->"Vivo"	48227630	2570606469
-->"Tecno"	48227630	2570606469
--are higher in app_usage_count

--My insight
--> Realme, Vivo, Tecno are dominant device brands in terms of registerd users and app 
--usage

--------------------------------------------------------------------------------------

--No.2 Query

-->Lets group by both devices and state and seeing the max of registered users and
--max of registered count

SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_device_count DESC
    LIMIT 5;

--so we can see that device brands-->
-->"Huawei"	"maharashtra"	48227630	2157769514
-->"Xiaomi"	"maharashtra"	48227630	2157769514
-->"Tecno"	"maharashtra"	48227630	2157769514

--are in higher registered_users_count

--where as

SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_device_count ASC
    LIMIT 5;

-->"COOLPAD"	"lakshadweep"	501	0
-->"Gionee"	"lakshadweep"	918	0
-->"Vivo"	"lakshadweep"	5990	67320

--are having lower registered_users_count

SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
    ORDER BY total_app_opens DESC
    LIMIT 5;

--So we can see that device brands-->
-->"Oppo"	"rajasthan"	23398857	2570606469
-->"Realme"	"rajasthan"	23398857	2570606469
-->"Samsung"	"rajasthan"	23398857	2570606469
--are having higher app_uasge_count

--whereas

SELECT "Device_Brand","State",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
    FROM aggregated_user
    GROUP BY "Device_Brand","State"
	HAVING SUM("App_Opens")>0
    ORDER BY total_app_opens ASC
	LIMIT 5;

-->"Micromax"	"manipur"	61935	0
-->"Micromax"	"punjab"	1152190	0
-->"Lenovo"	"arunachal-pradesh"	61852	0

--are having literally zero app_usage_count eventhough having good registered users counts


--Insights from this query is 
-->To improve user adoption in low engagemrnt regions, phonepe should shift focus from increasing
--registrations on low -performing device brands (like Micromax,"Lenovo",coolpad,Gionee) to
--driving engagement through high performing brands likr Oppo and Realme, while simultaeneously
--optimising app experienceand onboarding for users in connectivity - constrained regions

--------------------------------------------------------------------------------------

--No.3 Query

-->Lets group by both devices and time periods(quartesrs) and
--seeing the max of registered users and max of registered count

SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_device_count DESC;




--SO WE can see that quarter
-->"Realme"	1	48227630	2570606469
-->"Samsung"	1	48227630	2570606469
-->"Others"	1	48227630	2570606469
--are havung higher registered_users_count


SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_device_count ASC;


-->"COOLPAD"	1	501	0
-->"Lyf"	1	29925	0
-->"Lyf"	2	46055	0

--are having lower registered_users_count

SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_app_opens DESC;


-->"Realme"	1	48227630	2570606469
-->"Samsung"	1	48227630	2570606469
-->"Others"	1	48227630	2570606469

--are having higher app_usage_count

SELECT
    "Device_Brand",
    "Quarter",
    SUM("Device_Count") AS total_device_count,
    SUM("App_Opens") AS total_app_opens
FROM aggregated_user
GROUP BY "Device_Brand", "Quarter"
ORDER BY total_app_opens ASC;


-->"Lyf"	1	29925	0
-->"Lyf"	2	46055	0
-->"COOLPAD"	1	501	0

--are having lower app_usage_count	

--Insghts 

-->Here i could combine this with the aggregated transacyional behavior,
-->Question :- If payments happens through the app , why dont app opens peak in 
--Q3/Q4 as well?

-->Answer:- Device brands such as Realme and Samsung show peak user registration and
--app engagement in early quarters, indicating their strong role in initial onboarding . 
--However, transaction volumes peak in later quarters, suggesting that once users are 
--onboarded , they transform from exploraryory app usage to more intentionsl, transaction-
--focused behavior over time.

--Where as the lower brands are fail at the first onboarding step, so only they never seen 
--reach in the transaction heavy phase

--Business Decions includes

-->Seperate onboarding startegy from Transaction startegy:-

--> Q1- focused campaigns-->education ease, onboarding
--> Q3,Q4 - focused campaigns --> offers , cashback, repeat usage

--Dont expect both to peak together

--Growth engines are Realme and Samsung as they are good in app insatlls, new user on boarding
--Awareness campaigns

--------------------------------------------------------------------------------------

--No.4 Query

-->Lets group by regions and seeing the max of registered users and app counts


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


--Actually the states maharashtra,uttar-pradesh,karnataka,rajasthan are tend to more
--usage in both registered_users_count,app_usage_count.

SELECT "State",
MAX("Registered_Users") AS registered_users_count,
MAX("App_Opens") AS app_usage_count
FROM aggregated_user
GROUP BY  "State"
ORDER BY registered_users_count DESC
LIMIT 3;

--So here the regions lakshadweep,andaman-&-nicobar-islands,ladakh are always accounting
--for lower adoption states in terms of registered_users_count,app_usage_count.

--------------------------------------------------------------------------------------

--No.5 Query

-->Lets group by all the device brands, states, quarter and seeing the behavior of 
--app usage and registered users

SELECT "State","Device_Brand","Quarter",
MAX("Registered_Users") AS registered_users_count,
MAX("App_Opens") AS app_usage_count
FROM aggregated_user
GROUP BY  "State","Device_Brand","Quarter"
ORDER BY registered_users_count 
LIMIT 3;

------------------------------------------------------------------------------


--Insights

-->User Engagement on phonepe is driven by device compatibility and regional maturity than
--by time period, with mainstream device brands enabling string adoption in high - performing states
--while low-end devices contribute to engagement gaps in underpenetrated regions

--Business Decisions

-->1)
--> Use Different startegies for different transactoins
---->High adoption states--> Scale campaigns, merchant partnership, volume growth
-----> Low Adoption states --> Education , on boarding ,trust and device specific optimization.

--2)
-->Seperate Onboarding success from Transaction success
-->Early quarters-- measure success by registration and app opens
--> Later quarters -- measure success by transaction and value



-----------------------DONE-------------------------