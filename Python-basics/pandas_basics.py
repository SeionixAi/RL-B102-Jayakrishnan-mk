import pandas as pd;

# df = pd.DataFrame(data);
# print(df);

# read csv
df = pd.read_csv('data.csv');
print(df.head());

# print("Available columns:", df.columns.tolist())
# print(df["Age"].mean())

# print(df["Marks"].max())

# print(df[df["Age"] > 22]);
