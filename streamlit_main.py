import streamlit
from datetime import date
import pandas

streamlit.title('👿 Anaya and Zavi Pocket Money 👿 ')

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)
