from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
from typing import List

class ScatterPlot(BaseVisual):
    def __init__(self):
        visualType = Visual.ScatterPlot
        name = 'Visualization #6'
        hasFiltering = False
        hasRadio = False
        hasSorting = False

        super().__init__(visualType, name, hasFiltering, hasRadio, hasSorting)
        self._scatter_data = None

    def get_counties(self) -> List[str]:
        retCounties = [entry.County for entry in self.get_data()[0]]
        return retCounties

    def create_chart(self):
        self.set_scatter_data()

        # Add to the data object
        data = []
        for county in self._scatter_data:
            countyValues = self._scatter_data[county]
            data.append([county, countyValues[0], countyValues[1]])

        medianAqis = [dataPoint[2] for dataPoint in data]
        healthScores = [int(dataPoint[1]) for dataPoint in data]

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(1, 1, 1)
        
        ax.set_title(f"Michigan Counties Medium AQI vs Health Score")
        ax.set_xlabel('Health Score')
        ax.set_ylabel('Median AQI')
        ax.scatter(medianAqis, healthScores, marker='o')
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
