from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
from typing import List

class ScatterPlot(BaseVisual):
    def __init__(self):
        visualType = Visual.ScatterPlot
        name = 'Visualization #6'
        hasFiltering = True
        hasRadio = False
        hasSorting = False
        hasDefaultFilteringAll = False

        super().__init__(visualType, name, hasFiltering, hasRadio, hasSorting, hasDefaultFilteringAll)
        self._scatter_data = None
        self._highlighted_counties = []

    def get_counties(self) -> List[str]:
        retCounties = [entry.County for entry in self.get_data()[0]]
        return retCounties

    def create_chart(self):
        self.set_scatter_data()

        # Add to the data objects
        data = []
        highlighted_data = []
        for county in self._scatter_data:
            countyValues = self._scatter_data[county]
            dataPoint = [county, countyValues[0], countyValues[1]]

            if county in self._highlighted_counties:
                highlighted_data.append(dataPoint)
            else:
                data.append(dataPoint)

        medianAqis = [dataPoint[2] for dataPoint in data]
        healthScores = [int(dataPoint[1]) for dataPoint in data]

        highlightedMedianAqis = [dataPoint[2] for dataPoint in highlighted_data]
        highlightedHealthScores = [int(dataPoint[1]) for dataPoint in highlighted_data]

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(1, 1, 1)
        
        ax.set_title(f"Michigan Counties Medium AQI vs Health Score")
        ax.set_xlabel('Health Score')
        ax.set_ylabel('Median AQI')

        if len(medianAqis) > 0:
            ax.scatter(medianAqis, healthScores, marker='o', color='blue')
        if len(highlightedMedianAqis) > 0:
            ax.scatter(highlightedMedianAqis, highlightedHealthScores, marker='s', color='red')

        self.set_visual(figure)

    def set_scatter_data(self) -> None:
        self._scatter_data = {}
        data = self.get_data()
        aqi_data = data[0]
        health_data = data[1]

        sortedCounties = self.get_counties()
        for county in sortedCounties:
            matchingCountyMedianAqi = [aqi for aqi in aqi_data if aqi.County == county][0]
            matchingCountyHealthScore = [h for h in health_data if h.County == county][0]
            self._scatter_data[county] = (matchingCountyMedianAqi.MedianAqi, matchingCountyHealthScore.HealthScore)

    def remove_from_dict(self, county):
        if county in self.get_counties() and county in self._highlighted_counties:
            self._highlighted_counties.remove(county)

    def add_to_dict(self, county):
        if county in self.get_counties() and county not in self._highlighted_counties:
            self._highlighted_counties.append(county)
