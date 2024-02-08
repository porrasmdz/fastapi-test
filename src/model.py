from typing import Text, Optional
from enum import Enum
from uuid import uuid4 as uuid
from datetime import datetime, date
from pydantic import BaseModel

class PaymentType(Enum):
    UNK = 0 
    CSH = 1 
    CRE = 2 
    NOC = 3 
    DIS = 4

class Trip(BaseModel):
    trip_id: int
    pickup_date :date
    pickup_datetime :datetime
    dropoff_date :date
    dropoff_datetime :datetime
    store_and_fwd_flag :int
    rate_code_id :int
    pickup_longitude : float
    pickup_latitude :float
    dropoff_longitude :float
    dropoff_latitude :float
    passenger_count :int
    trip_distance :float
    fare_amount :float
    extra :float
    mta_tax :float
    tip_amount :float
    tolls_amount :float
    ehail_fee :float
    improvement_surcharge :float
    total_amount :float
    payment_type : PaymentType
    trip_type :int
    pickup: str
    dropoff: str
    cab_type: Enum('CabType', ['yellow','green','uber'])
    pickup_nyct2010_gid :int
    pickup_ctlabel :float
    pickup_borocode :int
    pickup_ct2010 :str
    pickup_boroct2010 :str
    pickup_cdeligibil :str
    pickup_ntacode: str
    pickup_ntaname :str
    pickup_puma :int
    dropoff_nyct2010_gid :int
    dropoff_ctlabel :float
    dropoff_borocode :int
    dropoff_ct2010 :str
    dropoff_boroct2010 :str
    dropoff_cdeligibil :str
    dropoff_ntacode: str
    dropoff_ntaname :str
    dropoff_puma: int

