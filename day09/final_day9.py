import pandas as pd

df = pd.read_csv("students_missing.csv")
print(df.head(5))
print(df.shape, df.columns, df.dtypes, df.info())
print(df.isna().sum())
average_s = (df["Баллы"].mean()).round(1)
df["Баллы"] = df["Баллы"].fillna(average_s)
average_p = (df["Посещено"].mean()).round(1)
df["Посещено"] = df["Посещено"].fillna(average_p)
print(df)
df["Процент посещаемости"] = df["Посещено"] / 20 * 100
result = df[(df["Баллы"] >= 70) | (df["Посещено"] > 15)]
print(result)
print(df[df["Баллы"] > 80])
df_sort = df.sort_values("Посещено")
print(df_sort)
print(average_s)
print(df["Баллы"].max())
print(df["Баллы"].min())
df_sort = df.reset_index(drop=True)
print(df_sort)
df_sort.to_csv("results.csv", index=False, encoding="utf-8")