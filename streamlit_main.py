import streamlit as st
import datetime
import pandas

st.title('👿 Anaya and Zavi Pocket Money 👿 ')

todays_date = datetime.datetime.now().strftime("%Y-%m-%d")

printme = "Today: " + todays_date

st.header(printme)

st.header('-----------------------')

st.header('Anaya has £10')

st.header('-----------------------')

st.header('Zavi has £10')


