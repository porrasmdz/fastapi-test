import clickhouse_connect

from clickhouse_driver import Client

DB_HOST='clickhouse'
DB_PORT='8123'
DB_USER='default'
DB_PASSWORD=''
client = Client(host=DB_HOST)
# clickhouse_connect.get_client(host=DB_HOST, port=DB_PORT,username=DB_USER)
