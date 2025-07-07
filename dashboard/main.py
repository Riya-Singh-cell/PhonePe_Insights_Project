import streamlit as st 
import requests
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="PhonePe Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for styling, background, and animations
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f0f4f8, #e3f2fd);
    }
    .title {
        font-size: 42px;
        text-align: center;
        color: #1a237e;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .welcome {
        text-align: center;
        margin-top: 100px;
        animation: fadeInSlow 3s ease;
    }
    @keyframes fadeInSlow {
        0% { opacity: 0; transform: translateY(40px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>📲 PhonePe Transaction Insights Dashboard</div>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar filters
st.sidebar.header("📌 Filter Options")
year = st.sidebar.selectbox("Select Year", [2018, 2019, 2020, 2021, 2022])
quarter = st.sidebar.selectbox("Select Quarter", [1, 2, 3, 4])
graph_choices = st.sidebar.multiselect(
    "📈 Choose Graphs to Display",
    ["Bar Chart", "Pie Chart", "Line Chart", "TreeMap", "Raw Data Table"],
    default=[]
)

# API call
url = f"http://127.0.0.1:8000/map/transactions?year={year}&quarter={quarter}"
response = requests.get(url)

if response.status_code == 200:
    df = pd.DataFrame(response.json())
    df["state"] = df["state"].str.title()

    if df.empty:
        st.warning("⚠️ No data available for the selected year and quarter.")
    elif not graph_choices:
        st.markdown("""
            <div class='welcome'>
                <h2 style='color: #0d47a1;'>✨ Welcome to the PhonePe Insights Dashboard ✨</h2>
                <p style='font-size:18px; color: #37474f;'>Use the sidebar filters to explore visualizations of PhonePe transactions across Indian states.</p>
                <p style='font-size:16px; color: #607d8b;'>Select one or more charts from the sidebar to start exploring!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        if "Bar Chart" in graph_choices:
            st.subheader("💰 Top 10 States by Transaction Amount")
            top_states = df.groupby("state")["amount"].sum().nlargest(10).reset_index()
            fig1 = px.bar(top_states, x="state", y="amount", color="amount",
                          color_continuous_scale="Viridis", title=None)
            st.plotly_chart(fig1, use_container_width=True)

        if "Pie Chart" in graph_choices:
            st.subheader("📊 Transaction Count Distribution by State")
            state_share = df.groupby("state")["count"].sum().reset_index()
            fig2 = px.pie(state_share, values="count", names="state", hole=0.4,
                          color_discrete_sequence=px.colors.sequential.RdBu, title=None)
            st.plotly_chart(fig2, use_container_width=True)

        if "Line Chart" in graph_choices:
            st.subheader("📈 Transaction Trend for Top 5 States")
            top5 = df.groupby("state")["amount"].sum().nlargest(5).index.tolist()
            trend = df[df["state"].isin(top5)].groupby(["year", "quarter", "state"])["amount"].sum().reset_index()
            trend["time"] = "Q" + trend["quarter"].astype(str) + "-" + trend["year"].astype(str)
            fig3 = px.line(trend, x="time", y="amount", color="state", markers=True)
            st.plotly_chart(fig3, use_container_width=True)

        if "TreeMap" in graph_choices:
            st.subheader("🌳 TreeMap: Transaction Volume by State")
            treemap = df.groupby("state")["amount"].sum().reset_index()
            fig4 = px.treemap(treemap, path=["state"], values="amount", color="amount",
                              color_continuous_scale="Tealgrn", title=None)
            st.plotly_chart(fig4, use_container_width=True)

        if "Raw Data Table" in graph_choices:
            st.subheader("🧾 Raw Transaction Data")
            st.dataframe(df)

else:
    st.error("❌ Failed to fetch data from backend API.")
