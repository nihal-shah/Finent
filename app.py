import streamlit as st
import httpx as httpx
import os
from dotenv import load_dotenv

load_dotenv()
domain = os.environ.get("DOMAIN")
import streamlit as st
import datetime

stock_name = st.text_input("Enter your stock symbol")
start_datetime = st.datetime_input(
    "Select start date and time",
    value=None
)
end_datetime = st.datetime_input(
    "Select end date and time",
    value=None
)
def fetch_data():
    response = httpx.post(domain + "/gethistoricaltypeSubindexdata", json={"stock": stock_name, "start_date": start_datetime.strftime("%Y-%m-%d %H:%M:%S"), "end_date": end_datetime.strftime("%Y-%m-%d %H:%M:%S")},timeout=30.0)
    return response

st.write("You selected:", start_datetime, "to", end_datetime)
if st.button("fetch data"):
    # Code inside this 'if' block only executes when the button is pressed
    response = fetch_data()
    # st.write(response)
    data = response.json()
    st.json(data)