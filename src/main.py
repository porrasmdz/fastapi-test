import math
from typing import Any, List, Optional
from fastapi import FastAPI, Query
from src.model import Trip
from src.controller import get_filtered_trips, daily_pickups_per_neighborhood, unique_neighborhoods, get_root

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
    return get_root()


@app.get('/trips')
def get_trips(pickup_ntaname: Optional[str] = Query(None), 
                          pickup_date: Optional[str] = Query(None), 
                          page: int = Query(1, ge=1), 
                          limit: int = Query(15, ge=1, le=10000)):
    filters = {}
    if pickup_ntaname:
        filters['pickup_ntaname'] = pickup_ntaname
    if pickup_date:
        filters['pickup_date'] = pickup_date
    data = get_filtered_trips(filters=filters, page=page, limit=limit)
    total_count = data[1]

    total_pages = math.ceil(total_count/limit)
    return APIResponse(
        data=data[0],
        page=page,
        total_pages=total_pages,
        limit=limit,
        total_registries=total_count,
    )


@app.get('/trips/daily-by-neighborhood')
def get_daily_trips_by_neighborhood(pickup_ntaname: Optional[str] = Query(None), 
                          pickup_date: Optional[str] = Query(None), 
                          page: int = Query(1, ge=1), 
                          limit: int = Query(15, ge=1, le=10000)):
    filters = {}
    if pickup_ntaname:
        filters['pickup_ntaname'] = pickup_ntaname
    if pickup_date:
        filters['pickup_date'] = pickup_date
    data = daily_pickups_per_neighborhood(filters=filters, page=page, limit=limit)
    total_count = data[1]
    total_pages = math.ceil(total_count/limit)
    return APIResponse(
        data=data[0],
        page=page,
        total_pages=total_pages,
        limit=limit,
        total_registries=total_count,
    )

# For frontend
@app.get('/neighborhoods')
def get_neighborhoods( page: int = Query(1, ge=1), 
                          limit: int = Query(15, ge=1, le=10000)):
   
    data = unique_neighborhoods(page=page, limit=limit)
    total_count = data[1]

    total_pages = math.ceil(total_count/limit)
    return APIResponse(
        data=data[0],
        page=page,
        total_pages=total_pages,
        limit=limit,
        total_registries=total_count,
    )
