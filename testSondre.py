import pandas as pd
import numpy as np
import sqlite3

# Load the datasets with specified encoding
amazon = pd.read_csv("./Amazon-GoogleProducts/Amazon.csv", encoding='ISO-8859-1')
google = pd.read_csv("./Amazon-GoogleProducts/GoogleProducts.csv", encoding='ISO-8859-1')

def amazon_query(query):
    conn = sqlite3.connect('Amazon.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def google_query(query):
    conn = sqlite3.connect('Google.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

"""Create tables for 
    Amazon and Google databases"""
conn = sqlite3.connect('Amazon.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Amazon (
    id TEXT,
    title TEXT,
    description TEXT,
    manufacturer TEXT,
    price TEXT
)
''')
amazon.to_sql('Amazon', conn, if_exists='replace', index=False)
conn.close()

# Table for Google database
conn = sqlite3.connect('Google.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Google (
    id TEXT,
    name TEXT,
    description TEXT,
    manufacturer TEXT,
    price TEXT
)
''')

google.to_sql('Google', conn, if_exists='replace', index=False)
conn.close()

empty_amazon = amazon[amazon.isnull().any(axis=1)]
print(empty_amazon)

empty_amazon = amazon_query("SELECT * FROM Amazon WHERE id = NULL OR title = NULL OR description = NULL OR manufacturer = NULL OR price = NULL")
empty_google = google_query("SELECT * FROM Google WHERE id = '' OR name = '' OR description = '' OR manufacturer = '' OR price = ''")
test = amazon_query("SELECT * FROM Amazon limit 1")
print(test)
print(empty_amazon)
print(empty_google)
# amazon.fillna("", inplace=True)
# google.fillna("", inplace=True)

"""
    Cleaninig the data
"""

# Replace NaN values in the 'description' column with 'no description'
amazon['description'] = amazon['description'].fillna('no description')

