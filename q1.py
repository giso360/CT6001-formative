import pandas as pd

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', None)

df = pd.read_csv("./questions/car.data", index_col=0)
# 1.	print the first and last 5 rows
print("# 1.	print the first and last 5 rows")
print(df.head())
print("================")
print(df.tail())

print(df.shape)
print(df.columns)

# 2.	count the number of companies
print("\n # 2.	count the number of companies")
# print(companies)
# print(len(companies))
companies = df['company'].nunique()

# 3.	print the rows that contain toyota cars
print("\n3.	print the rows that contain toyota cars")

df = df[df['company'] == 'toyota']
print(df.shape)
print(df.head(10))

# 4.	print the number of car/models per company
print("\n4.	print the number of car/models per company")

df = pd.read_csv("./questions/car.data", index_col=0)
df = df['body-style'].groupby(df['company']).count()
print(df.head(20))

# 5.	find the most expensive car per company
print("\n5.	find the most expensive car per company")
df = pd.read_csv("./questions/car.data", index_col=0)
grouped_df = df.groupby("company")["price"].max()
print(grouped_df)


# 6.	what is the most expensive car?  Show the car and the price
print("\n6.	what is the most expensive car?  Show the car and the price")
df = df[df['price'] == df['price'].max()]

print(df.head(20))





