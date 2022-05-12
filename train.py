import numpy as np
import pandas as pd
import spacy
from sklearn.linear_model import LogisticRegression
# doc du lieu tu file train.xlsx
df = pd.read_excel(f"train.xlsx")#train.csv or F.R.I.D.A.Y/train.csv
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

# train
model = LogisticRegression()
model.fit(data,label)


# test
dftest = pd.read_excel(f"test.xlsx")#train.csv or F.R.I.D.A.Y/train.csv
datatest = []
labeltest = []
for i in range(len(dftest.keys().tolist())):#
    for j in dftest[dftest.keys()[i]]:
        if(str(j) in "nan NaN"):
            break
        datatest.append(nlp(j).vector)
        labeltest.append(i)
labeltest = np.array(labeltest)
datatest = np.array(datatest)
print("do chinh xac: "+str(model.score(datatest,labeltest)))
y_test_p = model.predict(datatest)
print(labeltest)
print(y_test_p)