import glob

import PROJ_COD.FINAL.Get_File_Info as getFileInfo
import PROJ_COD.FINAL.Get_VirusTotal as getVirustotal
import PROJ_COD.FINAL.Get_File_Hash as getFileHash
import PROJ_COD.FINAL.Get_MongoDB_Connection as mongoDB

learnFiles = glob.glob("G:\\exe파일\\새 폴더\\*.exe")

def insertDataToDatabase():
    checkData = getFileHash.checkHashInDB(fileInfo['hash'])
    if checkData[0] == "NO":
        opcode_data = mongoDB.DBConn("shutdown").opcode_data
        opcode_data.insert(fileInfo)
        print("[+] Insert SUCCESS!!!!!")
    else:
        print("[+] Insert FAILE!!!!!!!")

for filePath in learnFiles:
    print(filePath)
    fileInfo = getFileInfo.getFileInfo(filePath)
    if fileInfo != "NOPEFILE":
        virustotal = getVirustotal.get_mal_kind(filePath)

        if virustotal[1] == "NORMAL":
            fileInfo.update({"kind": "NORMAL", "detect": "NORMAL"})
            insertDataToDatabase()
        elif virustotal[1] == "ERROR":
            print("ERROR!!!!@!@!@!@!@!@!@!@!!@")
            pass
        else:
            fileInfo.update({"kind": "MALWARE", "detect": virustotal[1]})
            insertDataToDatabase()
    else:
        print("[+] THIS IS NOT PEFILE. WE CAN'T DETECT THIS FILE !!!!!!!!!!!!!!!!!")

