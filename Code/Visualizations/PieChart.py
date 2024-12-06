from Enums.Visualization import Visual
from Models.CountyAirPollutant import CountyAirPollutant
from Visualizations.BaseVisual import BaseVisual
from Visualizations.Helpers.AirPollutantHelper import AirPollutantHelper
from Visualizations.Helpers.ColorHelper import ColorHelper
from collections import Counter
from matplotlib.figure import Figure
import copy 

class PieChart(BaseVisual):
    def __init__(self):
        visualType = Visual.PieChart
        name = 'Visualization #3'
        hasFiltering = False
        hasRadio = True

        super().__init__(visualType, name, hasFiltering, hasRadio)
        self.counties = []
        self.pollutant_data_original = {
            'categories': [],
            'primary_pollutant': []
        }
        self.county_pollutant_data_original = {}
        self.pollutant_data = {}
        self._selectedCounty:CountyAirPollutant = None

    def set_pollutant_data(self):
        self.pollutant_data_original['categories'] = []
        self.pollutant_data_original['primary_pollutant'] = []
        self.county_pollutant_data_original = {}

        for county in self.get_data():
            self.pollutant_data_original['categories'].append(county.County)
            self.pollutant_data_original['primary_pollutant'].append(county.GetPrimaryPollutant().name)

            if self._selectedCounty == None: # Will default to the first county
                self._selectedCounty = county.County

            if self._selectedCounty != None and self._selectedCounty == county.County:
                apHelper = AirPollutantHelper()

                for pollutant in apHelper.GetPollutants():
                    self.county_pollutant_data_original[pollutant.name] = county.GetPollutionCount(pollutant)

        self.counties = self.pollutant_data_original['categories']
        self.pollutant_data = copy.deepcopy(self.pollutant_data_original)

    def get_counties(self):
        return self.counties

    def create_chart(self) -> None:
        self.set_pollutant_data()

        figure = Figure(figsize=(17, 12))
        figure.suptitle('Pie Chart: \nPrimary Pollutants in State of Michigan and Per County')
        
        # State wide values
        axState = figure.add_subplot(1, 2, 1)
        counts, pollutants = self.get_list_of_counts()

        cHelper = ColorHelper()
        pollutantColors = [cHelper.GetColor(p) for p in pollutants]
        axState.set_title(f"Michigan's Statewide Primary Pollutants\n(% of Counties Pollutant was Primary)")
        axState.pie(counts, labels=pollutants, colors=pollutantColors)

        # County specific values
        if self._selectedCounty != None:
            axCounty = figure.add_subplot(1, 2, 2)

            pollutants = []
            counts = []

            for pollutant in self.county_pollutant_data_original:
                value = int(self.county_pollutant_data_original[pollutant])

                # Only displaying pollutants that have at least 1 day
                if value > 0:
                    pollutants.append(pollutant)
                    counts.append(value)

            cHelper = ColorHelper()
            pollutantColors = [cHelper.GetColor(p) for p in pollutants]
            axCounty.set_title(f"{self._selectedCounty} County's Primary Air Pollutants\n(% of Days Pollutant was Primary)")
            axCounty.pie(counts, labels=pollutants, colors=pollutantColors)

        self.set_visual(figure)

    def get_list_of_counts(self) -> None:
        counts = []
        pollutants = [] 
        counter = Counter(self.pollutant_data['primary_pollutant'])

        for key, item in counter.items():
            pollutants.append(key)
            counts.append(item)

        return counts, pollutants
    
    def remove_from_dict(self, county) -> None:
        print(f"This should not be hit. | County: {county}")

    def add_to_dict(self, county) -> None:
        self._selectedCounty = county
