from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId
from bson.timestamp import Timestamp
from datetime import date

# default_time = dt.utcnow()
# default_time = dt.now()
default_day = date.today()

datetime_to_date = lambda t: t.isoformat(' ', 'hours').split(' ')[0]
create_datetime = lambda t: t.isoformat()
datetime_to_date_field = datetime.now().isoformat().split(' ')[0]


encode_date = lambda t: t.isoformat()

# json_encoders = {
    # ObjectId: str,
    # datetime: datetime.isoformat,
    # date: date.today
    # date: lambda dt: dt.today()
    # datetime: lambda dt: dt.strptime("%Y-%m-%dT%H:%M:%S"),
    # datetime: lambda dt: dt.strptime("%Y-%m-%d"),
    # datetime: lambda dt: dt.utcnow().isoformat(),
    # date: lambda dt: dt.isoformat(),
# }


class CreateModelConfig(BaseModel):
    '''
    create new model: create new document with bson _id
    create datetime with timestamp
    '''
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { 
            ObjectId: lambda x: ObjectId(oid=x),
            datetime: create_datetime
        }


class ReadModelConfig(BaseModel):
    '''query model: extract _id as str
    datetime encoding: this controls how datetime is 
        - queried
        - created    
    ObjectId encoding:
        - can be string => '_id': '6160be356dbbd9d9c2ed4a35'
            - ObjectId: str
        - can be bson ObjectId -> {'_id': {'oid': '6160be356dbbd9d9c2ed4a35'}
            - ObjectId: lambda x: ObjectId(oid=x),
    '''
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { 
            ObjectId: str,
            datetime: datetime_to_date,
        }


class UpdateModelConfig(BaseModel):
    '''updating models'''
    class Config:
        arbitrary_types_allowed = True
        json_encoders = { 
            ObjectId: str,
            datetime: datetime_to_date,
            # date: encode_date
        }