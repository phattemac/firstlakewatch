from config.first_lake_zone import FIRST_LAKE_ZONE


def is_in_first_lake_zone(latitude, longitude):

    return (
        FIRST_LAKE_ZONE["min_lat"]
        <= latitude
        <= FIRST_LAKE_ZONE["max_lat"]
        and
        FIRST_LAKE_ZONE["min_lon"]
        <= longitude
        <= FIRST_LAKE_ZONE["max_lon"]
    )