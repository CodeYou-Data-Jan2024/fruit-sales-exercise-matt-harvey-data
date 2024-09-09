import pandas as pd

df = pd.DataFrame({'': ['2017 Sales', '2018 Sales'], 'Apples': [35, 41], 'Bananas': [21, 34]})

df = df.set_index('')

print(df.head())

df.to_csv('fruit.csv')