import random
import PROJ_COD.MongoDB_Connection as mongoDB
from sklearn import svm, metrics
import PROJ_COD.GUI_Test.Get_File_Info2 as getFileInfo

def getFIleMachine(filePath):
    opcode_data = mongoDB.DBConn("shutdown").opcode_data
    learn_data1 = opcode_data.find({},{"_id":0,"hash":0,"detect":0})
    learn_data2 = []
    for item in learn_data1:
        print(str(item.keys()))
        learn_data2.append(list(item.values()))

    # 데이터 셔플하기(섞기)
    random.shuffle(learn_data2)

    # 학습 전용 데이터와 테스트 전용 데이터 분할하기(2:1 비율)
    total_len = len(learn_data2)
    print("total_len : ", total_len)
    train_len = len(learn_data2)
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    for i in range(total_len):
        data = learn_data2[i][1:10]
        data2 = getFileInfo.getFileInfo("C:\\Users\\Administrator\\Downloads\\CorsixTHInstaller.exe")
        del data2['kind']
        del data2['hash']
        del data2['detect']
        data2 = list(data2.values())
        label = learn_data2[i][0]
        if i < train_len:
            train_data.append(data)
            train_label.append(label)
    test_data.append(data2)
    test_label.append(label)

    # 데이터를 학습시키고 예측하기
    clf = svm.SVC()
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)
    print("pre  :::::::::::::: ", pre[0])
    return pre[0]