from Enums.AirPollutant import AirPollutant
from Visualizations.Helpers.AirPollutantHelper import AirPollutantHelper

class CountyAirPollutant:
    def __init__(self, county:str, coDays:int, no2Days:int, ozoneDays:int, pm25:int, pm10:int):
        self.County = county    
        self._aqiValues = dict({
            AirPollutant.CO: coDays,
            AirPollutant.NO2: no2Days,
            AirPollutant.Ozone: ozoneDays,
            AirPollutant.PM25: pm25,
            AirPollutant.PM10: pm10
        })

    def GetPollutionCount(self, pollutant:AirPollutant|str) -> int:
        retDays = 0
        
        if self._aqiValues.get(pollutant) != None:
            retDays = self._aqiValues[pollutant]
        else:
            apHelper = AirPollutantHelper()
            pollutantEnum = apHelper.GetEnumFromName(pollutant)
            retDays = self._aqiValues[pollutantEnum]

        return retDays

    def GetPrimaryPollutant(self) -> AirPollutant:
        return max(self._aqiValues, key=self._aqiValues.get) # TODO: This needs to be tested - idk if this actually works
