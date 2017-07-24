import hashlib
import PROJ_COD.FINAL.Get_MongoDB_Connection as mongoDB

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
    checkCount = 0
    try:
        opcode_data = mongoDB.DBConn("shutdown").opcode_data
        selectDB = opcode_data.find({},{'_id':0,'hash':1, 'kind':1})
        for i in selectDB:
            i = str(i).split(",")
            kind = i[0].replace("{'kind': '","").replace("'","")
            hash = i[1].replace(" 'hash': '","").replace("'}","")
            if hash == md5Hash:
                if kind == "MALWARE":
                    checkCount = 1
                    return "YES", "M"
                elif kind == "NORMAL":
                    checkCount = 0
                    return "YES", "N"
        if checkCount == 0:
            return "NO", "?"
        else:
            return "YES"
    except:
        pass