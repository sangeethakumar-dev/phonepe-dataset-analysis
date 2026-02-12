import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
import db1

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.ui import load_phonepe_theme

load_phonepe_theme()

st.set_page_config(layout="wide")

# ---------- GET SELECTED BUSINESS CASE ----------

business_case = st.session_state.get("1. Decoding Transaction Dynamics on PhonePe", "Business Case One")

st.title("1. Decoding Transaction Dynamics on PhonePe")

st.subheader("Business Scenario")

st.markdown(
    """
    <div style="
        text-align: left;
        max-width: 900px;
        font-size: 16px;
        line-height: 1.6;
    ">
    PhonePe, a leading digital payments platform, has recently identified significant
    variations in transaction behavior across states, quarters, and payment categories.
    While some regions and transaction types demonstrate consistent growth, others show
    stagnation or decline. The leadership team seeks a deeper understanding of these
    patterns to drive targeted business strategies.
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
        [
            "Select",
            "1)State-wise Transaction Summary",
            "2)Quarter-wise Transaction Summary",
            "3)Payment Category Analysis",
            "4)State-wise Payment Category Performance Analysis",
            "5)State-Quarter Transaction Comparison"
        ]
    )

# ---------- Analysis 1 : State-wise Transaction Summary ----------


#Chart 1

with left_col:
    
    if analysis == "1)State-wise Transaction Summary":
        df = db1.fetch_total_transaction_amount_higher_state()
        st.header("State-wise Transaction Summary")
        st.markdown("Analyze state-wise transaction dynamics by aggregating total transaction count and total transaction amount to identify regional usage patterns.")
        
        fig = px.bar(
            df,
            x="total_transaction_amount",
            y="State",
            orientation="h",
            title="1)Top Performing States by Transaction Amount",
            color_discrete_sequence=["#4D0A94"]
        )

        st.plotly_chart(fig, use_container_width=True,key="high_amount")

#Chart 2

with left_col:
    if analysis == "1)State-wise Transaction Summary":
        df = db1.fetch_total_transaction_amount_lower_state()
        fig = px.bar(
            df,
            x="total_transaction_amount",
            y="State",
            orientation="h",
            title="2)Underperforming States by Transaction Amount",
            color_discrete_sequence=["#804CB8"]
        )

        st.plotly_chart(fig, use_container_width=True,key="low_amount")

#Chart 3

with left_col:
    if analysis == "1)State-wise Transaction Summary":
        df = db1.fetch_total_transaction_count_higher_state()

        fig = px.bar(
            df,
            x="total_transaction_count",
            y="State",
            orientation="h",
            title="3)Most Active States by Transaction Count",
            color_discrete_sequence=["#2d145f"]
        )

        st.plotly_chart(fig, use_container_width=True,key="high_count")

#Chart 4

with left_col:
    if analysis == "1)State-wise Transaction Summary":
        df = db1.fetch_total_transaction_count_lower_state()

        fig = px.bar(
            df,
            x="total_transaction_count",
            y="State",
            orientation="h",
            title="4)Least Active States by Transaction Count",
            color_discrete_sequence=["#6B4BA5"]
        )

        st.plotly_chart(fig, use_container_width=True,key="low_count")



# ---------- Analysis 2 : Quarter-wise Transaction Summary ----------


with left_col:
    if analysis == "2)Quarter-wise Transaction Summary":
        df =db1.fetch_total_transaction_amount_higher_quarter()
        st.header("Quarter-wise Transaction Summary")
        st.markdown("This analysis aggregates total transaction count and transaction amount across all quarters")
        fig = px.bar(
            df,
            x="total_transaction_amount",
            y="Quarter",
            orientation="h",
            title="1) Quarterly Transaction Amount Summary",
            color_discrete_sequence=["#5F259F"]
        )

        st.plotly_chart(fig, width="stretch",key="high_amount_quar")


with left_col:
    if analysis == "2)Quarter-wise Transaction Summary":
        df =db1.fetch_total_transaction_count_higher_quarter()

        fig = px.bar(
            df,
            x="total_transaction_count",
            y="Quarter",
            orientation="h",
            title="2)Quarterly Transaction Count Summary  ",
            color_discrete_sequence=["#5F259F"]
        )

        st.plotly_chart(fig, width="stretch",key="high_count_quar")

        

#--------------Analysis 3 : Payment Category Analysis ---------------------------------

#This analysis aggregates transactions by payment type to evaluate overall transaction volume and value.

#Chart 1

with left_col:
    if analysis == "3)Payment Category Analysis":
        st.header("Payment Category Analysis")
        st.markdown("This analysis aggregates transactions by payment type to evaluate overall transaction volume and value.")
        df =db1.fetch_total_transaction_amount_transaction_type()

        fig = px.bar(
            df,
            x="total_transaction_amount",
            y="Transaction_type",
            orientation="h",
            title="1) Transaction Type by Amount  ",
            color_discrete_sequence=["#5F259F"]
        )

        st.plotly_chart(fig, width="stretch", key="amount_pay")
        

with left_col:
    if analysis == "3)Payment Category Analysis":
        df =db1.fetch_total_transaction_count_transaction_type()

        fig = px.bar(
            df,
            x="total_transaction_count",
            y="Transaction_type",
            orientation="h",
            title="2) Transaction Type by Count  ",
            color_discrete_sequence=["#5F259F"]
        )

        st.plotly_chart(fig, width="stretch",key="count_pay")


#--------------Analysis 4 : State-wise Payment Category Performance Analysis ---------------------------------


#This analysis examines how different payment categories perform across states using transaction volume and transaction value.
#It helps identify dominant payment modes and underperforming regions for strategic insights.

#Chart 1

with left_col:
    df=None
    fig=None

    if analysis == "4)State-wise Payment Category Performance Analysis":
        st.header("State-wise Payment Category Performance Analysis")
        st.markdown("""This analysis examines how different payment categories perform across states using transaction volume and transaction value.
It helps identify dominant payment modes and underperforming regions for strategic insights.
                    """)
        df =db1.fetch_total_transaction_amount_state_transaction_type_higher()

        fig = px.bar(
        df,
        x="State",
        y="total_transaction_amount",
        color="Transaction_type",
        barmode="stack",
        title="1) Top Performing States by Transaction Amount (Payment Category-wise)"
        )

        fig.update_layout(
        height=700,  
        xaxis_tickangle=45,  
        xaxis_title="State",
        yaxis_title="Total Transaction Amount",
        legend_title="Payment Category",
        margin=dict(l=40, r=40, t=80, b=180), 
        bargap=0.15,
        )
if fig is not None:
    st.plotly_chart(fig, width="stretch",key="high_amount_state")

#Chart  2

with left_col:
    if analysis == "4)State-wise Payment Category Performance Analysis":
        df =db1.fetch_total_transaction_amount_state_transaction_type_lower()

        fig = px.bar(
            df,
            x="State",
            y="total_transaction_amount",
            color="Transaction_type",
            barmode="stack",
            title="2) Low Performing States by Transaction Amount(Payment Category-wise)"
            )

        fig.update_layout(
        height=700,  
        xaxis_tickangle=45,  
        xaxis_title="State",
        yaxis_title="Total Transaction Amount",
        legend_title="Payment Category",
        margin=dict(l=40, r=40, t=80, b=180), 
        bargap=0.15,
        )
if fig is not None:
    st.plotly_chart(fig, width="stretch",key="low_amount_state")


#Chart  3

with left_col:
    if analysis == "4)State-wise Payment Category Performance Analysis":
        df =db1.fetch_total_transaction_count_state_transaction_type_higher()

        fig = px.bar(
        df,
        x="State",
        y="total_transaction_count",
        color="Transaction_type",
        barmode="stack",
        title="3) Top Performing States by Transaction Count(Payment Category-wise)"
        )

        fig.update_layout(
        height=700,  
        xaxis_tickangle=45,  
        xaxis_title="State",
        yaxis_title="Total Transaction Count",
        legend_title="Payment Category",
        margin=dict(l=40, r=40, t=80, b=180), 
        bargap=0.15,
        )

if fig is not None:
    st.plotly_chart(fig, width="stretch",key="high_count_state")


#Chart  4

with left_col:
    if analysis == "4)State-wise Payment Category Performance Analysis":
        df =db1.fetch_total_transaction_count_state_transaction_type_lower()

        fig = px.bar(
        df,
        x="State",
        y="total_transaction_count",
        color="Transaction_type",
        barmode="stack",
        title="4) Low Performing States by Transaction Count(Payment Category-wise)"
        )

        fig.update_layout(
        height=700,  
        xaxis_tickangle=45,  
        xaxis_title="State",
        yaxis_title="Total Transaction Count",
        legend_title="Payment Category",
        margin=dict(l=40, r=40, t=80, b=180), 
        bargap=0.15,
        )

if fig is not None:
    st.plotly_chart(fig, width="stretch",key="low_count_state")

#--------------Analysis 5 : State–Quarter Transaction Comparison ---------------------------------

#This analysis compares transaction count and transaction amount across states, quarters, and transaction types.
#It helps understand digital payment distribution and performance patterns across different regions and periods.

# --------------Analysis 5 : State–Quarter Transaction Comparison --------------

if analysis == "5)State-Quarter Transaction Comparison":

    st.header("State-Quarter Transaction Comparison")

    st.markdown("""
    This analysis compares transaction count and transaction amount 
    across states, quarters, and transaction types.
    """)

#Chart 1

    df = db1.fetch_total_transaction_count_state_transaction_type_quarter_higher()

    fig = px.bar(
        df,
        x="State",
        y="total_transaction_count", 
        color="Quarter",
        barmode="group",
        title="1)Top Performing States by Transaction Count Across Quarters"
    )

    st.plotly_chart(fig, use_container_width=True)

#Chart 2
    df = db1.fetch_total_transaction_count_state_transaction_type_quarter_lower()

    fig = px.bar(
        df,
        x="State",
        y="total_transaction_count",
        color="Quarter",
        barmode="group",
        title="2)Low Performing States by Transaction Count Across Quarters"
    )

    st.plotly_chart(fig, use_container_width=True)

#Chart 3

    df = db1.fetch_total_transaction_amount_state_transaction_type_quarter_higher()

    fig = px.bar(
        df,
        x="State",
        y="total_transaction_amount",
        color="Quarter",
        barmode="group",
        title="3)Top Performing States by Transaction Amount Across Quarters"
    )

    st.plotly_chart(fig, use_container_width=True)

#Chart 4

    df = db1    .fetch_total_transaction_amount_state_transaction_type_quarter_lower()

    fig = px.bar(
        df,
        x="State",
        y="total_transaction_amount",
        color="Quarter",
        barmode="group",
        title="4) Low Performing States by Transaction Amount Across Quarters"
    )

    st.plotly_chart(fig, use_container_width=True)


