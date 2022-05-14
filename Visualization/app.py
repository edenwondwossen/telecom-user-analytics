import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

#title
st.title('User Analytics in the Telecommunication Industry')
#sidebar
st.sidebar.title('satisfaction analysis of users')
# sidebar markdown 
st.sidebar.markdown("We can analyse users satisfaction from this application.")

data=pd.read_csv('../data/cleaned/user_satisfaction_data.csv')
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))