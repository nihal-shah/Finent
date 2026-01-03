from fastapi import FastAPI
import httpx as httpx
from model import Fetching
import os
from dotenv import load_dotenv


load_dotenv()
tewlvedata_api_key=os.getenv("twelvedata_api_key")
app = FastAPI()

@app.post("/gethistoricaltypeSubindexdata")
def get_historical_type_subindex_data(fetching: Fetching):
        stock=fetching.stock
        # start=input("Enter the start date (2006-01-02 22:52:00): ")
        start=fetching.start_date
        end=fetching.end_date
        response = httpx.get(f"https://api.twelvedata.com/time_series?apikey={tewlvedata_api_key}&symbol={stock}&interval=1day&start_date={start}&end_date={end}&format=JSON")
        print(response.json())
        return response.json()