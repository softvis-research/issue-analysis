import pandas as pd

import Processing.PreProcessing as p


df_bug= pd.read_csv('bug.csv')
df_nolabel = pd.read_csv("not_bug.csv")


df_bug["class"] = 1
df_nolabel["class"] = 0



#
df_total = df_bug.append(df_nolabel, ignore_index=True)
df_total = df_total.append(df_bug)



#merg bodys!
df_total["full_body"] = df_total["body"] + df_total["title"]



#drop nan
df_total=df_total.dropna()

y = df_total["class"].to_numpy()



df_total["full_body"]=df_total["full_body"].apply(lambda x: p.preprocess(x))

df_total=df_total.dropna()

#uncommend to create the "trainings.csv
#df_total.to_csv("training.csv",index=False)


