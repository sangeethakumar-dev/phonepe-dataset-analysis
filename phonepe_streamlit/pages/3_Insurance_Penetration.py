import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
import db3

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.ui import load_phonepe_theme

load_phonepe_theme()

st.set_page_config(layout="wide")

# ---------- GET SELECTED BUSINESS CASE ----------

business_case = st.session_state.get("3) Insurance Penetration and Growth Potential Analysis", "Business Case Two")

st.title("3) Insurance Penetration and Growth Potential Analysis")

st.subheader("Business Scenario")


st.markdown(
    """
    <div style="
        text-align: left;
        max-width: 900px;
        font-size: 16px;
        line-height: 1.6;
    ">
    "PhonePe has ventured into the insurance domain, providing users with options to secure various policies. With increasing transactions in this segment, the company seeks to analyze its growth trajectory and identify untapped opportunities for insurance adoption at the state level. This data will help prioritize regions for marketing efforts and partnerships with insurers."
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.subheader("Select Analysis")

left_col, right_col = st.columns([1,1])

# ---------- ANALYSIS DROPDOWN ----------



with left_col:
    analysis = st.selectbox(
        "",
        ["Select",
        "1) State-wise Insurance Adoption Performance",
        "2) Yearly Insurance Growth Trend Analysis",
        "3) Quarterly Insurance Demand Pattern",
        "4) State-wise Insurance Volume Concentration",
        "5) State-Year Insurance Growth Comparison"
])
    

# ---------- Analysis 1 : State-wise Insurance Adoption Performance ----------

#Analyzes average transaction amount and transaction count across states to identify high-performing and low-performing insurance markets.
#Highlights regional disparities in insurance penetration and adoption intensity.

#Chart 1

with left_col  :

    if analysis == "1) State-wise Insurance Adoption Performance":
        
        st.header("State-wise Insurance Adoption Performance")
        st.markdown("Analyzes average transaction amount and transaction count across states to identify high-performing and low-performing insurance markets.Highlights regional disparities in insurance penetration and adoption intensity.")

        df_high = db3.fetch_avg_insurance_state_higher()

        fig_high = px.treemap(
        df_high,
        path=["State"],
        values="average_insurance_value",
        color="average_insurance_value",
        color_continuous_scale="Blues",
        title="State-wise Distribution of Highest Average Insurance Value"
        )

        fig_high.update_layout(title_x=0.25)

        st.plotly_chart(fig_high, use_container_width=True)

#Chart 2

with left_col  :

    if analysis == "1) State-wise Insurance Adoption Performance":
        df_low = db3.fetch_avg_insurance_state_lower()

        fig_low = px.pie(
        df_low,
        names="State",
        values="average_insurance_value",
        hole=0.5,
        title="Proportional Contribution of States with Lowest Average Insurance Value"
        )

        fig_low.update_traces(textinfo="percent+label")

        fig_low.update_layout(title_x=0.2)

        st.plotly_chart(fig_low, use_container_width=True)

        

# ---------- Analysis 2 : Yearly Insurance Growth Trend Analysis ----------

#Evaluates yearly average transaction amount and transaction count to understand insurance adoption trends over time.
#Identifies peak growth years and periods of slower market expansion.

#Chart 1

with left_col  :

    if analysis == "2) Yearly Insurance Growth Trend Analysis":
        st.header("Yearly Insurance Growth Trend Analysis ")
        st.markdown("Evaluates yearly average transaction amount and transaction count to understand insurance adoption trends over time.Identifies peak growth years and periods of slower market expansion.")
        df_year_high = db3.fetch_avg_insurance_year_higher()

       
        df_year_high = df_year_high.sort_values(by="Year")

        fig_year_high = px.area(
        df_year_high,
        x="Year",
        y="average_insurance_value",
        markers=True,
        title="Peak Years in Average Insurance Transaction Value"
        )

        fig_year_high.update_layout(
        xaxis_title="Year",
        yaxis_title="Average Insurance Value",
        title_x=0.25
        )

        st.plotly_chart(fig_year_high, use_container_width=True)

#Chart 2

with left_col  :

    if analysis == "2) Yearly Insurance Growth Trend Analysis":
        df_year_low = db3.fetch_avg_insurance_year_lower()

        df_year_low = df_year_low.sort_values(by="Year")

        fig_year_low = px.scatter(
        df_year_low,
        x="Year",
        y="average_insurance_value",
        size="average_insurance_value",
        title="Low Performing Years in Insurance Transaction Value"
        )

        fig_year_low.update_layout(
        xaxis_title="Year",
        yaxis_title="Average Insurance Value",
        title_x=0.2
        )

        st.plotly_chart(fig_year_low, use_container_width=True)




# ---------- Analysis 3 :  Quarterly Insurance Demand Pattern ----------

#Examines quarter-wise average transaction metrics to detect seasonal insurance purchasing behavior.
#Reveals high-activity quarters and short-term adoption fluctuations.


#Chart 1


with left_col  :

    if analysis == "3) Quarterly Insurance Demand Pattern":
        st.header("Quarterly Insurance Demand Pattern")
        st.markdown("#Examines quarter-wise average transaction metrics to detect seasonal insurance purchasing behavior.Reveals high-activity quarters and short-term adoption fluctuations.")
        import plotly.express as px
        import streamlit as st
        import pandas as pd

        df_quarter_high = db3.fetch_avg_insurance_quarter_higher()

        df_quarter_high["Quarter"] = df_quarter_high["Quarter"].astype(int).astype(str)

        df_quarter_high["Quarter"] = "Q" + df_quarter_high["Quarter"]

        # Now create bar chart
        fig = px.bar(
        df_quarter_high,
        x="Quarter",
        y="average_insurance_value",
        text="average_insurance_value",
        title="Quarter-wise Average Insurance Transaction Value"
        )

        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

        fig.update_layout(
        xaxis_title="Quarter",
        yaxis_title="Average Insurance Value",
        xaxis=dict(type="category"),   
        title_x=0.25
        )

        st.plotly_chart(fig, use_container_width=True)

#Chart 2

with left_col  :

    if analysis == "3) Quarterly Insurance Demand Pattern":
        import plotly.express as px

        df_state_low = db3.fetch_avg_insurance_quarter_lower()

        fig_funnel = px.funnel(
        df_state_low,
        x="total_transaction_count",
        y="Quarter",
        title="States with Lowest Insurance Transaction Volume"
        )

        fig_funnel.update_layout(
        xaxis_title="Total Transaction Count",
        yaxis_title="Quarter",
        title_x=0.25
        )

        st.plotly_chart(fig_funnel, use_container_width=True)


# ---------- Analysis 4 :  State-wise Insurance Volume Concentration ----------

#Aggregates total transaction count by state to determine overall insurance volume distribution.
#Identifies dominant markets and underpenetrated regions based on total policy purchases.

#Chart 1

with left_col  :

    if analysis == "4) State-wise Insurance Volume Concentration":
        st.header("State-wise Insurance Volume Concentration")
        st.markdown("Aggregates total transaction count by state to determine overall insurance volume distribution.Identifies dominant markets and underpenetrated regions based on total policy purchases.")
        import plotly.express as px
        import streamlit as st
        from db3 import fetch_total_transaction_count_state_higher

        def show_top5_insurance_transactions():

            df = fetch_total_transaction_count_state_higher()

            fig = px.pie(
            df,
            names="State",
            values="total_transaction_count",
            hole=0.5,  # Makes it donut
            title="Contribution of Top 5 States to Total Insurance Transactions"
            )

            fig.update_traces(textinfo='percent+label')

            fig.update_layout(
            title_x=0.25
            )

            st.plotly_chart(fig, use_container_width=True)
        show_top5_insurance_transactions()

#Chart 2

with left_col  :

    if analysis == "4) State-wise Insurance Volume Concentration":
        import plotly.express as px

        def show_bottom5_insurance_transactions():

            df = db3.fetch_total_transaction_count_state_lower()

            fig = px.pie(
            df,
            names="State",
            values="total_transaction_count",
            hole=0.5,
            title="Contribution of Bottom 5 States to Total Insurance Transactions"
            )

            fig.update_traces(textinfo='percent+label')

            fig.update_layout(
            title_x=0.25
            )

            st.plotly_chart(fig, use_container_width=True)

        show_bottom5_insurance_transactions()


# ---------- Analysis 5 :  State-Year Insurance Growth Comparison ----------

#Analyzes transaction count growth across states over different years to assess expansion patterns.
#Highlights consistently growing states and regions with declining or stagnant adoption.

#Chart 1

with left_col  :

    if analysis == "5) State-Year Insurance Growth Comparison":
        st.header(" State-Year Insurance Growth Comparison")
        st.markdown("Analyzes transaction count growth across states over different years to assess expansion patterns.Highlights consistently growing states and regions with declining or stagnant adoption.")
        import plotly.express as px

        def show_top5_state_year():

            df = db3.fetch_total_transaction_count_state_year_higher()

            fig = px.treemap(
            df,
            path=["State", "Year"],
            values="total_transaction_count",
            title="Top 5 State-Year Combinations by Insurance Transaction Volume"
            )

            fig.update_layout(title_x=0.2)

            st.plotly_chart(fig, use_container_width=True)
        show_top5_state_year()

#Chart 2

with left_col  :

    if analysis == "5) State-Year Insurance Growth Comparison":

        def show_bottom5_state_year():

            df = db3.fetch_total_transaction_count_state_year_lower()

            df["State_Year"] = df["State"] + " (" + df["Year"].astype(str) + ")"

            fig = px.funnel(
            df,
            x="total_transaction_count",
            y="State_Year",
            title="Bottom 5 State-Year Combinations by Insurance Transaction Volume"
            )

            fig.update_layout(title_x=0.2)

            st.plotly_chart(fig, use_container_width=True)

        show_bottom5_state_year()
