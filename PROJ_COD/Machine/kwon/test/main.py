import kitri.PROJ_COD.Machine.kwon.test.Con_Virustotal as filehash
import kitri.PROJ_COD.Machine.kwon.test.Get_File_Hash as filehas
import kitri.PROJ_COD.Machine.kwon.test.Con_Virustotal as filehash
# from PROJ_COD.Machine.kwon.test import Get_File_Hash as filehash
# from PROJ_COD.Machine.kwon.test import Con_Virustotal as conVirustotal
from kitri.PROJ_COD.Machine.kwon.test import Get_Mal_Info as malInfo
from kitri.PROJ_COD.Machine.kwon.test import Get_Opcode_Info as opInfo
import kitri.PROJ_COD.MongoDB_Connection as mongoDB
import glob
if __name__ == '__main__':
    # 악성코드 탐지할 경로 가져오기
    # pyqt에서 선택한 내용으로 집어 넣기
    # Version1: selFile -> 파일 하나 선택한 경우
    # Version2: allFiles -> 폴더 경로 선택한 경우

    # Version1 : selFile

    ########################################################################################
    # Version2 : allFiles(폴더 선택한 경우)
    allFiles = glob.glob('C:\\TMP4\\*.exe')
    # 가져온 리스트만큼 반복작업 진행
    for fileName in allFiles:
        print("file_name : ", fileName)
        hashRslt = filehash.Get_File_Hash_Main(fileName)[0]
        hashFile = filehash.Get_File_Hash_Main(fileName)[1]
        if hashRslt[0] == "NO":
            # print("[+] RESULT IS NO")
            # vtotalRslt = conVirustotal.get_mal_kind(fileName)
            # print("vtotalRslt : ",vtotalRslt)
            # print("vtotalRslt[0] : ",vtotalRslt[0])
            # if vtotalRslt[0] > 10:
            #     print("[+] THIS FILE MIGHT BE A MALWARE. WE HAVE TO CHECK MORE USING OUR MACHINE. PLEASE WAIT. TILL IT'S OVER.")
            #     # 테스트할 때 필요한 코드(악성 학습데이터 저장하기)
            #     malInfo.get_info(fileName).update({"kind":"MALWARE","hash":hashFile})
            #     print("[+] MAL_INFORMATION : ", malInfo.get_info(fileName))
            #     insert_data = malInfo.get_info(fileName)
            #     try: del insert_data['_id']
            #     except: pass
            #     learn_data = mongoDB.DBConn("shutdown").learn_data
            #     learn_data.insert(insert_data)
            #     print("[+] WE FINISHED INSERT MALWARE DATA IN SHUTDOWN.LEARN_DATA SUCCESSFULLY.")
            # elif vtotalRslt[0] <= 10:
            #     try:
            #         print("[+] THIS FILE IS NOT A MALWARE. PROCESS IS FINISHED.")
            #         # 테스트할 때 필요한 코드(정상 학습데이터 저장하기)
            #         malInfo.get_info(fileName).update({"kind": "NORMAL", "hash": hashFile})
            #         print("[+] MAL_INFORMATION : ", malInfo.get_info(fileName))
            #         insert_data = malInfo.get_info(fileName)
            #         try: del insert_data['_id']
            #         except: pass
            #         learn_data = mongoDB.DBConn("shutdown").learn_data
            #         learn_data.insert(insert_data)
            #         print("[+] WE FINISHED INSERT NORMAL DATA IN SHUTDOWN.LEARN_DATA SUCCESSFULLY.")
            #     except:
            #         print("[+] THE ERROR IN MAIN 51")
            print("[+] RESULT IS NO")
            vtotalRslt = conVirustotal.get_mal_kind(fileName)
            print("vtotalRslt : ", vtotalRslt)
            print("vtotalRslt[0] : ", vtotalRslt[0])
            if vtotalRslt[0] > 10:
                print(
                    "[+] THIS FILE MIGHT BE A MALWARE. WE HAVE TO CHECK MORE USING OUR MACHINE. PLEASE WAIT. TILL IT'S OVER.")
                # 테스트할 때 필요한 코드(악성 학습데이터 저장하기)
                opInfo.get_info(fileName).update({"kind": "MALWARE", "hash": hashFile})
                print("[+] MAL_INFORMATION : ", opInfo.get_info(fileName))
                insert_data = opInfo.get_info(fileName)
                try:
                    del insert_data['_id']
                except:
                    pass
                opcode_data = mongoDB.DBConn("shutdown").opcode_data
                opcode_data.insert(insert_data)
                print("[+] WE FINISHED INSERT MALWARE DATA IN SHUTDOWN.LEARN_DATA SUCCESSFULLY.")
            elif vtotalRslt[0] <= 10:
                try:
                    print("[+] THIS FILE IS NOT A MALWARE. PROCESS IS FINISHED.")
                    # 테스트할 때 필요한 코드(정상 학습데이터 저장하기)
                    opInfo.get_info(fileName).update({"kind": "NORMAL", "hash": hashFile})
                    print("[+] MAL_INFORMATION : ", opInfo.get_info(fileName))
                    insert_data = opInfo.get_info(fileName)
                    try:
                        del insert_data['_id']
                    except:
                        pass
                    opcode_data = mongoDB.DBConn("shutdown").opcode_data
                    opcode_data.insert(insert_data)
                    print("[+] WE FINISHED INSERT NORMAL DATA IN SHUTDOWN.LEARN_DATA SUCCESSFULLY.")
                except:
                    print("[+] THE ERROR IN MAIN 51")
        elif hashRslt[0] == "YES":
            if hashRslt[1] == "M":
                print("[+] THIS FILE IS A MALWARE. WE FIND OUT MATCHED HASH VALUE IN OUR MALWARE_DATABAE")
                print("[+] YOU HAVE TO REMOVE THIS FILE")
            elif hashRslt[1] == "N":
                print("[+] THIS FILE IS NOT A MALWARE. PROCESS IS FINISHED.")
        else:
            print("[+] GET_FILE_HASH_MAIN ERROR")

        # break
        # rslt = vs.get_mal_kind(i)
        # print(rslt)
        # learnDB = mg.DBConn("shutdown").learnDB
        # if rslt[0] > 0:
        #     if fh.get_hash_match(i) == False:
        #         insert_test_doc = get_info()
        #         try:
        #             del insert_test_doc['_id']
        #         except:
        #             pass
        #         insert_test_doc.update({"detect": rslt[1], "hash": rslt[2]})
        #         print("insert_teset_doc : ", insert_test_doc)
        #         try:
        #             users.insert(insert_test_doc)
        #             print("[+] insert success", sys.exc_info()[0])
        #         except:
        #             print("[-] insert failed", sys.exc_info()[0])
        #     else:
        #         print("[-] We find matched Hash. You don't need to insert again!")