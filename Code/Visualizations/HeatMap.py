from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
import copy 

class HeatMap(BaseVisual):
    def __init__(self):
        visualType = Visual.HeatMap
        name = 'Visualization #5'
        hasFiltering = False
    
        super().__init__(visualType, name, hasFiltering)  

    def create_heat_map(self):
        pass 