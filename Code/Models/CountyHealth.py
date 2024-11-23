
class CountyHealth:
    def __init__(self, county:str, healthOutcome:str, healthFactors:str, qualityOfLife:str):
        self.County = county    
        self.HealthOutcome = float(healthOutcome)
        self.HealthFactors = float(healthFactors)
        self.QualityOfLife = float(qualityOfLife)
        self.HealthScore = self._getHealthScore(self.HealthOutcome, self.HealthFactors)

    def _getHealthScore(self, healthOutcome:float, healthFactors:float) -> float:
        return -1 * ((healthOutcome + healthFactors) / 2)
