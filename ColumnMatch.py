import pandas as pd

y = "nuts118nm"
x = "compressed"



df = pd.read_csv("mergedpostcodes.csv")


y_values = set(df[y].tolist())
y_values = list(y_values)

finallist = []

for i in (y_values):
    df2 = df[df[y].isin([i])]
    #print(i + " = " + str(df2[x].tolist()))
    finallist.append([i,str(df2[x].tolist())])

finaldf = pd.DataFrame(finallist)

finaldf.to_csv("list.csv", index=False, header=None)
print("done")




