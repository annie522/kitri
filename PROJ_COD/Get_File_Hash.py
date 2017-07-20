import hashlib, glob
import PROJ_COD.MongoDB_Connection as mongoDB

"""
작성일   : 2017-07-14(최초작성)
수정일   : 2017-07-18(디비연결 공통으로 변경)
버전     : v1.1(수정시 버전 올려주세요)
프로그램 : 파일 해시값을 중복되지 않게 몽고디비에 저장하는 코드
"""

users = mongoDB.DBConn("maldb").users


def getFileHash(filename):
    insertFormat = {}
    myMd5 = hashlib.md5()
    a = 0
    with open(filename, 'rb') as checkFile:
        for chunk in iter(lambda: checkFile.read(8192), ''):
            myMd5.update(chunk)
            fileHash = myMd5.hexdigest()
            insertFormat = {'hash': fileHash}
            item = users.find()
            for i in item:
                if (i['hash'] == fileHash):
                    print("[+] find match data : ", i['hash'], fileHash)
                    a = 1
                    break
                else:
                    print("[+] not match : ", i['hash'], fileHash)
            if a == 0:
                try:
                    users.insert(insertFormat)
                    print("[ ] insert success")
                except:
                    print("[ ] insert failed")
            checkFile.close()
            break
        checkFile.close()

def get_hash_match(filename):
    insertFormat = {}
    myMd5 = hashlib.md5()
    a = 0
    with open(filename, 'rb') as checkFile:
        print("111111111111111111111111111111111111111111111111111 fileName : ", filename)
        for chunk in iter(lambda: checkFile.read(8192), ''):
            myMd5.update(chunk)
            fileHash = myMd5.hexdigest()
            print("111111111111111111111111111111111111111111111111111 fileHash : ", fileHash)
            insertFormat = {'hash': fileHash}
            item = users.find()
            print("item : ", item)
            for i in item:
                try:
                    if (i['hash'] == fileHash):
                        print("[+] find match data : ", i['hash'], fileHash)
                        a = 1
                        break
                    else:
                        print("[+] not match : ", i['hash'], fileHash)
                except:
                    pass
            checkFile.close()
            break
        checkFile.close()
    if a == 0:
        try:
            return False
        except:
            return True

if __name__ == "__main__":
    flist = glob.glob('C:/Tmp2/*.exe')
    print(flist)
    for i in flist:
        print("[+] fileName = ", i)
        getFileHash(i)
