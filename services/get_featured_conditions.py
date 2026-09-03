from services.get_featured_station import (
    get_featured_station
)


def get_featured_conditions():

    return {
        "deep_water":
            get_featured_station(
                "DEEP_WATER"
            ),

        "surface":
            get_featured_station(
                "SURFACE"
            ),

        "inflow":
            get_featured_station(
                "INFLOW"
            ),

        "outflow":
            get_featured_station(
                "OUTFLOW"
            ),

        "ecoli":
            get_featured_station(
                "ECOLI"
            ),

        "ditch":
            get_featured_station(
                "DITCH"
            )
    }