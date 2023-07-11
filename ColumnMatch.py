import pandas as pd

y = "nuts118nm"
x = "compressed"



df = pd.read_csv("mergedpostcodes.csv")


y_values = set(df[y].tolist())
y_values = list(y_values)


for i in (y_values):
    df2 = df[df[y].isin([i])]
    print(i + " = " + str(df2[x].tolist()))

