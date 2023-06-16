__author__ = "Khaled Alam"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Khaled Alam"
__email__ = "khaledalam.net@gmail.com"
__status__ = "Production"

from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
import pytz
from datetime import datetime
import socket

load_dotenv()

# Get country from env.
app_country = os.getenv('APP_COUNTRY')

app = FastAPI()

@app.get("/result")
async def result(request: Request):
    global app_country
    
    # different logic based on app_country env var.
    if app_country == 'US':
        result = "This is a test message"
    elif app_country == 'UAE':
        result = "هذه رسالة تجريبية"
    else:
        result = "N/A"
        
    # IP
    client_host = request.client.host
    
    # Get host name => differ pods
    hostname = socket.gethostname()
    
    return {
        "client_host":          client_host,
        "hostname-pod":         'pod/' + hostname,
        "app_country":          app_country,
        "result":               result
    }
    
@app.get("/datetimenow")
async def datetimenow(request: Request):
    global app_country
    
    # different logic based on app_country env var.
    if app_country == 'US':
        country_time = datetime.now(pytz.timezone('America/Chicago'))
        country_date_time = country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S")
    elif app_country == 'UAE':
        country_time = datetime.now(pytz.timezone('Asia/Dubai'))
        country_date_time =  country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S")
    else:
        app_country = 'N/A'
        country_date_time = 'N/A'
        
    return {
        "country_date_time":    country_date_time,
    }