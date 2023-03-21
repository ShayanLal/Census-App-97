
import numpy as np
import pandas as pd
import streamlit as st

@st.cache()
def load_data():
	df = pd.read_csv('adult.csv', header=None)
	df.head()

	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	df.head()

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	df.dropna(inplace=True)

	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

import census_home
import census_plots

pages_dict = {"Home": census_home, "Visualise Data": census_plots}
st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))

selected_page = pages_dict[user_choice]
selected_page.app(census_df)