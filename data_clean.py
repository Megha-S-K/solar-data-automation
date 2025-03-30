import pandas as pd
from datetime import date

today = date.today()
today_date = today.strftime('%d-%m-%y')

def dataClean(data):

    date = data['time'].str.split(' ').str.get(0)
    data['time'] = data['time'].str.split(' ').str.get(1).astype(int)
    data['temp'] = data['temp'].astype(int)
    data['flux'] = data['flux'].astype(int)
    data['speed'] = data['speed'].astype(int)
    data['direction'] = data['direction'].astype(int)

    Date = pd.DataFrame(
    {
        'date': date
    })
     
    fullData = Date.join(data)
    
    full_data = fullData.loc[(data['time']>=615) & (data['time']<=1745)]
    today_data = full_data.loc[(full_data['date'] == today_date)]
    return full_data, today_data
