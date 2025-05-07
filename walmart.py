import pandas as pd

df = pd.read_csv('Walmart Sales Data.csv')

print('First 5 rows of the dataset:')
print(df.head())

print('info')
# Get general info (rows, columns, data types)
df.info()

print('describe')
# Summary statistics
print(df.describe())

print('isnull')
# Check for missing values
print(df.isnull().sum())
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)

'''print(df.columns)

print(df['City'].value_counts())
print(df['Product line'].value_counts())
print(df['Payment'].value_counts())'''
city_sales = df.groupby('City')['Total'].sum()
print(city_sales)
