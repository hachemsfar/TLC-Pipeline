#needed to make web requests
import requests

#store the data we get as a dataframe
import pandas as pd

#convert the response as a strcuctured json
import json

#mathematical operations on lists
import numpy as np

#parse the datetimes we get from NOAA
from datetime import datetime

#add the access token you got from NOAA
Token = 'XjIjUpNPDmIAEUNzkeUGXzxufLXqisZM'

station_id = 'GHCND:USW00023129'

def get_weather(year,month):  
    #initialize lists to store data
    dates_temp = []
    dates_prcp = []
    temps = []
    prcp = []

    if(month<10):
        month="0"+str(month)

    #make the api call
    r = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00023129&startdate='+str(year)+'-'+str(month)+'-01&enddate='+str(year)+'-'+str(month)+'-31', headers={'token':Token})
    #load the api response as a json
    d = json.loads(r.text)
    #get all items in the response which are average temperature readings
    avg_temps = [item for item in d['results'] if item['datatype']=='TAVG']
    #get the date field from all average temperature readings
    dates_temp += [item['date'] for item in avg_temps]
    #get the actual average temperature from all average temperature readings
    temps += [item['value'] for item in avg_temps]
    
    
    
    #initialize dataframe
    df_temp = pd.DataFrame()
    
    #populate date and average temperature fields (cast string date to datetime and convert temperature from tenths of Celsius to Fahrenheit)
    df_temp['date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in dates_temp]
    df_temp['avgTemp'] = [float(v)/10.0*1.8 + 32 for v in temps]

    df_temp.to_csv("Weather data/weather_NYC_"+str(year)+"_"+str(month)+".csv")
    
    

if __name__ == '__main__':
    get_weather(2021,7)