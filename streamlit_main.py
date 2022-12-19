import streamlit as st
import datetime
import pandas

st.title('👿 Anaya and Zavi Pocket Money 👿 ')

todays_date = datetime.datetime.now().strftime("%Y-%m-%d")

printme = "Today is the " + todays_date

st.header(printme)

