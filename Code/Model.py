from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from Visualizations.BubbleChart import BubbleChart
from Visualizations.ColumnChart import ColumnChart
from Visualizations.ChoroplethMap import ChoroplethMap
from Visualizations.HeatMap import HeatMap
from Visualizations.PieChart import PieChart
from Visualizations.ScatterPlot import ScatterPlot

class Model:
    def __init__(self):
        self.visualizations = {
            Visual.BubbleChart: BubbleChart(),
            Visual.ColumnChart: ColumnChart(),
            Visual.PieChart: PieChart(),
            Visual.ChoroplethMap: ChoroplethMap(),
            Visual.HeatMap: HeatMap(),
            Visual.ScatterPlot: ScatterPlot()
        }

    def set_visualizations(self, aqi_days, pfas_occurances, primary_pollutants, geo_data, health_data) -> None:
        self.add_visual(Visual.BubbleChart, pfas_occurances)
        self.add_visual(Visual.ColumnChart, aqi_days)
        self.add_visual(Visual.PieChart, primary_pollutants)
        self.add_visual(Visual.ChoroplethMap, [geo_data, health_data, primary_pollutants])
        self.add_visual(Visual.HeatMap, [aqi_days, health_data])
        self.add_visual(Visual.ScatterPlot, [aqi_days, health_data])

    def get_visualizations(self) -> BaseVisual:
        return self.visualizations
    
    def update_visualization(self, visual, county, shouldCountyDisplay) -> None:
        if shouldCountyDisplay:
            visual.add_to_dict(county)
        else:
            visual.remove_from_dict(county)

        self.visualizations.get(visual.get_id()).create_chart()

    def add_visual(self, visualType:Visual, data) -> None:
        self.visualizations.get(visualType).set_data(data)
        self.visualizations.get(visualType).create_chart()
