from Enums.Visualization import Visual
from Visualizations.BaseVisual import BaseVisual
from matplotlib.figure import Figure
from typing import List

class HeatMap(BaseVisual):
    def __init__(self):
        visualType = Visual.HeatMap
        name = 'Visualization #5'
        hasFiltering = False
        hasRadio = False
        hasSorting = True

        super().__init__(visualType, name, hasFiltering, hasRadio, hasSorting)
        self._heat_data = None
        self._columns = ["County", "Median AQI", "Health Score"]
        self._selectedSort = self._columns[0]

    def create_chart(self):
        self.set_heat_data()

        # Add to the data object
        data = [self._columns]
        for county in self._heat_data:
            countyValues = self._heat_data[county]
            data.append([county, countyValues.MedianAqi, countyValues.HealthScore])

        figure = Figure(figsize=(17, 12))
        ax = figure.add_subplot(1, 1, 1)
        ax.set_title(f"Michigan Counties\nMedium AQI vs Health Score Heat Map")
        ax.axis('off')

        table = ax.table(
            cellText=data,
            cellLoc='center',
            loc='center'
        )

        # Update each row
        for row in range(0, len(data)):
            countyCell = table[(row, 0)]
            medianAqiCell = table[(row, 1)]
            healthScoreCell = table[(row, 2)]

            cellHeight = .03
            countyCell.set_height(cellHeight)
            medianAqiCell.set_height(cellHeight)
            healthScoreCell.set_height(cellHeight)

            # Hide the health score
            healthScoreCell.set_text_props(text="")

            # Add color to the medium aqi based on health score
            if row >= 1:
                healthScore = float(data[row][2])
                color = None
                if healthScore >= 1:
                    color = "forestgreen"
                elif healthScore >= 0.5:
                    color = "limegreen"
                elif healthScore >= 0:
                    color = "khaki"
                elif healthScore >= -0.5:
                    color = "lightcoral"
                elif healthScore >= -1:
                    color = "indianred"
                else:
                    color = "orangered"
                medianAqiCell.set_facecolor(color)

        table.set_fontsize(12)
        table.auto_set_column_width(col=list(range(len(data[0]))))
        self.set_visual(figure)

    def get_counties(self) -> List[str]:
        retCounties = [entry.County for entry in self.get_data()[0]]
        return retCounties

    def set_heat_data(self) -> None:
        self._heat_data = {}
        data = self.get_data()
        aqi_data = data[0]
        health_data = data[1]

        sortedCounties = sorted(self.get_counties(), key=self.sort_key(aqi_data, health_data))
        for county in sortedCounties:
            matchingCountyMedianAqi = [aqi for aqi in aqi_data if aqi.County == county][0]
            matchingCountyHealthScore = [h for h in health_data if h.County == county][0]
            self._heat_data[county] = HeatMapModel(matchingCountyMedianAqi.MedianAqi, matchingCountyHealthScore.HealthScore)
        
    def sort_key(self, aqi_data, health_data):
        def key_function(county):
            retValue = county
            if self._selectedSort == "County":
                retValue = county
            elif self._selectedSort == "Median AQI":
                matchingCountyMedianAqi = next(aqi for aqi in aqi_data if aqi.County == county)
                retValue = matchingCountyMedianAqi.MedianAqi
            elif self._selectedSort == "Health Score":
                matchingCountyHealthScore = next(h for h in health_data if h.County == county)
                retValue = matchingCountyHealthScore.HealthScore
            return retValue
        return key_function

    def get_sort_options(self) -> List[str]:
        return self._columns
    
    def remove_from_dict(self, value) -> None:
        print(f"This should not be hit. | Value: {value}")

    def add_to_dict(self, value) -> None:
        self._selectedSort = value

class HeatMapModel:
    def __init__(self, medianAqi, healthScore):
        self.MedianAqi = medianAqi
        self.HealthScore = healthScore