import sqlite3
import pandas as pd


def get_profile_data(
    station_id,
    sample_date
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    df = pd.read_sql_query(
        """
        SELECT
            depth,
            characteristic_name,
            value,
            unit
        FROM profile_observations
        WHERE monitoring_location_id = ?
        AND sample_date = ?
        """,
        conn,
        params=(
            station_id,
            sample_date
        )
    )

    conn.close()

    return df