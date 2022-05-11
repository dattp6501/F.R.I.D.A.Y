import pandas as pd
import spacy
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# dọc file
df = pd.read_excel(f"F.R.I.D.A.Y/train.xlsx")#train.csv or F.R.I.D.A.Y/train.csv
nlp = spacy.load("vi_core_news_lg")#en_core_web_sm, vi_core_news_lg xx_sent_ud_sm
data = []
label = []
for i in range(len(df.keys().tolist())):#
    for j in df[df.keys()[i]]:
        if(str(j) in "nan NaN"):
            break
        data.append(nlp(j).vector)
        label.append(i)
# for i in data:
#     print(i,sep="\n")
label = np.array(label)
data = np.array(data)
# for i in label:
#     print(i,end=", ")
# train

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data,label)