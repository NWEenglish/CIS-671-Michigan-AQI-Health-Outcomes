from Visualizations.Visualization import Visualization
from matplotlib.figure import Figure
import copy 

class HeatMap(Visualization):
    def __init__(self, id= 5, name = 'Visualization #5', visual = None, data = None):
        super().__init__(id, name, visual, data)  

    def create_heat_map(self):
        pass 