import streamlit as st
import  pandas as pd
import preprocessor
import helper
df=preprocessor.preprocess()
st.sidebar.title("Olympic Analysis")
user_menu=st.sidebar.radio(
    'select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athelete Wise Analysis')
)


if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country= helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    st.dataframe(medal_tally)



