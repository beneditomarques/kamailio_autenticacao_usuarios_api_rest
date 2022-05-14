from fastapi import FastAPI, Request, Response, UploadFile
from fastapi.responses import FileResponse
from fastapi.openapi.utils import get_openapi
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
from urllib.parse import unquote
import os
import motor.motor_asyncio
from bson import ObjectId
from pymongo import MongoClient, ReturnDocument
import secrets



app = FastAPI()
security = HTTPBasic()


# Constants
DEFAULT_PROJECTION    = {'_id':0}
MONGODB_URL           = "mongodb://"+os.environ["DB_USER"]+":"+os.environ["DB_PASSWORD"]+"@"+os.environ["DB_SERVER"]+":"+os.environ["DB_PORT"]+"/"+os.environ["DB_NAME"]+"?retryWrites=true&w=majority"
CLIENT                = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
DB                    = CLIENT.get_database(os.environ["DB_NAME"])

# Authentication
def authentication(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, os.environ["API_USER"])
    correct_password = secrets.compare_digest(credentials.password, os.environ["API_PASSWORD"])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/subscribers")
async def search_subscribers(username: str, domain: str, credentials: HTTPBasicCredentials = Depends(security)):   
    authentication(credentials)             
    projection = {"_id":0}
    result = await DB['subscribers'].find_one({'username':username,'domain': domain},projection)
    if result:
        return result
    else:
        return Response(status_code=404,content=json.dumps({'detail':"Subscriber not found"}))

    