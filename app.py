# Run with streanlit run app.py
# App should run locally without errors before uploading to server
# In plotly app --> Settings --> Run on save (updates app when file is saved, as can't run from terminal when server is active)
import streamlit as st
# st.write("Hello world!")
import pandas as pd
import matplotlib.pyplot as plt # Opens figure on your screen; acts as figure GUI manager
import plotly.express as px # Interactive plots/visualisations
import plotly.graph_objects as go # Library for further dev objects
from urllib.request import urlopen # Libraries to request datasets from the web (stdlib)
import json

# Fuel efficiency data
df = pd.read_csv("mpg.csv")

st.title("Introduction to streamlit")

st.header("MPG Data Exploration")

# Create sidebar with check box to see df or not
if st.sidebar.checkbox("Show dataframe"):
    st.subheader("This is my dataset")
    st.dataframe(data = df) # Display dataframe

# Create containers laid out as side by side columns
# Pass either an int (# of cols) or an iter of numbers that specifies the relative widths
left_col, mid_cols, right_col = st.columns([3, 1, 1])

# Have different years in df --> select by year of car production
# All option and unique years
# Widget: small standalone component that provides a specific functionality
# selectbox
years = ["All"] + sorted(pd.unique(df["year"]))
year = st.sidebar.selectbox("Choose a year", options=years)

# Plot dependent on year
if year == "All": # year variable specified dynamically via selectbox 
    reduced_df = df
else:
    reduced_df = df[df["year"] == year]

# fig = figure to store plots
# ax = axis object (encompasses all elements of individual plot)
# Can have multiple axes objects passed via axs = plt.subplots(nrows, ncols)
# Acces single plot with axs[row, col]
# sharex, sharey (bool) --> Share axes among subplots
fig, ax = plt.subplots(figsize=(10,8))
# Scatter plot to show dependency between displacement and MPG value
ax.scatter(reduced_df["displ"], reduced_df["hwy"])
ax.set_title("Engine size vs. Mileage")
st.pyplot(fig) # Display plot in app





