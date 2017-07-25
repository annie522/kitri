import pymongo

"""
작성일   : 2017-07-18(최초작성)
수정일   : 
버전     : v1.0(수정시 버전 올려주세요)
프로그램 : 몽고디비 공통으로 관리, db추가시 코드 수정 필요
"""

def DBConn(dbName):
    connection = pymongo.MongoClient("mongodb://203.234.103.169:27017")
    if dbName == "testdb":
        db = connection.testdb
    elif dbName == "maldb":
        db = connection.maldb
    elif dbName == "shutdown":
        db = connection.shutdown
    else:
        print("db이름을 확인하세요")
    return db
