import numpy as np
import pandas as pd
import spacy
from sklearn.linear_model import LogisticRegression

class MyModel:
    def __init__(self):
        # xử lý ngôn ngữ tự nhiên
        self.nlp = spacy.load("vi_core_news_lg")#en_core_web_sm, vi_core_news_lg xx_sent_ud_sm
        # model
        self.model = LogisticRegression()
        
    def read_file_excel(self, pathfile):
        df = pd.read_excel(pathfile)#train.csv or F.R.I.D.A.Y/train.csv
        print(df)
        x_data = []
        y_data = []
        for i in range(len(df.keys().tolist())):#
            for j in df[df.keys()[i]]:
                if(str(j) in "nan NaN"):
                    break
                x_data.append(self.nlp(j).vector)
                y_data.append(i)
        x_data = np.array(x_data)
        y_data = np.array(y_data)
        return x_data, y_data

    def fit(self, x_data, y_data):
        self.model.fit(x_data, y_data)
    
    def predict(self, s):
        # chuyen string ve vector
        s = np.array(self.model.predict_proba([self.nlp(s).vector]))
        # bắt đầu dự đoán
        s = s[0]
        label = np.argsort(s)[::-1]
        p = s[label[0]]
        label = label[0]
        # label có xác suất cao nhất
        return label,p

    def predicts(self, x_predicts):
        self.model.predict(x_predicts)

    def score(self, x_test, y_test):
        return self.model.score(x_test, y_test)
    
if __name__ == "__main__":
    # tạo model
    model = MyModel()
    # đọc dữ liệu từ file để train
    x_data,y_data = model.read_file_excel(f"train.xlsx")

    # train
    model.fit(x_data,y_data)
   
    # test
    x_test,y_test = model.read_file_excel(f"test.xlsx")
    print("độ chính xác: " + str(model.score(x_test,y_test)))

    # kết quả dự đoán trong file test
    # print(model.predicts(x_test))
    # print(y_test)

    # dự đoán 1 câu
