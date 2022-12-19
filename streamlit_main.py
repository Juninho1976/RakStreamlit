import streamlit
from datetime import date
import pandas

streamlit.title('👿 Anaya and Zavi Pocket Money 👿 ')

todays_date = date.today()

printme = "Today is" + todays_date

streamlit.header(printme)
