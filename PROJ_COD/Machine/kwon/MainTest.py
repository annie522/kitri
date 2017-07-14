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

    ####################STEP  3 : machineRunning############################
    print("****************Step Three*******************")
    DATA = sectionData()
    print(DATA)
    print(len(DATA))
    a = "033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34"
    b = "033C0"
    c = "오늘 강남에서 스파게티를 먹엇다."
      # 4-gram
    print(a)
   # r4, word4 = diff_ngram(DATA, DATA, 1)
    ngram_an
    print("4-gram:", r4, word4)
