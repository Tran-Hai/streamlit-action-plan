import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
from data.DataProcessor import crawl_data, process_data
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title = 'Actions Plan', layout = 'wide')

st.title(':dart: Actions Plan')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# Setting time range for planing
startDate = pd.to_datetime('today').replace(day=1)
endDate = pd.to_datetime('today')

# Convert time objects to string
startDate = startDate.strftime('%d-%m-%Y')
endDate = endDate.strftime('%d-%m-%Y')

# Start crawl data and convert to pandas dataframe
json_data = crawl_data(startDate, endDate)
df = process_data(json_data)

st.write(df)

