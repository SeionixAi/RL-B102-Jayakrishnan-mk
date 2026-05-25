import os
import pandas as pd
import numpy as np

np.random.seed(1)
rows = 200

df = pd.DataFrame({
    "PassengerId": np.arange(1, rows + 1),
    "Name": np.random.choice(["Mr. John", "Mrs. Anna", "Miss Emma", "Dr. Smith"], rows),
    "Age": np.random.choice(np.append(np.random.randint(1, 80, 180), [np.nan]*20), rows),
    "Sex": np.random.choice(["male", "female"], rows),
    "Pclass": np.random.choice([1, 2, 3], rows),
    "Fare": np.round(np.random.uniform(10, 500, rows), 2)
})

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data.csv')
print(csv_path) # c:/JK_The_DISK/ML/Pandas/pandas_practice/day4/data.csv

df2 = pd.read_csv(csv_path)

# ........................................................................................................

# 20. Merging DataFrames

# df = pd.merge(df, df2, on='PassengerId', how="left")
# print(df)

# 21. Concatenating DataFrames

# df_combined = pd.concat([df,df2], axis=0);
# print(df_combined);

# 22. Pivot Table

# print(pd.pivot_table(df, values='Fare', index='Pclass', columns='Sex', aggfunc='mean'));

# 23. Resetting and Setting Index

# df.reset_index(drop=True, inplace=True);
# df.set_index('PassengerId', inplace=True)

# 24. Conditional Column Creation

# df['AgeGroup'] = df['Age'].apply(lambda x: 'senior' if x > 50 else 'youth')
# print(df)

# 25. Save Cleaned Data

# df.to_csv("c:/JK_The_DISK/ML/Pandas/pandas_practice/day4/cleaned_titanic.csv", index=False);
# df.to_excel("c:/JK_The_DISK/ML/Pandas/pandas_practice/day4/cleaned_titanic.xlsx", index=False)