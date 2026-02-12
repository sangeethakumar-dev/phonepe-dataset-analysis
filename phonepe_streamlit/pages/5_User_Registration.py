import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
import db5

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.ui import load_phonepe_theme

load_phonepe_theme()

st.set_page_config(layout="wide")

# ---------- GET SELECTED BUSINESS CASE ----------

business_case = st.session_state.get("5) User Registration Analysis", "Business Case Two")

st.title("5) User Registration Analysis")

st.subheader("Business Scenario")


st.markdown(
    """
    <div style="
        text-align: left;
        max-width: 900px;
        font-size: 16px;
        line-height: 1.6;
    ">
    "PhonePe aims to conduct an analysis of user registration data to identify the top states, districts, and pin codes from which the most users registered during a specific year-quarter combination. This analysis will provide insights into user engagement patterns and highlight potential growth areas."

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
        "1) State-Level User Registration Performance Overview",
        "2) District-Level User Registration Analysis",
        "3) PIN Code-Level User Registration Concentration Study",
        "4) Quarterly User Registration Trend Analysis",
        "5) State Contribution to Total User Registration"
])
    
# ---------- Analysis 1 : State-Level User Registration Performance Overview ----------

#Evaluates total registered users aggregated at the state level to identify high-performing states.
#Highlights regional adoption patterns and leading contributors to overall user growth.1

#Chart 1

with left_col  :

    if analysis == "1) State-Level User Registration Performance Overview":
        
        st.header("State-Level User Registration Performance Overview")
        st.markdown("Evaluates total registered users aggregated at the state level to identify high-performing states.")
        
        import plotly.express as px

# Fetch data
        df = db5.fetch_total_count_state_year_quarter_higher()

# Create label for better readability
        df["State_Period"] = (
        df["State"] + " (" +
        df["Year"].astype(str) + " Q" +
        df["Quarter"].astype(str) + ")"
        )

# Vertical column chart
        fig = px.bar(
        df,
        x="State_Period",
        y="total_registered_count",
        color="State",
        text_auto=".2s",
        title="Top 3 State-Level Registration Peaks"
        )

        fig.update_layout(
        xaxis_title="State (Year & Quarter)",
        yaxis_title="Total Registered Users",
        template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)


         


# ---------- Analysis 2 : District-Level User Registration Analysis ----------

#Examines cumulative user registrations across districts to determine top-performing regions.
#Provides insights into localized growth concentration within states.

with left_col  :

    if analysis == "2) District-Level User Registration Analysis":
        st.header("State-Level Transaction Performance Overview")
        st.markdown("Examines cumulative user registrations across districts to determine top-performing regions.Provides insights into localized growth concentration within states.")
        
        import plotly.express as px

# Fetch data
        df = db5.fetch_total_count_district_year_quarter_higher()

# Create readable label
        df["District_Label"] = (
        df["District"] + " (" +
        df["Year"].astype(str) + " Q" +
        df["Quarter"].astype(str) + ")"
)

# Donut Chart
        fig = px.pie(
        df,
        names="District_Label",
        values="total_registered_count",
        hole=0.5,
        title="Top 5 Districts by User Registration Share"
        )

        fig.update_traces(textinfo="percent+label")

        fig.update_layout(template="plotly_white")

        st.plotly_chart(fig, use_container_width=True)



        

# ---------- Analysis 3 : PIN Code-Level User Registration Concentration Study ----------

#Analyzes registered users at the PIN code level to uncover high-density micro-markets.
#Reveals granular adoption trends and areas with strong user penetration.

with left_col  :

    if analysis == "3) PIN Code-Level User Registration Concentration Study":
        st.header("PIN Code-Level User Registration Concentration Study")
        st.markdown("Analyzes registered users at the PIN code level to uncover high-density micro-markets.Reveals granular adoption trends and areas with strong user penetration.")
        
        import plotly.express as px

# Fetch data
        df = db5.fetch_total_count_pincode_year_quarter_higher()

# Create readable label
        df["Pincode_Label"] = (
        df["Pincode"].astype(str) + " (" +
        df["Year"].astype(str) + " Q" +
        df["Quarter"].astype(str) + ")"
)

# Treemap
        fig = px.treemap(
        df,
        path=["Pincode_Label"],
        values="total_registered_count",
        title="Top PIN Code-Level Registration Concentration"
)

        fig.update_layout(template="plotly_white")

        st.plotly_chart(fig, use_container_width=True)



# ---------- Analysis 4 : Quarterly User Registration Trend Analysis ----------

#Tracks user registration growth over year and quarter to identify temporal trends.
#Highlights seasonal patterns and periods of accelerated user acquisition.

with left_col  :
    if analysis == "4) Quarterly User Registration Trend Analysis":
        st.header("Quarterly User Registration Trend Analysi")
        st.markdown("Tracks user registration growth over year and quarter to identify temporal trends.Highlights seasonal patterns and periods of accelerated user acquisition.")
       
        import plotly.express as px

# Fetch data
        df = db5.fetch_year_quarter_trend()

# Create proper time label
        df["Year_Quarter"] = df["Year"].astype(str) + " Q" + df["Quarter"].astype(str)

# Line chart
        fig = px.line(
        df,
        x="Year_Quarter",
        y="total_registered_count",
        markers=True,
        text="total_registered_count",
        title="Quarterly User Registration Growth Trend"
        )

# Improve readability
        fig.update_traces(textposition="top center")

        fig.update_layout(
        xaxis_title="Year & Quarter",
        yaxis_title="Total Registered Users",
        template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)


    
# ---------- Analysis 5 : State Contribution to Total User Registration----------

#Assesses each state's proportional contribution to overall registered users.
#Helps understand regional dominance and distribution of user base nationwide.

with left_col  :
    if analysis ==  "5) State Contribution to Total User Registration":
        st.header("Quarterly User Registration Trend Analysi")
        st.markdown("Assesses each state's proportional contribution to overall registered users.Helps understand regional dominance and distribution of user base nationwide.")
      
        import plotly.express as px

# Fetch data
        df = db5.fetch_total_contribution_state_higher()

# Sort properly
        df = df.sort_values(by="contribution_percentage", ascending=False)

# Vertical column chart
        fig = px.bar(
        df,
        x="State",
        y="contribution_percentage",
        text="contribution_percentage",
        title="State-wise Contribution to Total User Registration (%)"
        )

# Improve readability
        fig.update_traces(texttemplate='%{text}%', textposition='outside')

        fig.update_layout(
        xaxis_title="State",
        yaxis_title="Contribution Percentage",
        template="plotly_white",
        uniformtext_minsize=8,
        uniformtext_mode='hide'
        )

        st.plotly_chart(fig, use_container_width=True)




   