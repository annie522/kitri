import hashlib, glob, pymongo

"""
작성자   : 김예지
작성일   : 2017-07-14
버전     : v1.0(수정시 버전 올려주세요)
프로그램 : 파일 해시값을 중복되지 않게 몽고디비에 저장하는 코드
"""

# connection = pymongo.MongoClient("mongodb://14.63.24.247:27017")
connection = pymongo.MongoClient("mongodb://192.168.0.13:27017")
db = connection.testdb
users = db.users

def getFileHash(filename):
    print("1111111111111111111111")
    insertFormat = {}
    print("22222222222222222222222")
    myMd5 = hashlib.md5()
    print("33333333333333333333333")
    a = 0
    print("444444444444444444444")
    with open(filename, 'rb') as checkFile:
        print("555555555555555555555")
        for chunk in iter(lambda: checkFile.read(8192), ''):
            print("666666666666666666666")
            myMd5.update(chunk)
            print("7777777777777777777")
            fileHash = myMd5.hexdigest()
            print("1111111111111111111111")
            insertFormat = {'hash':fileHash}
            print("1111111111111111111111")
            item = users.find()
            print("1111111111111111111111")
            for i in item:
                if(i['hash'] == fileHash):
                    print("[+] find match data : ",i['hash'], fileHash)
                    a = 1
                    break
                else:
                    print("[+] not match : ",i['hash'], fileHash)
            if a == 0:
                try:
                    users.insert(insertFormat)
                    print("[ ] insert success")
                except:
                    print("[ ] insert failed")
            checkFile.close()
            break
        checkFile.close()

if __name__ == "__main__":
    flist = glob.glob('C:/Tmp/*.exe')
    print(flist)
    for i in flist:
        print("[+] fileName = ",i)
        getFileHash(i)