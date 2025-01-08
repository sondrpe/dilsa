import pandas as pd
import numpy as np

# Load the datasets with specified encoding
amazon = pd.read_csv("./Amazon-GoogleProducts/Amazon.csv", encoding='ISO-8859-1')
google = pd.read_csv("./Amazon-GoogleProducts/GoogleProducts.csv", encoding='ISO-8859-1')

"""
    Cleaninig the data
"""
# Remove duplicates from both datasets
amazon = amazon.drop_duplicates()
google = google.drop_duplicates()

# Replace NaN values in the 'description' column with 'no description'
amazon['description'] = amazon['description'].fillna('no description')

# Filter rows where any column except 'description' is NaN
filtered_rows = amazon[amazon.drop(columns=['description']).isnull().any(axis=1)]

# Display the filtered rows
dfOhneDescription = amazon.drop(columns=['description'])
empty_ohne = dfOhneDescription[dfOhneDescription.isnull().any(axis=1)]
#print(empty_ohne)
#print(dfOhneDescription.iloc[0])

# View rows where price is 0 in Amazon
zero_price_rows = amazon[amazon['price'] == 0]
print(zero_price_rows)
# NO NULL VALUES IN GOOGLES PRICES

