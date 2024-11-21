from Enums.AqiStdMeasure import AqiStandard

class CountyAqiDays:
    def __init__(self, county:str, totalDays:int, goodDays:int, moderateDays:int, unhealthyForSensDays:int, 
                 unhealthyDays:int, veryUnhealthyDays:int, hazardousDays:int, medianAqi:int):
        self.County = county
        self._totalDays = totalDays
        self._aqiValues = dict({
            AqiStandard.GoodDay: goodDays,
            AqiStandard.ModerateDay: moderateDays,
            AqiStandard.UnhealthyForSensitiveGroupsDay: unhealthyForSensDays,
            AqiStandard.UnhealthyDay: unhealthyDays,
            AqiStandard.VeryUnhealthyDay: veryUnhealthyDays,
            AqiStandard.HazardousDays: hazardousDays
        })
        self.MedianAqi = medianAqi

    def GetAqiDays(self, aqi:AqiStandard) -> int:
        return self._aqiValues[aqi]

    def GetAqiPercentage(self, aqi:AqiStandard) -> float:
        return self._aqiValues[aqi] / self._totalDays
