from Visualizations.Visualization import Visualization
from matplotlib.figure import Figure
import copy 

class ChoroplethMap(Visualization):
    def __init__(self, id= 4, name = 'Visualization #4', visual = None, data = None):
        super().__init__(id, name, visual, data)

    def create_choropleth_map(self):
        pass 