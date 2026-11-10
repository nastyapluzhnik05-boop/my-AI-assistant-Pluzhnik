import pandas as pd

df = pd.read_csv("result.csv")
print(df)

df["Процент посещаемости"] = df["Посещено"] / 20 * 100
print(df)
sort_scores = df[df["Баллы"] >= 70]
df_sort = sort_scores.sort_values("Баллы", ascending=False)
print(df_sort)
df_sort.to_csv("sort_result.csv", index=False, encoding="utf-8")
