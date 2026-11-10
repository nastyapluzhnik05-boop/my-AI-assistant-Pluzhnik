import pandas as pd
df = pd.DataFrame({"Группа":["A","B"],"Баллы":[70,90]})
result = df.groupby("Группа")["Баллы"].mean().reset_index()
print(result.shape)


