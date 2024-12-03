from Enums.AirPollutant import AirPollutant
from Visualizations.Helpers.AirPollutantHelper import AirPollutantHelper

class ColorHelper():
    def __init__(self):
        self._colorMapper = {
            AirPollutant.CO: 'orange',
            AirPollutant.NO2: 'yellow',
            AirPollutant.Ozone: 'blue',
            AirPollutant.PM25: 'red',
            AirPollutant.PM10: 'green'
        }

    def GetColor(self, pollutant:AirPollutant|str) -> str:
        retColor = None
        
        if self._colorMapper.get(pollutant) != None:
            retColor = self._colorMapper.get(pollutant)
        else:
            apHelper = AirPollutantHelper()
            retColor = self._colorMapper.get(apHelper.GetEnumFromName(pollutant))

        return retColor

    def GetColorMap(self) -> dict:
        retColorMap = {}
               
        for apEnum in self._colorMapper.keys():
            retColorMap[apEnum.value] = self._colorMapper[apEnum]

        return retColorMap
