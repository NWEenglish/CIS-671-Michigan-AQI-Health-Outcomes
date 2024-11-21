
class CountyHealth:
    def __init__(self, county:str, healthOutcome:float, healthFactors:float, qualityOfLife:float):
        self.County = county    
        self.HealthOutcome = healthOutcome
        self.HealthFactors = healthFactors
        self.QualityOfLife = qualityOfLife
        self.HealthScore = self._getHealthScore(healthOutcome, healthFactors)

    def _getHealthScore(self, healthOutcome:float, healthFactors:float) -> float:
        return -1 * ((healthOutcome + healthFactors) / 2)
