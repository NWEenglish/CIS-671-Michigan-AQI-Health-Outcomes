from Enums.AqiStdMeasure import AqiStandard as aqi
from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
import numpy as np
import copy

class ColumnChart(BaseVisual):
    def __init__(self):
        visualType = Visual.ColumnChart
        name = 'Visualization #2'
        hasFiltering = True
        
        super().__init__(visualType, name, hasFiltering)
        self.counties = []  
        self.aqi_data_original = {
            'categories': [],
            'good_days': [],
            'moderate_days': [],
            'unhealthy_for_sensitive_groups_days': [],
            'unhealthy_days': [],
            'very_unhealthy_days': [],
            'hazardous_days': []    
        } 
        self.aqi_data = {} 

    def set_aqi_data(self):
        for county in self.get_data():    
            self.aqi_data_original['categories'].append(county.County)
            self.aqi_data_original['good_days'].append(county.GetAqiDays(aqi.GoodDay).astype(float))
            self.aqi_data_original['moderate_days'].append(county.GetAqiDays(aqi.ModerateDay).astype(float)) 
            self.aqi_data_original['unhealthy_for_sensitive_groups_days'].append(county.GetAqiDays(aqi.UnhealthyForSensitiveGroupsDay).astype(float)) 
            self.aqi_data_original['unhealthy_days'].append(county.GetAqiDays(aqi.UnhealthyDay).astype(float))
            self.aqi_data_original['very_unhealthy_days'].append(county.GetAqiDays(aqi.VeryUnhealthyDay).astype(float))
            self.aqi_data_original['hazardous_days'].append(county.GetAqiDays(aqi.HazardousDays).astype(float))  

        self.counties = self.aqi_data_original['categories']
        self.aqi_data = copy.deepcopy(self.aqi_data_original)

    def get_aqi_data(self):
        return self.aqi_data
    
    def get_counties(self):
        return self.counties 

    def create_column_chart(self):
        if self.aqi_data_original['categories'] == []:
            self.set_aqi_data()
        
        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(111)
        
        total_days = np.array(self.aqi_data['good_days']) + np.array(self.aqi_data['moderate_days']) + np.array(self.aqi_data['unhealthy_for_sensitive_groups_days']) + np.array(self.aqi_data['unhealthy_days']) + np.array(self.aqi_data['very_unhealthy_days']) + np.array(self.aqi_data['hazardous_days'])
        good_days_percent = (np.array(self.aqi_data['good_days']) / total_days) * 100
        moderate_days_percent = (np.array(self.aqi_data['moderate_days']) / total_days) * 100
        unhealthy_for_sensitive_groups_days_percent = (np.array(self.aqi_data['unhealthy_for_sensitive_groups_days']) / total_days) * 100
        unhealthy_days_percent = (np.array(self.aqi_data['unhealthy_days']) / total_days) * 100
        very_unhealthy_days_percent = (np.array(self.aqi_data['very_unhealthy_days']) / total_days) * 100
        hazardous_days_percent = (np.array(self.aqi_data['hazardous_days']) / total_days) * 100

        bar_width = .1
        pos = np.arange(len(self.aqi_data['categories']))

        ax.bar(pos, good_days_percent, bar_width, color='blue')
        ax.bar(pos + bar_width, moderate_days_percent, bar_width, color='green')
        ax.bar(pos + (bar_width*2), unhealthy_for_sensitive_groups_days_percent, bar_width, color='orange')
        ax.bar(pos + (bar_width*3), unhealthy_days_percent, bar_width, color='yellow')
        ax.bar(pos + (bar_width*4), very_unhealthy_days_percent, bar_width, color='red')
        ax.bar(pos + (bar_width*5), hazardous_days_percent, bar_width, color='black')

        ax.set_title('Percent AQI Number of Days v. Michigan Counties')
        ax.set_xlabel('Michigan Counties')
        ax.set_ylabel('Percent AQI Number of Days')

        ax.set_ylim(0, 100)
        ax.set_yticks(np.arange(0, 101, 10))

        ax.set_xticks(pos)
        ax.set_xticklabels(self.aqi_data['categories'], rotation=45)

        ax.legend(['Good Days', 'Moderate Days', 'Unhealthy for Sensitive Groups Days', 'Unhealthy_Days', 'Very Unhealthy Days', 'Hazardous Days'], loc='upper left') 

        self.set_visual(figure)

    def remove_from_dict(self, county):
        if county in self.aqi_data['categories']:
            index = self.aqi_data['categories'].index(county)

        for key in self.aqi_data:
            self.aqi_data[key].pop(index)

    def add_to_dict(self, county):
        if county not in self.aqi_data['categories']:
            if county in self.aqi_data_original['categories']:
                index = self.aqi_data_original['categories'].index(county)

        for key in self.aqi_data:
            self.aqi_data[key].insert(index, self.aqi_data_original[key][index])
