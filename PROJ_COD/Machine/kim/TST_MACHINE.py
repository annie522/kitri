from sklearn import svm, metrics
import PROJ_COD.MongoDB_Connection as  mongoDB
import random, re

# 붗꽃의 CSV 데이터 읽어 들이기
csv = []
result = []
opcode_data = mongoDB.DBConn("shutdown").opcode_data
all_data = opcode_data.find({},{"_id":0,"$exists":})

for line in all_data:
    print("line : ", line.values())
    print(test)
with open("iris.csv","r",encoding="utf-8") as fp:
    # 한 줄씩 읽어 들이기
    for line in fp:
        # print (line)
        line = line.strip()     # 줄바꿈 제거
        # print(line)
        cols = line.split(",")  # 쉼표로 자르기
        # print(cols)
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n :float(n) if re.match(r'^[0-9\.]+$', n) else n
        print(fn("10"))
        cols = list(map(fn, cols))
        print (cols)
        csv.append(cols)
    print("[+] CSV : ",csv)



# 가장 앞 줄의 헤더 제거
del csv[0]
print("[+] CSV : ",csv)
#
# # 데이터 셔플하기(섞기)
# random.shuffle(csv)
#
# # 학습 전용 데이터와 테스트 전용 데이터 분할하기(2:1 비율)
# total_len = len(csv)
# train_len = int(total_len * 2 / 3)
# train_data = []
# train_label = []
# test_data = []
# test_label = []
# for i in range(total_len):
#     data = csv[i][0:4]
#     label = csv[i][4]
#     if i < train_len:
#         train_data.append(data)
#         train_label.append(label)
#     else:
#         test_data.append(data)
#         test_label.append(label)
#
# # 데이터를 학습시키고 예측하기
# clf = svm.SVC()
# clf.fit(train_data, train_label)
# pre = clf.predict(test_data)
#
# # 정답률 구하기
# ac_score = metrics.accuracy_score(test_label, pre)
# print("정답률 : ", ac_score)
