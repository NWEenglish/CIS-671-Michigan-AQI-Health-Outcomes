from Models.CountyAirPollutant import CountyAirPollutant
from Models.CountyAqiDays import CountyAqiDays
from Models.CountyHealth import CountyHealth
from Models.CountyPfasOccurances import CountyPfasOccurances
from typing import List
import numpy
import geopandas as gpd

class DataProvider:
    def __init__(self, filePath:str = None):
        if (filePath == None):
            self._dataFilePath = '../Datasets/Clean Data'
        else:
            self._dataFilePath = filePath

    def GetPrimaryPollutants() -> List[CountyAirPollutant]:
        retPrimaryPollutants = []

        try:
            fileName = '../Datasets/Clean Data/annual_aqi_by_county_2023.csv'
            data = numpy.loadtxt(fileName, delimiter=',', skiprows=1, dtype=str)
            
            for row in range(len(data)):
                values = data[row]
                county = CountyAirPollutant(values[1], values[12], values[13], values[14], values[15], values[16])
                retPrimaryPollutants.append(county)

        except Exception as ex:
            print(f"Error occurred while getting primary pollutants. | Exception: {ex}")

        return retPrimaryPollutants

    def GetAqiDays() -> List[CountyAqiDays]:
        retAqiDays = []

        try:
            fileName = '../Datasets/Clean Data/annual_aqi_by_county_2023.csv'
            data = numpy.loadtxt(fileName, delimiter=',', skiprows=1, dtype=str)

            for row in range(len(data)):
                values = data[row]
                county = CountyAqiDays(values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[11])
                retAqiDays.append(county)

        except Exception as ex:
            print(f"Error occurred while getting AQI values. | Exception: {ex}")

        return retAqiDays

    def GetPfasOccurances() -> List[CountyPfasOccurances]:
        retPfasCount = []

        try:
            fileName = '../Datasets/Clean Data/Michigan_PFAS_Sites.csv'
            data = numpy.loadtxt(fileName, delimiter=',', skiprows=1, dtype=str)
            
            for row in range(len(data)):
                values = data[row]
                countyName = values[0].strip()

                # If already in list, increment occurrence, else append to list
                wasFound = False
                for existingCounty in retPfasCount:
                    if (existingCounty.County == countyName):
                        existingCounty.Occurances += 1
                        wasFound = True
                        break
                
                if not wasFound:
                    county = CountyPfasOccurances(countyName, 1)
                    retPfasCount.append(county)

        except Exception as ex:
            print(f"Error occurred while getting PFAS occurances. | Exception: {ex}")

        return retPfasCount

    def GetHealthData() -> List[CountyHealth]:
        retHealthData = []

        try:
            fileName = '../Datasets/Clean Data/2023 County Health Rankings Michigan Data - v2.csv'
            data = numpy.loadtxt(fileName, delimiter=',', skiprows=1, dtype=str)

            for row in range(len(data)):
                values = data[row]
                county = CountyHealth(values[1], values[2], values[3], values[4])
                retHealthData.append(county)

        except Exception as ex:
            print(f"Error occurred while getting health data. | Exception: {ex}")

        return retHealthData
    
    def GetGeoSpatialData() -> gpd.GeoDataFrame:
        try:
            fileName = '../Datasets/Clean Data/County.geojson'
            geospatial_data = gpd.read_file(fileName)
        
        except Exception as ex:
            print(f"Error occurred while getting health data. | Exception: {ex}")
        
        return geospatial_data

