--1. Decoding Transaction Dynamics on PhonePe
--Scenario
--PhonePe, a leading digital payments platform, has recently identified significant 
--variations in transaction behavior across states, quarters, and payment categories. 
--While some regions and transaction types demonstrate consistent growth, others show 
--stagnation or decline. The leadership team seeks a deeper understanding of these patterns
--to drive targeted business strategies.


SELECT *FROM aggregated_transaction;

--head()

SELECT *FROM aggregated_transaction
LIMIT 5; 

--sample()

SELECT *FROM aggregated_transaction
ORDER BY RANDOM()
LIMIT 5;

--tail()

SELECT *FROM aggregated_transaction
ORDER BY "Year" DESC, "Quarter" DESC
LIMIT 5;

--column_names

SELECT column_name,data_type
FROM information_schema.columns
WHERE table_name = 'aggregated_transaction';

--get uniques states

SELECT DISTINCT "State"
FROM aggregated_transaction;

--get the total number of unique states(BUT LONGEST)

WITH state_count AS(
SELECT DISTINCT "State"
FROM aggregated_transaction
)

SELECT COUNT(*) AS total_unique_state
FROM state_count;

--get the total number of unique states(BUT Shortest)

SELECT COUNT(DISTINCT "State") AS unique_states_count
FROM aggregated_transaction;

--yes there are 36 states in total

--To check no. of rows(df.shape())

SELECT COUNT(*) FROM aggregated_transaction;

--get number of each unique states

SELECT "State", COUNT(*)
FROM aggregated_transaction
GROUP BY "State";

--Checking null values

SELECT COUNT(*) FROM aggregated_transaction
WHERE "State" is NULL;

--OVERALL inspection

SELECT COUNT(*) AS total_rows,
COUNT(DISTINCT "State") AS unique_states,
MIN("Year") AS min_year,
MAX("Year") AS max_year
FROM aggregated_transaction;

--------------------------------------------------------------------------------------

--No.1 Query

-- Analyze state-wise transaction dynamics by aggregating total transaction count and total transaction amount to identify regional usage patterns.


-- lets order it by total_transaction_amount and see

SELECT "State",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State"
ORDER BY total_transaction_amount DESC
LIMIT 3;

--so we can see that telangana amount -->41655955630076.31, count-->26174684592
--					 karnataka amount -->40678721773666.375,count-->30970946279
--					 maharashtra amount-->40374195687971.67,count-->31985208732
--are higher by transaction amount


SELECT "State",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State"
ORDER BY total_transaction_amount 
LIMIT 3;

--so we can see that lakshadweep amount -->1609320784.7771473, count-->883994
--					 mizoram amount -->46102103410.33138,count-->19535750
--					 andaman-&-nicobar-islands amount-->70667453146.59808,count-->39706951
--are lower by transaction amount


-- lets order it by transaction_count and see

SELECT "State",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State"
ORDER BY total_transaction_count DESC
LIMIT 3;

--so we can see that maharashtra amount -->40374195687971.67, count-->31985208732
--					 karnataka amount -->40678721773666.375,count-->30970946279
--					 telangana amount-->41655955630076.31,count-->26174684592
--are higher by transaction count

SELECT "State",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State"
ORDER BY total_transaction_count 
LIMIT 3;

--so we can see that lakshadweep amount -->1609320784.7771473, count-->883994
--					 mizoram amount -->46102103410.33138,count-->19535750
--					 ladakh amount-->88994622100.10213,count-->39345875
--are lower by transaction count

-------------------------------------------------------------------------------

--No.2 Analysis

--Lets groupby quarters and seeing transaction count and transaction amount

-- lets order it by transaction_amount and see

SELECT "Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "Quarter"
ORDER BY total_transaction_amount DESC;

--so we can see that quarter -->
-->4	70638277656	101909692480018.39
-->3	62141176425	88233138211669.73
-->2	54659969115	82024231029539.02
--are higher by transaction amount.

--and its reverse for lower transaction amount.

-- lets order it by transaction_count and see

SELECT "Quarter",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "Quarter"
ORDER BY total_transaction_count DESC;

--so we can see that quarter -->
-->4	70638277656	101909692480018.39
-->3	62141176425	88233138211669.73
-->2	54659969115	82024231029539.02
--are higher by transaction count.

--and its reverse for lower transaction count.

-- Hence the 4th Quarter are always higher in transaction count wise as well as 
--transaction amount wise

-------------------------------------------------------------------------------

--No.3 Analysis

--First Lets Check what are all the payment types and how many?

SELECT DISTINCT "Transaction_type"
FROM aggregated_transaction;

--So we 5 types of payments in total

--	1-->"Recharge & bill payments"
--	2-->"Others"
--	3-->"Financial Services"
--	4-->"Merchant payments"
--	5-->"Peer-to-peer payments"

--Lets groupby transaction types and seeing transaction count and transaction amount

-- lets order it by transaction_amount and see

SELECT "Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "Transaction_type"
ORDER BY total_transaction_amount DESC;

--so we can see the transaction type
-->"Peer-to-peer payments" 	  amount-->266527358971212.5 	count-->85032446653
-->"Merchant payments"	   	  amount-->65339877074733.14 	count-->130238755487
-->"Recharge & bill payments" amount-->13338759360277.838 		count-->19596755603

--are having higher transaction amount

--And its reverse for lower the trancation amount

-- lets order it by transaction_amount and see

SELECT "Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "Transaction_type"
ORDER BY total_transaction_count DESC;

--so we can see the transaction types

-->"Merchant payments"	   	  amount-->65339877074733.14 	count-->130238755487
-->"Peer-to-peer payments" 	  amount-->266527358971212.5 	count-->85032446653
-->"Recharge & bill payments" amount-->13338759360277.838 		count-->19596755603

--are having higher transaction count

--And its reverse for lower the trancation count

-------------------------------------------------------------------------------

--No.4 Query

--Now lets (groupby states and payment category) and compare that with sum of transaction count 
--and sum of transaction amount


SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_amount DESC
LIMIT 3;

--so we can see that state-->
-->"telangana"	"Peer-to-peer payments"	count-->9564940509	amount-->33367578287355.734
-->"karnataka"	"Peer-to-peer payments"	count-->10092132378	amount-->31322457204362.15
-->"maharashtra" "Peer-to-peer payments"count-->10066546779	amount-->29931537860773.88

--> the peer to peer payments values are higher in these states

SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_amount
LIMIT 3;

--so we can see that state-->
-->"lakshadweep"	"Others"			  count-->979	amount-->1608211.2038720455
-->"lakshadweep"	"Financial Services"  count-->1624	amount-->2003873.5340129058
-->"mizoram"		"Others"			  count-->30824	amount-->26356250.558611058

-->payments values are much lower in these states 

--Now lets check through the sum of transaction count

SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_count DESC
LIMIT 3;

-->so here we can see that states-->
-->"maharashtra"	"Merchant payments"	count-->19290166803	amount-->8677544010665.549
-->"karnataka"	"Merchant payments"		count-->18851053952	amount-->8046394678981.805
-->"telangana"	"Merchant payments"		count-->14953817184	amount-->6753346861006.314

--interesting the same states for higher transaction amount but here 
--it is for the payment type Merchant payments

--So , The higher transaction count in merchant payments indicates strong merchant adoption and 
--frequent usage in states like Maharashtra, Karnataka, Telangana.
--Although, peer to peer payemnts contribute higher transaction value, merchant payments reflect
--consistent dat_to_day economic activity


SELECT "State","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Transaction_type"
ORDER BY total_transaction_count 
LIMIT 3;

-- so here comes the same states which is having lower transaction amount

--> So States such as Lakshadweep an Mizoram consistently shows the lowest transaction count and 
--transaction amount across payment categories. This indicates lower digital payment adoption
--which may be attributed to smaller population size,limited merchant presence and lower
--commercial activity . Unlike high - performing states such as Maharashtra, Karnataka, Telangana
--where transaction dominance varies by category , these states exhibit uniformly low usage 
--across all categories.

--Business Decision
-- This highlights the need for region - specific strategies as growth drivers in high-adoption states
--differ significantly from those in low- adoption regions.

--Region specific strategies focusing on Digital infrastructure support,
--Merchant onboarding, awareness campaigns and small value incentives. 

--Unlike High-Adoption states where optimization ansd scale drive growth 
--these regions require foundational adoption efforts to build trust and accessibility 
--in digital payments




-------------------------------------------------------------------------------

--No.5 Query

--Now lets compare all state , quarter, transaction type with the sum oftotal_transaction_count,
--total_transaction_amount

--First lets see based on transaction count

SELECT "State","Quarter","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_count DESC
LIMIT 3;

--so we can see that states-->
-->"maharashtra"	4	"Merchant payments"	5882453352	2660337656941.3594
-->"karnataka"		4	"Merchant payments"	5572426848	2370638894552.975
-->"Marashtra"		3	"Merchant payments"	5004592742	2226585326060.8994

--Here Merchant payments peak in Q4 in high - adoption states due to festive and year-end spending.
--Indiactes strong seasonality in digital payment uasge.

SELECT "State","Quarter","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_count
LIMIT 3;

--same expected states only but with quarter changed
-->"lakshadweep"	3	"Others"	223	348173.1878503985
-->"lakshadweep"	1	"Others"	227	401747.476428433
-->"lakshadweep"	1	"Financial Services"	247	234005.32139426202


--Now lets see based on transaction amount

SELECT "State","Quarter","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_amount DESC
LIMIT 3;

--Same expected states and quarter only also with expected high peer to peer payments with 
--high transaction amount
--"telangana"	4	"Peer-to-peer payments"	2886714695	9916035006137.117
-->"karnataka"	4	"Peer-to-peer payments"	2926970377	8964097378211.73
-->"telangana"	3	"Peer-to-peer payments"	2575355846	8811770675211.814

SELECT "State","Quarter","Transaction_type",
SUM("Transaction_count") AS total_transaction_count,
SUM("Transaction_amount") AS total_transaction_amount
FROM aggregated_transaction
GROUP BY "State","Quarter","Transaction_type"
ORDER BY total_transaction_amount 
LIMIT 3;

--here to the same expected states and quarter and transaction types

-->"lakshadweep"	1	"Financial Services"	247	234005.32139426202
-->"lakshadweep"	3	"Others"	223	348173.1878503985
-->"lakshadweep"	2	"Financial Services"	318	368916.8536804439

-->So based on the Quarter of high abodted states and quarter of low adopted states what 
--i can say is -->

--Business insights-->
-->While high - aboption states such as Maharastraa and Karnataka exhibit a strong surge in merchant payments
-->during Q3 and Q4 whereas low adoption regions like Lakshadweep  and Mizoram show minimal transaction
--activity and do not experience a similar seasonal uplift. This suggects that seasonal 
--demand alone is insufficient without foundational digital payments adoption . 
--Initializing targeted awareness , merchant onboarding, and incentive programs during late Q2 or 
--early Q3 can help low adoption states participate in the Q4 peak thereby improviong 
--overall adoption and usage.


--Overall Business Decision from my insights 

--Seasonality amplifies existing adoption , it does not create it. FOundational onboarding
--must happen before the peak seasonfor seasonal effects to be effective.


------------------DONE---------------------
