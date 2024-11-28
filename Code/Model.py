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
            Visual.HeatMap: HeatMap()
        }

    def set_visualizations(self, aqi_days, pfas_occurances, primary_pollutants, geo_data, health_data) -> None:
        self.add_bubble_chart(pfas_occurances)
        self.add_column_chart(aqi_days)
        self.add_pie_chart(primary_pollutants)
        self.add_choropleth_map(geo_data, health_data, primary_pollutants) 

    def get_visualizations(self) -> BaseVisual:
        return self.visualizations
    
    def update_visualization(self, visual, county, state) -> None:
        if visual.get_id() == Visual.BubbleChart:
            self.update_bubble_chart(visual, county, state)
        elif visual.get_id() == Visual.ColumnChart:
            self.update_column_chart(visual, county, state)
        elif visual.get_id() == Visual.PieChart:
            self.update_pie_chart(visual, county, state)
        elif visual.get_id() == Visual.ChoroplethMap:
            self.update_choropleth_map(visual, county, state)
        elif visual.get_id() == Visual.HeatMap:
            self.update_heat_map(visual, county, state)
    
    def add_bubble_chart(self, pfas_occurances) -> None:
        self.visualizations.get(Visual.BubbleChart).set_data(pfas_occurances)
        self.visualizations.get(Visual.BubbleChart).create_bubble_chart()

    def update_bubble_chart(self, visual, county, state) -> None:
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)
        
        self.visualizations.get(Visual.BubbleChart).create_bubble_chart()
    
    def add_column_chart(self, aqi_days) -> None:
        self.visualizations.get(Visual.ColumnChart).set_data(aqi_days)
        self.visualizations.get(Visual.ColumnChart).create_column_chart() 

    def update_column_chart(self, visual, county, state) -> None:
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)

        self.visualizations.get(Visual.ColumnChart).create_column_chart()

    def add_pie_chart(self, primary_pollutant) -> None:
        self.visualizations.get(Visual.PieChart).set_data(primary_pollutant)
        self.visualizations.get(Visual.PieChart).create_pie_chart() 

    def update_pie_chart(self, visual, county, state) -> None:
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)

        self.visualizations.get(Visual.PieChart).create_pie_chart()

    def add_choropleth_map(self, geospatial, health_data, primary_pollutant) -> None:
        self.visualizations.get(Visual.ChoroplethMap).set_data([geospatial, health_data, primary_pollutant])
        self.visualizations.get(Visual.ChoroplethMap).create_choropleth_map()
