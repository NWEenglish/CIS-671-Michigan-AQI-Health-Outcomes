from Visualizations.Visualization import Visualization
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
import pandas as pd

class ChoroplethMap(Visualization):
    def __init__(self, id= 4, name = 'Visualization #4', visual = None, data = None):
        super().__init__(id, name, visual, data)
        self.healthpollutant_data = {
            'county' : [],
            'health_outcome' : [],
            'health_factors' : [],
            'quality_of_life' : [],
            'health_score' : [],
            'primary_pollutant' : [], 
        } 
        self.geohealthpollutant_data = None 
        self.locations = []

    def get_locations(self):
        return self.locations

    def set_geohealthpollutant_data(self):
        geo = self.data[0]
        health = self.data[1]
        pollutants = self.data[2]

        for county in pollutants:
            self.healthpollutant_data['county'].append(county.County)
            self.healthpollutant_data['primary_pollutant'].append(county.GetPrimaryPollutant().value)

        for county in health: 
            if county.County in self.healthpollutant_data['county']:
                self.healthpollutant_data['health_outcome'].append(county.HealthOutcome)
                self.healthpollutant_data['health_factors'].append(county.HealthFactors)
                self.healthpollutant_data['quality_of_life'].append(county.QualityOfLife)
                self.healthpollutant_data['health_score'].append(county.HealthScore)

        color_map = {1 : 'orange', 2 : 'yellow', 3 :  'blue', 4 : 'red', 5 : 'green'}
        df = pd.DataFrame(self.healthpollutant_data)
        df['color'] = df['primary_pollutant'].map(color_map)
        
        self.geohealthpollutant_data = geo.merge(df, left_on='Name', right_on='county', how='left') 
        self.geohealthpollutant_data['center_marker'] = self.geohealthpollutant_data.geometry.centroid 
        self.geohealthpollutant_data['color'] = self.geohealthpollutant_data['color'].fillna('gray')

    def create_choropleth_map(self):
        if self.geohealthpollutant_data == None:
            self.set_geohealthpollutant_data()

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(111)
        ax.set_title('Michigan Counties', fontsize=16)
        
        handles = []
        colors = ['orange', 'yellow', 'blue', 'red', 'green']
        pollutants = ['CO', 'NO2', 'Ozone', 'PM25', 'PM10']
        for i in range(len(colors)):
            handles.append(mpatches.Patch(color=colors[i], label=pollutants[i]))

        ax.legend(handles=handles, loc='upper right')
        self.geohealthpollutant_data.plot(ax = ax, color = self.geohealthpollutant_data['color'], edgecolor='black')

        for index, row in self.geohealthpollutant_data.iterrows():
            if pd.notna(row['primary_pollutant']): 
                center_marker = row['center_marker'] 
                ax.plot(center_marker.x, center_marker.y, marker='o', color='black', markersize=5)
                self.locations.append({'x': center_marker.x, 'y': center_marker.y, 'County': row['county'], 'Health Outcome': row['health_outcome'], 'Health Factors' : row['health_factors'], 'Quality Of Life' : row['quality_of_life'], 'Health Score' : row['health_score']})

        self.visual = figure  
        