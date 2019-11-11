import pandas as pd
import numpy as np

df = pd.read_csv("mail.csv")
l = df.values.tolist()
# print(l)
a=np.array(l)
print(a.shape)
for i in range(100):
    print(a[i][0])
# for i in l:
    # print(i[0])