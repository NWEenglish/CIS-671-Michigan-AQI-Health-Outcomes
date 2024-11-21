from enum import Enum

class AqiStandard(Enum):
    GoodDay = 1
    ModerateDay = 2
    UnhealthyForSensitiveGroupsDay = 3
    UnhealthyDay = 4
    VeryUnhealthyDay = 5
    HazardousDays =6
