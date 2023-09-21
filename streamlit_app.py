import streamlit as st
import pandas as pd
import plotly.express as px

# Decorator to cache data
@st.cache  
def load_data():
    data = pd.read_csv("openpowerlifting-2023-09-16-a8e1bcb4.csv")
    return data

# Layout configurations
st.set_page_config(
    page_title="Powerlifting Statistics Dashboard",
    layout="wide"
)

# Load the data
df = load_data()

# Title and Introduction
st.title("🏋️‍♀️ Powerlifting Statistics Dashboard 🏋️‍♂️")

with st.container():
    st.markdown("""
    ## Welcome to the Powerlifting Statistics Dashboard!
    Below is the trend showing the number of competitors by year.
    """)

# Extracting year from Date
df['Year'] = pd.to_datetime(df['Date']).dt.year

# Counting the number of people who competed each year
count_by_year = df['Year'].value_counts().sort_index().reset_index()
count_by_year.columns = ['Year', 'Number of Athletes']

# Plotting using Plotly
fig = px.line(count_by_year, x='Year', y='Number of Athletes',
              labels={'Number of Athletes': 'Number of Athletes'},
              title='📈 Trend of Number of Competitors by Year',
              line_shape='linear')
fig.update_traces(line=dict(width=2.5))
fig.update_layout(autosize=False, width=800, height=500,
                  margin=dict(l=50, r=50, b=100, t=100))

# Show the plot
st.plotly_chart(fig)
