import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
import db4

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.ui import load_phonepe_theme

load_phonepe_theme()

st.set_page_config(layout="wide")

# ---------- GET SELECTED BUSINESS CASE ----------

business_case = st.session_state.get("4) Transaction Analysis Across States and Districts", "Business Case Two")

st.title("4) Transaction Analysis Across States and Districts")

st.subheader("Business Scenario")


st.markdown(
    """
    <div style="
        text-align: left;
        max-width: 900px;
        font-size: 16px;
        line-height: 1.6;
    ">
    "PhonePe is conducting an analysis of transaction data to identify the top-performing states, districts, and pin codes in terms of transaction volume and value. This analysis will help understand user engagement patterns and identify key areas for targeted marketing efforts."
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
        "1) State-Level Transaction Performance Overview",
        "2) District-Level Transaction Performance Analysis",
        "3) PIN Code-Level Transaction Concentration Study",
        "4) State-District-Year Transaction Trend Analysis",
        "5) Quarterly Transaction Performance by Region"
])
    
# ---------- Analysis 1 : State-Level Transaction Performance Overview ----------

#Analyzes total transaction count and total transaction amount aggregated at the state level.
#Identifies the highest-performing states contributing maximum transaction volume and value.

#Chart 1

with left_col  :

    if analysis == "1) State-Level Transaction Performance Overview":
        
        st.header("State-Level Transaction Performance Overview")
        st.markdown("#Analyzes total transaction count and total transaction amount aggregated at the state level.Identifies the highest-performing states contributing maximum transaction volume and value.")
        import plotly.graph_objects as go

        df = db4.fetch_total_amount_state_higher()

        fig = go.Figure()

        # Bar for Total Amount
        fig.add_trace(
        go.Bar(
        x=df["State"],
        y=df["total_amount"],
        name="Total Transaction Amount",
        yaxis="y1"
        )
        )

        # Line for Total Count
        fig.add_trace(
        go.Scatter(
        x=df["State"],
        y=df["total_count"],
        name="Total Transaction Count",
        mode="lines+markers",
        yaxis="y2"
        )
        )

        fig.update_layout(
        title="Top 3 States by Transaction Value and Volume",
        xaxis=dict(title="State"),
        yaxis=dict(
        title="Total Transaction Amount",
        showgrid=False
        ),
        yaxis2=dict(
        title="Total Transaction Count",
        overlaying="y",
        side="right"
        ),
        legend=dict(x=0.01, y=0.99),
        template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)



# ---------- Analysis 2 : District-Level Transaction Performance Analysis ----------

#Evaluates transaction count and total transaction amount at the district level.
#Highlights top-performing districts driving regional transaction growth.

#Chart 1

with left_col  :

    if analysis == "2) District-Level Transaction Performance Analysis":
        
        st.header("District-Level Transaction Performance Analysis")
        st.markdown("Evaluates transaction count and total transaction amount at the district level.Highlights top-performing districts driving regional transaction growth.")
        import plotly.express as px

        df = db4.fetch_total_amount_district_higher()

        fig = px.scatter(
        df,
        x="total_count",
        y="total_amount",
        size="total_amount",
        color="District",
        hover_name="District",
        size_max=80,
        title="Top 3 Districts by Transaction Value and Activity Intensity",
        labels={
        "total_count": "Total Transaction Count",
        "total_amount": "Total Transaction Amount"
        },
        template="plotly_white"
        )

        fig.update_traces(marker=dict(opacity=0.7))

        fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        legend_title="District"
        )

        st.plotly_chart(fig, use_container_width=True)



# ---------- Analysis 3 : PIN Code-Level Transaction Concentration Study ----------

#Aggregates transaction count and amount by PIN code to identify localized transaction hotspots.
#Reveals high-activity micro-markets contributing significantly to overall transactions.

#Chart 1

with left_col  :

    if analysis == "3) PIN Code-Level Transaction Concentration Study":
        
        st.header("PIN Code-Level Transaction Concentration Study")
        st.markdown("Aggregates transaction count and amount by PIN code to identify localized transaction hotspots.Reveals high-activity micro-markets contributing significantly to overall transactions.")
        import plotly.express as px

        df = db4.fetch_total_amount_pincode_higher()

        fig = px.pie(
        df,
        names="Pincode",
        values="total_amount",
        hole=0.55,   # makes it donut
        title="Contribution of Top 3 PIN Codes to Total Transaction Value",
        template="plotly_white"
        )

        fig.update_traces(
        textinfo="percent+label",
        pull=[0.05, 0, 0]  # slightly highlight top pincode
        )

        fig.update_layout(
        showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)



# ---------- Analysis 4 : State-District-Year Transaction Trend Analysis ----------

#Examines yearly transaction performance across state and district combinations.
#Identifies which state-district pairs recorded peak transaction volume and value in specific years.

#Chart 1

with left_col  :

    if analysis == "4) State-District-Year Transaction Trend Analysis":
        
        st.header("State-District-Year Transaction Trend Analysis")
        st.markdown("Examines yearly transaction performance across state and district combinations.Identifies which state-district pairs recorded peak transaction volume and value in specific years.")
        import plotly.express as px

        df = db4.fetch_total_count_state_district_year_higher()

        fig = px.treemap(
        df,
        path=["State", "District", "Year"],
        values="total_amount",
        color="total_amount",
        title="Top State–District–Year Combinations by Transaction Value",
        template="plotly_white"
        )

        fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25)
        )

        st.plotly_chart(fig, use_container_width=True)



# ---------- Analysis 5 : Quarterly Transaction Performance by Region ----------

#Analyzes transaction count and amount across state, district, year, and quarter dimensions.
#Provides insights into seasonal and quarterly transaction trends at the regional level.

#Chart 1

with left_col  :

    if analysis == "5) Quarterly Transaction Performance by Region":
        
        st.header("Quarterly Transaction Performance by Region")
        st.markdown("Analyzes transaction count and amount across state, district, year, and quarter dimensions.Provides insights into seasonal and quarterly transaction trends at the regional level.")
        import plotly.express as px

        df = db4.fetch_total_count_state_district_year_quarter_higher()

# Create a combined label for clarity
        df["Region"] = df["State"] + " - " + df["District"]

        fig = px.density_heatmap(
        df,
        x="Quarter",
        y="Year",
        z="total_amount",
        facet_row="Region",
        color_continuous_scale="Purples",
        title="Peak Quarterly Transaction Intensity Across Top State–District Combinations",
        labels={
        "total_amount": "Total Transaction Amount"
        },
        template="plotly_white"
        )

        fig.update_layout(
        height=700
        )

        st.plotly_chart(fig, use_container_width=True)





