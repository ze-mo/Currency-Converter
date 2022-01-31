from cassandra.cluster import Cluster
import requests
import time
import itertools
from datetime import datetime
import datetime
import traceback

cluster = Cluster()
session = cluster.connect('forex_data')

API_KEY = '3B2IY9JPDHQ9IZDL'

list_of_permutations = list(itertools.permutations(['BGN', 'GBP', 'USD', 'CNY', 'CHF', 'EUR']))
set_of_pairs = set()
for perm_tuple in list_of_permutations:
    set_of_pairs.add(perm_tuple[0] + perm_tuple[1])

def populate_db(pairs):
    counter = 0
    for pair in pairs:
        url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={pair[:3]}&to_symbol={pair[3:]}&interval=15min&outputsize=compact&apikey={API_KEY}'
        r = requests.get(url)
        data_dict = r.json()
        print(r.status_code)
        try:
            values_by_date = data_dict["Time Series FX (15min)"]
            last_refreshed_api = data_dict["Meta Data"]["4. Last Refreshed"]
            last_refresh_date = datetime.datetime.strptime(last_refreshed_api, '%Y-%m-%d %H:%M:%S')
            for key, value in values_by_date.items():
                key_date_obj = datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
                tdelta = datetime.timedelta(minutes=45)
                limit = last_refresh_date - tdelta
                if key_date_obj > limit:
                    print(f'{key_date_obj} not included')
                    continue
                else:
                    refreshed = key
                    close_value = value["4. close"]
                    session.execute(f"INSERT INTO rates_by_pairs_model (pair, id, exchange_rate, last_refresh) VALUES ('{pair}', now(), {close_value}, '{refreshed}')")
            counter += 1
            print(f'{pair} added...')

        except Exception:
            print(traceback.format_exc())
            print(f'Exception: {pair}')
        
        if counter == 5:
            print('Sleeping 60 seconds...')
            time.sleep(60)
            counter = 0

#'select difference from rates_by_pairs where pair=('EUR', 'JPY') limit 1;'
#'select last_refreshed from rates_by_pairs where pair=('EUR', 'JPY') limit 1;'

if __name__ == "__main__":
    populate_db(set_of_pairs)
    print("Finished")