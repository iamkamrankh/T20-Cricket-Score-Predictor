import streamlit as st
import pickle
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka']

cities = ['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 'Christchurch', 'Trinidad']

st.title('Cricket Score Predictor')

col1, col2, col3, col4 = st.columns(4)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))
with col3:
    city = st.selectbox('Select city', sorted(cities))
with col4:
    current_score = st.number_input('Current Score')

col5, col6, col7 = st.columns(3)

with col5:
    overs = st.number_input('Overs done (works for over > 5)')
with col6:
    wickets = st.number_input('Wickets out')
with col7:
    last_five = st.number_input('Runs scored in last 5 overs')

balls_left = 120 - (overs * 6)

# Check if overs is zero to avoid division by zero error
if overs != 0:
    crr = current_score / overs
else:
    crr = 0  # or any other default value you want

# Predict score on button click
if st.button('Predict Score'):
    input_df = pd.DataFrame({'batting_team': [batting_team], 
                             'bowling_team': [bowling_team],
                             'city': [city], 
                             'current_score': [current_score],
                             'balls_left': [balls_left], 
                             'wickets_left': [wickets], 
                             'crr': [crr], 
                             'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
