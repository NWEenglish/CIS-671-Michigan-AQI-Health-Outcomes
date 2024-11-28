from Visualizations.BubbleChart import BubbleChart
from Visualizations.ColumnChart import ColumnChart
from Visualizations.ChoroplethMap import ChoroplethMap
from Visualizations.HeatMap import HeatMap
from Visualizations.PieChart import PieChart
from Visualizations.ScatterPlot import ScatterPlot

class Model: 
    def __init__(self):
        self.visualizations = {
            'bubble_chart' : BubbleChart(),
            'column_chart' : ColumnChart(),
            'pie_chart' : PieChart(),
            'choropleth_map' : ChoroplethMap(),
            'heat_map' : HeatMap(),
        }

    def set_visualizations(self, aqi_days, pfas_occurances, primary_pollutants, geo_data, health_data): 
        self.add_bubble_chart(pfas_occurances)
        self.add_column_chart(aqi_days)
        self.add_pie_chart(primary_pollutants)
        self.add_choropleth_map(geo_data, health_data, primary_pollutants) 

    def get_visualizations(self):
        return self.visualizations
    
    def update_visualization(self, visual, county, state):
        if visual.get_id() == 1:
            self.update_bubble_chart(visual, county, state) 
        elif visual.get_id() == 2:
            self.update_column_chart(visual, county, state)
        elif visual.get_id() == 3:
            self.update_pie_chart(visual, county, state) 
        elif visual.get_id() == 4:
            self.update_choropleth_map(visual, county, state) 
        elif visual.get_id() == 5:
            self.update_heat_map(visual, county, state) 
    
    def add_bubble_chart(self, pfas_occurances):
        self.visualizations.get('bubble_chart').set_data(pfas_occurances)
        self.visualizations.get('bubble_chart').create_bubble_chart()

    def update_bubble_chart(self, visual, county, state):
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)
        
        self.visualizations.get('bubble_chart').create_bubble_chart()
    
    def add_column_chart(self, aqi_days):
        self.visualizations.get('column_chart').set_data(aqi_days)
        self.visualizations.get('column_chart').create_column_chart() 

    def update_column_chart(self, visual, county, state):
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)

        self.visualizations.get('column_chart').create_column_chart()

    def add_pie_chart(self, primary_pollutant):
        self.visualizations.get('pie_chart').set_data(primary_pollutant)
        self.visualizations.get('pie_chart').create_pie_chart() 

    def update_pie_chart(self, visual, county, state):
        if state == 0:
            visual.remove_from_dict(county) 
        else:
            visual.add_to_dict(county)

        self.visualizations.get('pie_chart').create_pie_chart()

    def add_choropleth_map(self, geospatial, health_data, primary_pollutant):
        self.visualizations.get('choropleth_map').set_data([geospatial, health_data, primary_pollutant])
        self.visualizations.get('choropleth_map').create_choropleth_map()
