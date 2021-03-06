import requests
import time
import cx_Oracle
import json

i = 1
while True:
    str1 = 'https://web-api.coinmarketcap.com/v1.1/cryptocurrency/quotes/historical?convert=USD,BTC&format=chart_crypto_details&interval=1h&time_end=1598092056&time_start=1595413656&id='
    str2 = str1 + str(i)
    response = requests.get(str2)
    query = 'INSERT INTO table_name (column_name) values (:column_name)'
    if response.status_code == 200: # only connects to database if request made is successfull.
        plaindata = json.dumps(response.json(), sort_keys=True, separators=(',', ': '))
        conn = cx_Oracle.connect('Username/Password@hostname/sid')
        cursor = conn.cursor()
        cursor.execute(query,json_data = plaindata)
        conn.commit()
    time.sleep(86400) # no of seconds in a day so that the api gets called every day.
    i += 1
