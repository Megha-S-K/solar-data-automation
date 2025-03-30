import requests as r
import pandas as pd

def solarEnergy(url1, url2):
    solarData = pd.read_json(url1)
    windSpeed = pd.read_json(url2)

    solar_energy_data = pd.merge(solarData, windSpeed)
    return solar_energy_data
