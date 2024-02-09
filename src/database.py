import os
from typing import Any, Dict, List, Tuple

from clickhouse_driver import Client

DB_HOST = os.environ['DB_HOST']# DB_HOST='clickhouse'
DB_PORT = os.environ['DB_PORT'] #DB_PORT='8123'
DB_USER = os.environ['DB_USER'] #DB_USER='default'
DB_PASSWORD = os.environ['DB_PASSWORD'] #DB_PASSWORD=''

client = Client(host=DB_HOST)
# clickhouse_connect.get_client(host=DB_HOST, port=DB_PORT,username=DB_USER)

def paged_filtered_query(filters: Dict[str,Any]={}, page: int = 1, limit: int = 15) -> Tuple:
    queued_filters = list(filters.keys())
    queue_len = len(queued_filters)
    offset = (page - 1) * limit
    query = "SELECT trip_id, pickup_date, pickup_ntaname, passenger_count, trip_distance, tolls_amount, total_amount"
    totalquery = "SELECT COUNT(*)"

    query += " FROM trips"
    totalquery += " FROM trips"

    for filter in queued_filters:
        if queue_len == len(queued_filters):
            query += " WHERE %s = \'%s\'" % (filter, str(filters[filter])) 
            totalquery += " WHERE %s = \'%s\'" % (filter, str(filters[filter]))
        else:
            query += " AND %s = \'%s\'" % (filter, str(filters[filter])) 
            totalquery += " AND %s = \'%s\'" % (filter, str(filters[filter]))
        queue_len =- 1   
    
    query += " ORDER BY pickup_date DESC LIMIT %d OFFSET %d" % (int(limit), int(offset))
    
    data_result = client.execute(query)
    total_results = client.execute(totalquery)
    

    return (data_result, total_results[0][0])
    

def query_daily_pickups_per_neighborhood(filters: Dict[str,Any]={}, page: int = 1, limit: int = 15) -> Tuple:
    queued_filters = list(filters.keys())
    queue_len = len(queued_filters)
    offset = (page - 1) * limit
    query = "SELECT pickup_date, pickup_ntaname,SUM(1) AS number_of_trips"
    totalquery = "SELECT COUNT(*) FROM (SELECT pickup_date, pickup_ntaname,SUM(1) AS number_of_trips"

    query += " FROM trips"
    totalquery += " FROM trips"

    for filter in queued_filters:
        if queue_len == len(queued_filters):
            query += " WHERE %s = \'%s\'" % (filter, str(filters[filter])) 
            totalquery += " WHERE %s = \'%s\'" % (filter, str(filters[filter]))
        else:
            query += " AND %s = \'%s\'" % (filter, str(filters[filter])) 
            totalquery += " AND %s = \'%s\'" % (filter, str(filters[filter]))
        queue_len =- 1   
    
    query += " GROUP BY pickup_date, pickup_ntaname"
    totalquery += " GROUP BY pickup_date, pickup_ntaname)"
    query += " ORDER BY pickup_date DESC LIMIT %d OFFSET %d" % (int(limit), int(offset))
    
    data_result = client.execute(query)
    total_results = client.execute(totalquery)
    

    return (data_result, total_results[0][0])
    

def query_unique_neighborhoods(page: int = 1, limit: int = 15) -> Tuple:
    
    offset = (page - 1) * limit
    query = "SELECT DISTINCT(pickup_ntaname)"
    totalquery = "SELECT COUNT(*) FROM (SELECT DISTINCT(pickup_ntaname)"

    query += " FROM trips"
    totalquery += " FROM trips)"
    
    query += " ORDER BY pickup_ntaname DESC LIMIT %d OFFSET %d" % (int(limit), int(offset))
    
    data_result = client.execute(query)
    total_results = client.execute(totalquery)
    

    return (data_result, total_results[0][0])
    
