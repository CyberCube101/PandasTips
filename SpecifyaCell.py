import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
print(drinks.head())

print(drinks.iloc[4, 1])

print(drinks.loc['Angola', drinks.columns[1]])
