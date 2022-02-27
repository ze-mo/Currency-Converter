import requests
import time
import itertools
import logging
import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

mycursor = conn.cursor()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(name)s | %(message)s')

file_handler = logging.FileHandler("db_population.log")
error_file_handler = logging.FileHandler("db_population.log")

file_handler.setLevel(logging.INFO)
error_file_handler.setLevel(logging.ERROR)

error_file_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(error_file_handler)

list_of_currencies = ['BGN', 'GBP', 'USD', 'CHF', 'EUR']
list_of_permutations = list(itertools.permutations(list_of_currencies))
set_of_paired_currencies = set()
for perm_tuple in list_of_permutations:
    set_of_paired_currencies.add(perm_tuple[0] + perm_tuple[1])

def populate_db(pairs):
    """Submits a request to the Alphavantage API with the parameters set for each permutation of the currencies list.
    After the data is retrieved, it's upserted into the forex_ratesbypairs table, where each record represents a currency pair 
    with its exchange rate. Realtime rates are updated every 6 minutes."""

    counter = 0
    for pair in pairs:
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={pair[:3]}&to_currency={pair[3:]}&apikey={os.environ.get('FOREX_API_KEY')}"
        r = requests.get(url)
        data_dict = r.json()
        logger.info(r.status_code)
        try:
            realtime_rate = data_dict["Realtime Currency Exchange Rate"]
            last_refreshed_value = realtime_rate["6. Last Refreshed"]
            exchange_rate = realtime_rate["5. Exchange Rate"]
            mycursor.execute(f"INSERT INTO forex_ratesbypairs (pair, last_refreshed, exchange_rate) VALUES ('{pair}', '{last_refreshed_value}', {exchange_rate}) ON CONFLICT (pair) DO UPDATE SET last_refreshed=EXCLUDED.last_refreshed, exchange_rate=EXCLUDED.exchange_rate")
            conn.commit()
            counter += 1
            logger.info(f'{pair} Added... ')


        except Exception as e:
            logger.exception(e)

        if counter == 5:
            logger.info('Sleeping 60 seconds... ')
            time.sleep(60)
            counter = 0

if __name__ == "__main__":
    while True:
        populate_db(set_of_paired_currencies)
