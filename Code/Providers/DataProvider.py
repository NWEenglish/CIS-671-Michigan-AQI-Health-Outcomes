from Models.CountyAirPollutant import CountyAirPollutant
from Models.CountyAqiDays import CountyAqiDays
from Models.CountyHealth import CountyHealth
from Models.CountyPfasOccurances import CountyPfasOccurances
from typing import List

class DataProvider:
    def __init__(self, filePath:str = None):
        if (filePath == None):
            self._dataFilePath = '..\Datasets\Clean Data'
        else:
            self._dataFilePath = filePath

    def GetPrimaryPollutants() -> List[CountyAirPollutant]:
        retPrimaryPollutants = List[CountyAirPollutant]

        try:
            fileName = 'annual_aqi_by_county_2023.csv'
            
            # TODO: Get values

        except:
            print("Error occurred while getting primary pollutants.")

        return retPrimaryPollutants

    def GetAqiDays() -> List[CountyAqiDays]:
        retAqiDays = List[CountyAqiDays]

        try:
            fileName = 'annual_aqi_by_county_2023.csv'
            
            # TODO: Get values

        except:
            print("Error occurred while getting AQI values.")

        return retAqiDays

    def GetPfasOccurances() -> List[CountyPfasOccurances]:
        retPfasCount = List[CountyPfasOccurances]

        try:
            fileName = 'Michigan_PFAS_Sites.csv'
            
            # TODO: Get values

        except:
            print("Error occurred while getting PFAS occurances.")

        return retPfasCount

    def GetHealthData() -> List[CountyHealth]:
        retHealthData = List[CountyHealth]

        try:
            fileName = '2023 County Health Rankings Michigan Data - v2.csv'

            # TODO: Get values

        except:
            print("Error occurred while getting health data.")

        return retHealthData
