from Visualizations.Visualization import Visualization
from matplotlib.figure import Figure
import copy 
from collections import Counter

class PieChart(Visualization):
    def __init__(self, id= 3, name = 'Visualization #3', visual = None, data = None):
        super().__init__(id, name, visual, data)
        self.counties = []
        self.pollutant_data_original = {
            'categories' : [],
            'primary_pollutant' : []
        }
        self.pollutant_data = {}  

    def set_pollutant_data(self):
        for county in self.data:
            self.pollutant_data_original['categories'].append(county.County)
            self.pollutant_data_original['primary_pollutant'].append(county.GetPrimaryPollutant().name)

        self.counties = self.pollutant_data_original['categories']
        self.pollutant_data = copy.deepcopy(self.pollutant_data_original)

    def get_counties(self):
        return self.counties

    def create_pie_chart(self):
        if self.pollutant_data_original['categories'] == []:
            self.set_pollutant_data()

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(111)

        counts, pollutants = self.get_list_of_counts()
        ax.pie(counts, labels = pollutants)

        self.visual = figure 

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