import glob

import PROJ_COD.FINAL.Get_File_Info as getFileInfo
import PROJ_COD.FINAL.Get_VirusTotal as getVirustotal
import PROJ_COD.FINAL.Get_File_Hash as getFileHash
import PROJ_COD.FINAL.Get_MongoDB_Connection as mongoDB

learnFiles = glob.glob("C:\\TEMP10\\*.exe")

for filePath in learnFiles:
    print(filePath)
    fileInfo = getFileInfo.getFileInfo(filePath)
    virustotal = getVirustotal.get_mal_kind(filePath)

    print(type(fileInfo))
    print(type(virustotal))
    print(virustotal[0])
    print(virustotal[1])
    print(fileInfo)
    if virustotal[0]==0:
        fileInfo.update({"kind":"NORMAL","detect":"NORMAL"})
    elif virustotal[0]!=0:
        fileInfo.update({"kind": "MALWARE", "detect": virustotal[1]})
    print(fileInfo)
    print(fileInfo['hash'])

    checkData = getFileHash.checkHashInDB(fileInfo['hash'])
    if checkData[0] == "NO":
        opcode_data = mongoDB.DBConn("shutdown").opcode_data
        opcode_data.insert(fileInfo)
        print("[+] Insert SUCCESS!!!!!")
    else:
        print("[+] Insert FAILE!!!!!!!")