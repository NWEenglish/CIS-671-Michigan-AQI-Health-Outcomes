from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from Modules.BubbleChart import BubbleChart as Bubble
from matplotlib.figure import Figure
import copy

class BubbleChart(BaseVisual):
    def __init__(self):
        visualType = Visual.BubbleChart
        name = 'Visualization #1'
        hasFiltering = True

        super().__init__(visualType, name, hasFiltering) 
        self.counties = []
        self.pfas_data_original = {
            'categories': [],
            'occurances': [],
            'colors': ['#5A69AF', '#579E65', '#F9C784', '#FC944A', '#F24C00', 
                '#00B825','#E3D55B', '#A03D6B', '#69A6A6', '#B29D56', '#A33F49', 
                '#F59C42', '#D1D129', '#BC8A3C', '#C9D02D', '#3F8E91', '#FF7360',  
                '#5F6464', '#FC6F47', '#45A77D', '#62C2A2', '#FFC300', '#0B2F3A', 
                '#9E0A3F', '#850E5A', '#ACB433', '#4B8C7C', '#009B77', '#F44336', 
                '#8D93E4', '#76AB8A', '#E6B0A8', '#13A8D1', '#6D6A7F', '#7053D4', 
                '#00C3A0', '#8D74C1', '#9A3F0C', '#BDA8F6', '#23A8B5', '#6F9B43', 
                '#AB69E0', '#E4E728', '#42A1F2', '#E68271', '#D85474', '#9FB122', 
                '#5B0A75', '#0A9E1E', '#5E6876', '#D1B13D', '#81E2C7', '#51A9E3', 
                '#FAB97E', '#A1B95C', '#E19C6A', '#3F94D4', '#9C87AE', '#D6827C', 
                '#9A9F46', '#F08482', '#367BAF', '#0F8A85', '#FD5A56', '#76D285', 
                '#B6634B', '#D0A9E0', '#EF7F33'
            ]
        }
        self.pfas_data = {} 

    def set_pfas_data(self):
        for county in self.get_data():
            self.pfas_data_original['categories'].append(county.County)
            self.pfas_data_original['occurances'].append(county.Occurances)

        self.counties = self.pfas_data_original['categories']
        self.pfas_data = copy.deepcopy(self.pfas_data_original)

    def get_counties(self):
        return self.counties

    def create_chart(self):
        if self.pfas_data_original['categories'] == []:
            self.set_pfas_data()

        #https://towardsdatascience.com/i-found-a-hidden-gem-in-matplotlibs-library-packed-bubble-charts-in-python-d0f5d892beb7
        bubble_chart = Bubble(area=self.pfas_data['occurances'], bubble_spacing=0.1)
        bubble_chart.collapse()

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(111)

        bubble_chart.plot(ax, self.pfas_data['categories'], self.pfas_data['colors'])
        
        ax.axis("off")
        ax.autoscale_view()
        ax.set_title('PFAS Occurances Per County')

        self.set_visual(figure)

    def remove_from_dict(self, county):
        if county in self.pfas_data['categories']:
            index = self.pfas_data['categories'].index(county)

        for key in self.pfas_data:
            self.pfas_data[key].pop(index)

    def add_to_dict(self, county):
        if county not in self.pfas_data['categories']:
            if county in self.pfas_data_original['categories']:
                index = self.pfas_data_original['categories'].index(county)

        for key in self.pfas_data:
            self.pfas_data[key].insert(index, self.pfas_data_original[key][index])
