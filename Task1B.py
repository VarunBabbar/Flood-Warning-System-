

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    point = (52.2053, 0.1218)
    list_of_stations=stations_by_distance(stations, point)
    closest=list_of_stations[:10]
    furthest=list_of_stations[-10:]
    print("10 closest station to point P(52.2053, 0.1218): {}".format(closest))
    print("10 furthest station to point P(52.2053, 0.1218): {}".format(furthest))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()