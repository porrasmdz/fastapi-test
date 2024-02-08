import math
from typing import Any, Dict, List
from fastapi import FastAPI, Query
from .model import Trip
from .controller import get_paginated_trips, get_filtered_trips_by_location
from .database import client

app = FastAPI()

class APIResponse:
    def __init__(self, data: List[Any], page: int, total_pages: int, limit: int, total_registries: int):
        self.data = data
        self.page = page
        self.total_pages = total_pages
        self.limit = limit
        self.total_registries = total_registries

@app.get('/')
def read_root():
    result = client.execute('SHOW DATABASES')
    # client.command('SELECT count() FROM trips')
    total = client.execute('SELECT count() FROM trips')

    return {
        "databases": str(result),
        "total": "Total results %s" % str(total),
        "docs-entrypoint": "/docs"
    }


@app.get('/trips')
def get_all_trips(page: int =Query(1,ge=1), limit: int = Query(15, ge=1, le=10000)):
 
    data = get_paginated_trips(page,limit)
    
    total_count = data[1]
    
    total_pages = math.ceil(total_count/limit)
    return APIResponse(
        data= data[0],
        page= page,
        total_pages=total_pages,
        limit= limit,
        total_registries= total_count,
    )


@app.get('/trips/{pickup_ntaname}')
def get_trips_by_location(pickup_ntaname: str,page: int =Query(1,ge=1), limit: int = Query(15, ge=1, le=10000)):
 
    data = get_filtered_trips_by_location(page,limit)
    total_count = data[1]
    
    total_pages = math.ceil(total_count/limit)
    return APIResponse(
        data= data[0],
        page= page,
        total_pages=total_pages,
        limit= limit,
        total_registries= total_count,
    )