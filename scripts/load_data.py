# scripts/load_data.py
from clickhouse_driver import Client
import pandas as pd

# ClickHouse connection details
clickhouse_host = 'localhost'
clickhouse_port = 9000
clickhouse_user = 'admin'
clickhouse_password = 'admin'
clickhouse_database = 'makro_pro'

# File to load
input_file = '../data/sample_data.csv'

# Connect to ClickHouse
client = Client(host=clickhouse_host, port=clickhouse_port, user=clickhouse_user, password=clickhouse_password)

# Create database and table
client.execute('CREATE DATABASE IF NOT EXISTS forex')
client.execute('''
    CREATE TABLE IF NOT EXISTS forex.ticks (
        datetime DateTime,
        currency_pair String,
        bid Float64,
        ask Float64,
        volume UInt64
    ) ENGINE = MergeTree()
    PARTITION BY toYYYYMM(datetime)
    ORDER BY (datetime, currency_pair)
''')

# Load data
df = pd.read_csv(input_file)
client.execute('INSERT INTO forex.ticks VALUES', df.to_dict('records'))
print(f"Data loaded into ClickHouse from {input_file}")