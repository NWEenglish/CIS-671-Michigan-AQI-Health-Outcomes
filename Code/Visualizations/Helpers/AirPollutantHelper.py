from Enums.AirPollutant import AirPollutant
from typing import List

class AirPollutantHelper():
    def __init__(self):
        self._stringToEnumMapper = {
            'CO': AirPollutant.CO,
            'NO2': AirPollutant.NO2,
            'Ozone': AirPollutant.Ozone,
            'PM25': AirPollutant.PM25,
            'PM10': AirPollutant.PM10
        }

    def GetEnumFromName(self, pollutantStr:str) -> AirPollutant:
        return self._stringToEnumMapper[pollutantStr]
    
    def GetPollutants(self) -> List[AirPollutant]:
        return self._stringToEnumMapper.values()
