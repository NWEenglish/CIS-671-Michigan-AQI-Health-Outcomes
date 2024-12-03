from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from Visualizations.Helpers.ColorHelper import ColorHelper
from collections import Counter
from matplotlib.figure import Figure
import copy 

class PieChart(BaseVisual):
    def __init__(self):
        visualType = Visual.PieChart
        name = 'Visualization #3'
        hasFiltering = True

        super().__init__(visualType, name, hasFiltering)
        self.counties = []
        self.pollutant_data_original = {
            'categories': [],
            'primary_pollutant': []
        }
        self.pollutant_data = {}  

    def set_pollutant_data(self):
        for county in self.get_data():
            self.pollutant_data_original['categories'].append(county.County)
            self.pollutant_data_original['primary_pollutant'].append(county.GetPrimaryPollutant().name)

        self.counties = self.pollutant_data_original['categories']
        self.pollutant_data = copy.deepcopy(self.pollutant_data_original)

    def get_counties(self):
        return self.counties

    def create_chart(self):
        if self.pollutant_data_original['categories'] == []:
            self.set_pollutant_data()

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(111)

        counts, pollutants = self.get_list_of_counts()

        cHelper = ColorHelper()
        pollutantColors = [cHelper.GetColor(p) for p in pollutants]
        ax.pie(counts, labels=pollutants, colors=pollutantColors)

        self.set_visual(figure)

    def get_list_of_counts(self):
        counts = []
        pollutants = [] 
        counter = Counter(self.pollutant_data['primary_pollutant'])

        for key, item in counter.items():
            pollutants.append(key)
            counts.append(item)

        return counts, pollutants

    def remove_from_dict(self, county):
        if county in self.pollutant_data['categories']:
            index = self.pollutant_data['categories'].index(county)

        for key in self.pollutant_data:
            self.pollutant_data[key].pop(index)

    def add_to_dict(self, county):
        if county not in self.pollutant_data['categories']:
            if county in self.pollutant_data_original['categories']:
                index = self.pollutant_data_original['categories'].index(county)

        for key in self.pollutant_data:
            self.pollutant_data[key].insert(index, self.pollutant_data_original[key][index])
