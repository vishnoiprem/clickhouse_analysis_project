# scripts/generate_data.py
import pandas as pd
import numpy as np
import os

# Parameters
num_rows = 100000000
output_file = '../data/sample_data.csv'

# Generate sample data
def generate_data(num_rows):
    dates = pd.date_range(start='2023-01-01', periods=num_rows // 1000, freq='T')
    currency_pairs = ['USD/JPY', 'EUR/JPY']
    data = {
        'datetime': np.random.choice(dates, num_rows),
        'currency_pair': np.random.choice(currency_pairs, num_rows),
        'bid': np.random.uniform(100, 150, num_rows),
        'ask': np.random.uniform(100, 150, num_rows),
        'volume': np.random.randint(1, 1000, num_rows)
    }
    df = pd.DataFrame(data)
    return df

# Save data to CSV
if not os.path.exists('../data'):
    os.makedirs('../data')

df = generate_data(num_rows)
df.to_csv(output_file, index=False)
print(f"Generated data saved to {output_file}")
