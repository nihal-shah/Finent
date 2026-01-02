from fastapi import FastAPI
import httpx as httpx
from model import Fetching
app = FastAPI()

@app.post("/gethistoricaltypeSubindexdata")
def get_historical_type_subindex_data(fetching: Fetching):
    indextype = fetching.indextype
    # Dummy response for demonstration purposes
    data = {
        "Equity": {"data": [1, 2, 3]},
        "Fixed Income": {"data": [4, 5, 6]},
        "Multi Asset": {"data": [7, 8, 9]}
    }
    return data.get(indextype, {"data": []})


    
