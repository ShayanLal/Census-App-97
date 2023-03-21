import numpy as np
import pandas as pd
import streamlit as st

def app(census_df):
    with st.beta_expander("View Dataset"):
        st.table(census_df)   
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(census_df.describe())