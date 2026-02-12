import streamlit as st
import pandas as pd
import plotly.express as px
import json

from pathlib import Path
import sys

import db1



ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


BASE_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = BASE_DIR / "styles" / "phonepe_theme.css"

def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(CSS_PATH)

load_css(CSS_PATH)

st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background-color: #F5F0FF !important;
}

/* SIDEBAR BACKGROUND */
[data-testid="stSidebar"] {
    background-color: #EFE7FF !important;
}

/* Remove white container */
[data-testid="stHeader"] {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="PhonePe Pulse ", layout="wide",initial_sidebar_state="collapsed")
st.title("Project Title : PhonePe Transaction Insights")
st.caption("Business Case Study Dashboard")

# ---------------- REMOVE EXTRA PADDING ----------------

st.markdown("---")

# ---------------- LOAD GEOJSON ----------------

from pathlib import Path
import json

BASE_DIR = Path(__file__).parent  # phonepe_streamlit folder
geojson_path = BASE_DIR / "india_states.geojson"

with open(geojson_path, "r", encoding="utf-8") as f:
    india_geojson = json.load(f)


all_states = [
    feature["properties"]["NAME_1"]
    for feature in india_geojson["features"]    
    ]

# ---------------- DATAFRAME ----------------


df1 = pd.DataFrame({
    "State": all_states,
    "Value": 0
    })

sample_values = {
    "Tamil Nadu": 120,
    "Karnataka": 150,
    "Maharashtra": 300,
    "Kerala": 90,
    "Telangana": 180,
    "Delhi": 200
    }

df1["Value"] = df1["State"].map(sample_values).fillna(0)

# ---------------- MAIN LAYOUT ----------------

left_col, right_col = st.columns([3,2])

# ---------------- LEFT COLUMN : INDIA MAP--------------

with left_col:
        st.markdown("### State-wise Distribution of Registered Users Across India")

df=db1.map_func()

fig = px.choropleth(
    df,
    geojson=india_geojson,
    locations="State",
    featureidkey="properties.NAME_1",
    color="Value",  # 🔥 change here
    color_continuous_scale=[
        "#E6D6F5",
        "#C5A3E8",
        "#9C6ADE",
        "#6F3CC3",
        "#4B1F8C"
    ]
)
import plotly.graph_objects as go
fig.add_trace(
    go.Scattergeo(
        geojson=india_geojson,
        locations=df["State"],
        featureidkey="properties.NAME_1",
        text=df["State"],
        mode="text",
        textfont=dict(
            size=11,          
            color="#1F1F1F", 
            family="Arial Black"
        )
    )
)


fig.update_geos(
    fitbounds="locations",
    visible=False,
    showcountries=False,
    showcoastlines=False,
    showframe=False,
    lataxis_range=[5, 38],
    lonaxis_range=[70, 100]
    
    )
fig.update_layout(
    height=800,
    margin={"r":10,"t":0,"l":0,"b":0},
    geo=dict(
        bgcolor="rgba(0,0,0,0)"
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    coloraxis_colorbar=dict(
    title="Registered Users",
    tickformat=",",
    x=0.85,
    thickness=15,
    len=0.6,
    tickvals=[
        df["Value"].min(),
        df["Value"].mean(),
        df["Value"].max()
    ],
    ticktext=["Low", "Medium", "High"]
)

)

st.markdown("<div style='margin-top:-30px'></div>", unsafe_allow_html=True)

st.plotly_chart(fig, use_container_width=True)

# ---------------- RIGHT COLUMN : DROPDOWN ----------------

with right_col:
        st.subheader("Select Business Case Study")
        business_case = st.selectbox(
        "",
        [
            "Select",
            "1) Decoding Transaction Dynamics on PhonePe",
            "2) Device Dominance and User Engagement Analysis",
            "3) Insurance Penetration and Growth Potential Analysis",
            "4) Transaction Analysis Across States and Districts",
            "5) User Registration Analysis"
        ]
    )

if business_case == "1) Decoding Transaction Dynamics on PhonePe":
        st.session_state["business_case_one"] = business_case
        st.switch_page("pages/1_Transaction_Dynamics.py")
elif business_case == "2) Device Dominance and User Engagement Analysis":
        st.session_state["business_case_two"] = business_case
        st.switch_page("pages/2_Device_Dominance.py")
elif business_case == "3) Insurance Penetration and Growth Potential Analysis":
        st.session_state["business_case_three"] = business_case
        st.switch_page("pages/3_Insurance_Penetration.py")
elif business_case == "4) Transaction Analysis Across States and Districts":
        st.session_state["business_case_three"] = business_case
        st.switch_page("pages/4_District_Transaction_Analysis.py")
elif business_case == "5) User Registration Analysis":
        st.session_state["business_case_three"] = business_case
        st.switch_page("pages/5_User_Registration.py")

from utils.ui import load_phonepe_theme

load_phonepe_theme()
