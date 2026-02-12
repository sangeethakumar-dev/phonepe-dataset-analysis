import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
import db2

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from utils.ui import load_phonepe_theme

load_phonepe_theme()

st.set_page_config(layout="wide")

# ---------- GET SELECTED BUSINESS CASE ----------

business_case = st.session_state.get("2) Device Dominance and User Engagement Analysis", "Business Case Two")

st.title("2) Device Dominance and User Engagement Analysis")

st.subheader("Business Scenario")


st.markdown(
    """
    <div style="
        text-align: left;
        max-width: 900px;
        font-size: 16px;
        line-height: 1.6;
    ">
    PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands. The data reveals the number of registered users and app opens, segmented by device brands, regions, and time periods. However, trends in device usage vary significantly across regions, and some devices are disproportionately underutilized despite high registration numbers.

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
        "1) Overall Brand-wise User Base and Engagement Analysis",
        "2) State-wise Device Adoption Trends",
        "3) Quarterly Device Performance",
        "4) State-wise User Engagement Overview",
        "5) Multi-Dimensional Device Usage Analysis"
])
    

# ---------- Analysis 1 : Overall Brand-wise User Base and Engagement Analysis ----------

#This analysis evaluates overall device brand dominance by aggregating user base and app engagement across all states and reporting periods. 
#It highlights the brands with the strongest market presence and user interaction levels.

#Chart 1

with left_col  :

    if analysis == "1) Overall Brand-wise User Base and Engagement Analysis":
        
        st.header("1) Overall Brand-wise User Base and Engagement Analysis")
        st.markdown("This analysis evaluates overall device brand dominance by aggregating user base and app engagement across all states and reporting periods. It highlights the brands with the strongest market presence and user interaction levels.")

        df = db2.fetch_registered_users_count_device_higher()

        st.subheader("Top 5 Device Brands by Total User Base :")

        fig1 = px.pie(
            df,
            names="Device_Brand",
            values="total_brand_users",
            hole=0.5
            )

        fig1.update_traces(textinfo="percent+label")

        st.plotly_chart(fig1, use_container_width=True, key="brand_users_overall")

#Chart 2 

with left_col:
        if analysis == "1) Overall Brand-wise User Base and Engagement Analysis":
            df = db2.fetch_app_usage_count_device_higher()

            st.subheader("Top 5 Device Brands by Overall User Engagement :")

            fig2 = px.treemap(
            df,
            path=["Device_Brand"],
            values="engagement_score"
            )

            st.plotly_chart(fig2, use_container_width=True, key="brand_engagement_overall")

#--------------Analysis 2 : State-wise Device Adoption Trends ---------------------------------
 
#Examines registered users and app opens by device brand across states.
#Highlights regional preferences and device penetration patterns.


#Chart 1
with left_col:
    if analysis == "2) State-wise Device Adoption Trends":
        df = db2.fetch_device_count_state_higher()
        st.header("State-wise Device Adoption Trends")
        st.markdown("Examines registered users and app opens by device brand across states.Highlights regional preferences and device penetration patterns.")

        fig1 = px.funnel(
        df,
        x="total_device_count",
        y="Device_Brand",
        color="State",
        title="Top 5 Device Brands by Total Device Count"
        )

        fig1.update_layout(height=500)
        st.plotly_chart(fig1, use_container_width=True,key="device_count")

#Chart 2

with left_col:
    if analysis == "2) State-wise Device Adoption Trends":
        df = db2.fetch_device_count_state_lower()

        fig2 = px.pie(
        df,
        names="Device_Brand",
        values="total_device_count",
        hole=0.5,
        color="State",
        title="Bottom 3 Device Brands by Device Count"
        )

        fig2.update_traces(textinfo="percent+label")
        fig2.update_layout(height=500)

        st.plotly_chart(fig2, use_container_width=True,key="bottom_device_count")

#Chart 3
with left_col:
    if analysis == "2) State-wise Device Adoption Trends":
        df = db2.fetch_app_opens_state_higher()

        fig3 = px.scatter(
        df,
        x="Device_Brand",
        y="total_app_opens",
        size="total_app_opens",
        color="State",
        size_max=60,
        title="Top 5 Device Brands by Total App Opens"
        )

        fig3.update_layout(height=500)
        st.plotly_chart(fig3, use_container_width=True,key="top_app_opens")

#Chart 4
with left_col:
    if analysis == "2) State-wise Device Adoption Trends":
        df = db2.fetch_app_opens_state_lower()

        fig4 = px.sunburst(
        df,
        path=["State", "Device_Brand"],
        values="total_app_opens",
        color="total_app_opens",
        color_continuous_scale="Blues",
        title="Bottom Device Brand–State Combinations by App Opens (Non-Zero)"
        )

        fig4.update_layout(
        height=550,
        margin=dict(t=50, l=0, r=0, b=0)
        )
        st.plotly_chart(fig4, use_container_width=True)


#--------------Analysis 3 : Quarterly Device Performance Analysis ---------------------------------
 
#Evaluates how device brands perform across different quarters.
#Identifies seasonal or time-based growth trends in user registrations and app activity

#Chart 1
with left_col:
    if analysis == "3) Quarterly Device Performance":
        df = db2.fetch_registered_users_count_device_quarter_higher()
        st.header(" Quarterly Device Performance")
        st.markdown("Evaluates how device brands perform across different quarters.Identifies seasonal or time-based growth trends in user registrations and app activity")
        import plotly.express as px

        fig = px.treemap(
        df,
        path=["Device_Brand", "Quarter"],
        values="total_device_count",
        color="total_app_opens",
        title="Quarterly Device Penetration Leadership",
        )

        st.plotly_chart(fig, use_container_width=True)

#Chart 2
with left_col:
    if analysis == "3) Quarterly Device Performance":
        df["Brand_Quarter"] = df["Device_Brand"] + " - Q" + df["Quarter"].astype(str)

        fig = px.pie(
        df.head(10),
        names="Brand_Quarter",
        values="total_device_count",
        hole=0.5,
        title="Low Penetration Brand-Quarter Combinations"
        )

        st.plotly_chart(fig, use_container_width=True)

#Chart 3

with left_col:
    if analysis == "3) Quarterly Device Performance":
        df=db2.fetch_app_usage_count_device_quarter_higher()
        fig = px.scatter(
        df,
        x="total_device_count",
        y="total_app_opens",
        size="total_app_opens",
        color="Device_Brand",
        hover_data=["Quarter"],
        title="Quarterly App Engagement Dominance"
        )

        st.plotly_chart(fig, use_container_width=True)

#Chart 4

with left_col:
    if analysis == "3) Quarterly Device Performance":
        df=db2.fetch_app_usage_count_device_quarter_lower()
        fig = px.sunburst(
        df,
        path=["Device_Brand", "Quarter"],
        values="total_app_opens",
        title="Quarterly App Engagement Underperformance"
        )

        st.plotly_chart(fig, use_container_width=True)

#--------------Analysis 4 : State-wise User Registration & App Activity Overviews ---------------------------------

#Provides a comparative view of user registrations and app opens across states.
#Helps identify high-growth and high-engagement regions.


#Chart 1
with left_col:
    if analysis == "4) State-wise User Engagement Overview":
        
        st.header(" Quarterly Device Performance")
        st.markdown("#Provides a comparative view of user registrations and app opens across states.")

        df = db2.fetch_registered_users_count_state_lower()

        fig = px.treemap(
        df,
        path=["State"],
        values="registered_users_count",
        title="State-wise Maximum Registered Users",
        color="registered_users_count",
        color_continuous_scale="purples"
        )

        st.plotly_chart(fig, use_container_width=True)

#Chart 2
with left_col:
    if analysis == "4) State-wise User Engagement Overview":
        df=db2.fetch_app_usage_count_state_higher()
        fig2 = px.treemap(
        df,
        path=["State"],
        values="app_usage_count",
        title="State-wise Maximum App Opens",
        color="app_usage_count",
        color_continuous_scale="blues"
)

        st.plotly_chart(fig2, use_container_width=True)

      
#--------------Analysis 5: Multi-Dimensional Device Usage Analysis ---------------------------------

#Analyzes device brand performance across states and quarters simultaneously.
#Offers deep insights into geographic and temporal usage behavior patterns.

#Chart 1

with left_col:
    if analysis == "5) Multi-Dimensional Device Usage Analysis":
        
        st.header(" Quarterly Device Performance")
        st.markdown("Analyzes device brand performance across states and quarters simultaneously.Offers deep insights into geographic and temporal usage behavior patterns.")

        df=db2.fetch_registered_users_count_state_device_quarter_higher()

        fig = px.sunburst(
        df,
        path=["State", "Device_Brand", "Quarter"],
        values="total_device_count",
        color="total_device_count",
        color_continuous_scale="purples",
        title="Multi-Dimensional Device Brand Dominance"
        )

        st.plotly_chart(fig, use_container_width=True)

