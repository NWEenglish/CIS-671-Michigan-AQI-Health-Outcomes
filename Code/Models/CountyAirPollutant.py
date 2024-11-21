from Enums.AirPollutant import AirPollutant

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

    def GetPrimaryPollutant(self) -> AirPollutant:
        return max(self._aqiValues, key=self._aqiValues.get) # TODO: This needs to be tested - idk if this actually works
