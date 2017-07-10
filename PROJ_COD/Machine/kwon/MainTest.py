import kitri.PROJ_COD.Machine.kwon.ngramT
import sys, glob , os
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Conn_VirusTotal')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\get_Hash')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine\\kim')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine\\kown')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine\\lee')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine\\park')
from kitri.PROJ_COD.Conn_VirusTotal import modul as TotalModul
from kitri.PROJ_COD.get_Hash import modul as HashModul
from kitri.PROJ_COD.Machine.kwon.ngramT import ngram,diff_ngram, sectionData



if __name__ == "__main__":
    ####################STEP  1 : DB 매칭 ############################
    print("****************Step one*******************")
    flist = glob.glob('C:/Users/kitri/Desktop/new/*.txt')

    for i in flist:
        if HashModul.fileScan(i) is not None:
            print("find :", i, os.path.getsize(i))


    ####################STEP  2 : VirusTotal############################
    # virustotal을 만들면서 init 함수 실행
    print("****************Step Two*******************")
    main = TotalModul.Virustotal()
    # print (main.md5())
    var = main.md5()
    dic = main.rscReport(var)

    if dic['positives'] >= 10:
        print("VIRUS!!!")
        sys.exit(1)
    else:
        print("NOMAL FILE")
    print("total = ", dic['total'], "positives = ", dic['positives'])
    ####################STEP  3 : machineRunning############################
    print("****************Step Three*******************")
    DATA = sectionData()

    a = "033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34"
    b = "033C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A3433CBA34"
    c = "0020C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033CA34033C0A3433CBA34"
    # 4-gram
    r4, word4 = diff_ngram(a, DATA, 4)

    #print("4-gram:", r4, word4)
