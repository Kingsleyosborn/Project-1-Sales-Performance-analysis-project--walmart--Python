import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#Convert "Date" column to datetime

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#Group by Month and summarize sales
monthly_sales = df.groupby('Month')['Total'].sum()
monthly_sales.plot(kind='bar', title="Monthly Revenue")
plt.ylabel("Revenue")
plt.xlabel("Month")
plt.show()
# Group by City and summarize sales
city_sales = df.groupby('City')['Total'].sum()
city_sales.plot(kind='bar', title="Sales by City")
plt.ylabel("Revenue")
plt.xlabel("City")
plt.show()

# Example: Sales by city
df.groupby('City')['Total'].sum().plot(kind='bar', title='Sales by City')
plt.ylabel('Total Revenue')
plt.show()

# Group by Product line and summarize sales


top_products = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
top_products.plot(kind='bar', title="Sales by Product Line")
plt.ylabel("Revenue")
plt.xlabel("Product Line")
plt.show()
# Group by Payment and summarize sales
payment_sales = df.groupby('Payment')['Total'].sum()
payment_sales.plot(kind='bar', title="Sales by Payment Method")
plt.ylabel("Revenue")
plt.xlabel("Payment Method")
plt.show()
# Group by City and Payment and summarize sales
'''city_payment_sales = df.groupby(['City', 'Payment'])['Total'].sum().unstack()
city_payment_sales.plot(kind='bar', stacked=True, title="Sales by City and Payment Method")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.xlabel("City")

plt.show()'''
city_payment_sales = df.groupby(['City', 'Payment'])['Total'].sum().unstack()
city_payment_sales.plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    title="Sales by City and Payment Method"
)
plt.ylabel("Revenue ($)")
plt.xlabel("City")
plt.xticks(rotation=0)
plt.legend(title="Payment Method")
plt.show()

# Example: Rating by product line
sns.barplot(x='Product line', y='Rating', data=df)
plt.xticks(rotation=45)
plt.title('Average Rating by Product Line')
plt.show()

# Make sure your Date column is datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by Date and sum total revenue
daily_sales = df.groupby('Date')['Total'].sum()



# Plot daily sales trend
plt.figure(figsize=(12, 5))
daily_sales.plot(kind='line', title='Daily Sales Trend')
plt.ylabel('Revenue')
plt.xlabel('Date')
plt.grid(True)
plt.tight_layout()
plt.show()
