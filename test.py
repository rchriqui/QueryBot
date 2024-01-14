import pandas as pd
df=pd.read_csv('best_countries_2024.csv')
for col in df.columns:
    print(col)