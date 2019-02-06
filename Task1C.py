
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    reference_coordinate = (52.2053, 0.1218)
    r = 10
    stations = build_station_list()
    return stations_within_radius(stations,reference_coordinate, r) #Prints the stations located within 10km of the desired coordinate
print(run())
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()


