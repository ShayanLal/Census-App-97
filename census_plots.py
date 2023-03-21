import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):

    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    # Store the current value of this widget in a variable 'plot_list'.
    plot_list = st.multiselect("Select charts/plots", ('Count Plot', 'Pie Plot', 'Box Plot'))

    # Display count plot using seaborn module and 'st.pyplot()' 
    if 'Count Plot' in plot_list:
      st.subheader('Count plot for the distribution of records for unique work class groups')
      plt.figure(figsize = (15,10))
      sns.countplot(census_df['workclass'])
      st.pyplot()

    # Display pie plot using matplotlib module and 'st.pyplot()'
    if 'Pie Plot' in plot_list:
      st.subheader('Pie Chart')
      features = st.selectbox('Select the feature values', ('income', 'gender'))
      plt.figure(figsize = (15, 10))
      counts = census_df[features].value_counts()
      plt.pie(counts, labels = counts.index, autopct = '%.2f%%', explode = [.05, .05])
      plt.title(f"Distribution of records for different income groups")
      st.pyplot()

    # Display box plot using matplotlib module and 'st.pyplot()'
    if 'Box Plot' in plot_list:
      st.subheader('Box Plot for the Hours Worked Per Week')
      features = st.selectbox('Select the feature values', ('income', 'gender'))
      plt.figure(figsize = (15,10))
      plt.title(f'Distribution of hours worked per week for different {features} groups')
      sns.boxplot(census_df['hours-per-week'], census_df[features])
      st.pyplot()