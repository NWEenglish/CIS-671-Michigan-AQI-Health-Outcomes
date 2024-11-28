from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
import copy 

class ScatterPlot(BaseVisual):
    def __init__(self, visual, data):
        visualType = Visual.ScatterPlot
        name = 'Visualization #6'
        hasFiltering = False

        super().__init__(visualType, name, visual, data, hasFiltering) 

    def create_scatter_plot(self):
        pass
