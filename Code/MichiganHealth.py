from Providers.DataProvider import DataProvider as dp
from View import View 
from Model import Model 
import tkinter as tk

def main():
    print("Starting application.")

    aqi_days = dp.GetAqiDays()
    primary_pollutants = dp.GetPrimaryPollutants()
    health_data = dp.GetHealthData()
    pfas_occurances = dp.GetPfasOccurances()
    geo_data = dp.GetGeoSpatialData()

    #Tkinter documentation https://tkdocs.com/tutorial/index.html 
    print('Starting main frame')
    root = tk.Tk() 
    root.title('Michigan Health')
    root.state('zoomed')
    root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
    root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
    
    print('Creating model')
    model = Model()
    model.set_visualizations(aqi_days, pfas_occurances, primary_pollutants, geo_data, health_data)

    print('Creating view')
    view = View(root, model)
    view.run_display()

if __name__ == "__main__":
    main()
