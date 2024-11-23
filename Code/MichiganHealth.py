from Providers.DataProvider import DataProvider as dp
from Enums.AqiStdMeasure import AqiStandard as aqi
from Models.CountyAqiDays import CountyAqiDays

def main():
    print("Starting application.")

    # data = dp.GetAqiDays()
    # data = dp.GetPrimaryPollutants()
    # data = dp.GetHealthData()
    data = dp.GetPfasOccurances()
    
    for county in data:
        # print(f"{county.County}: {county.GetAqiDays(aqi.GoodDay)}")
        # print(f"{county.County}: {county.GetPrimaryPollutant()}")
        print(f"{county.County}: {county.Occurances}")

if __name__ == "__main__":
    main()