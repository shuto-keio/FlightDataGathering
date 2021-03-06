import datetime
import pytz
from src.spire.historicalapi import QueryGetManager


def main():
    time_interval_start = datetime.datetime(year=2019, month=9, day=1, hour=0, minute=0, second=0, tzinfo=pytz.utc)
    time_interval_stop = datetime.datetime(year=2019, month=9, day=2, hour=0, minute=0, second=0, tzinfo=pytz.utc)
    query_time_interval = datetime.timedelta(hours=1)
    callsign = 'ANA1'
    save_s3 = True
    remove_local_file = False
    processes = 6

    query_get_manager = QueryGetManager()
    list_dict = query_get_manager.query_request(time_interval_start,
                                                time_interval_stop,
                                                icao_address=None,
                                                callsign=callsign,
                                                latitude_between=None,
                                                longitude_between=None,
                                                altitude_baro_between=None,
                                                ingestion_time_interval=None,
                                                query_time_interval=query_time_interval,
                                                )
    print(list_dict)
    list_path = query_get_manager.get_data_bulk(max_wait_time=60,
                                                random_wait=True,
                                                processes=processes,
                                                save_s3=save_s3,
                                                remove_local_file=remove_local_file)
    print(list_path)


if __name__ == '__main__':
    main()