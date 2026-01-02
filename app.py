import streamlit as st
import httpx as httpx
import os
from dotenv import load_dotenv

load_dotenv()
domain = os.environ.get("DOMAIN")
option = st.selectbox('Select an Index Type?',('Equity', 'Fixed Income', 'Multi Asset'))

st.write('You selected:', option)
response = httpx.post(domain + "/gethistoricaltypeSubindexdata", json={"indextype": option},timeout=10.0)
st.json(response.json())