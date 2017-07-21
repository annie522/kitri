import hashlib, glob
import PROJ_COD.MongoDB_Connection as mongoDB

"""
작성일   : 2017-07-14(최초작성)
수정일   : 2017-07-18(디비연결 공통으로 변경)
버전     : v1.1(수정시 버전 올려주세요)
프로그램 : 파일 해시값을 중복되지 않게 몽고디비에 저장하는 코드
"""




def getFileHash(filename):
    with open(filename, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def checkHashInDB(md5Hash):
    md5Hash = md5Hash
    checkCount = 0
    try:
        learn_data = mongoDB.DBConn("shutdown").learn_data
        md5InDB = learn_data.find({},{'hash':1})
        print(md5InDB)
        for i in md5InDB:
            print(i)
            if i == md5Hash:
                checkCount = 1
                break
        if checkCount == 0:
            return "NO"
        else:
            return "YES"
    except:
        print("[+] Error HERE")

def Get_File_Hash_Main(filename):
    return checkHashInDB(getFileHash(filename))
# if __name__ == "__main__":
#     flist = glob.glob('C:\\TMP2\\*.exe')
#     print(flist)
#     for i in flist:
#         print(checkHashInDB(getFileHash(i)))
