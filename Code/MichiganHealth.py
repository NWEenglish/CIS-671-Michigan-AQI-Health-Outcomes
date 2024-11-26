from Providers.DataProvider import DataProvider as dp
from Enums.AqiStdMeasure import AqiStandard as aqi
from Models.CountyAqiDays import CountyAqiDays
from View import View 
from Model import Model 
from tkinter import *  

def main():
    print("Starting application.")

    aqi_days = dp.GetAqiDays()
    primary_pollutants = dp.GetPrimaryPollutants()
    health_data = dp.GetHealthData()
    pfas_occurances = dp.GetPfasOccurances()

    #Tkinter documentation https://tkdocs.com/tutorial/index.html 
    print('Starting main frame')
    root = Tk() 
    root.title('Michigan Health')
    
    print('Creating model')
    model = Model()
    model.set_visualizations(aqi_days, pfas_occurances, primary_pollutants)

    print('Creating view')
    view = View(root, model)
    view.run_display()

if __name__ == "__main__":
    main()