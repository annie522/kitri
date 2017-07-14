import sys
from collections import OrderedDict

sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine\\kwon')


from kitri.PROJ_COD.Machine.kwon.get_BinToHex22222 import sectionData

def ngram(s, num, num1):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(s[i:i+num])
  #  print("res : ",res)
  #  if num1 ==1: print("res : ",res)
    print("ngarm 되는중")
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num,0)
    b = ngram(sb, num,1)
    r = []
    cnt = 0
    print(len(a))
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    print(cnt)
    print("탈출!!!")
    return cnt / len(a), r

def ngram_analyze(n,content):
    ngram_dictionary= OrderedDict()
    for i in range(0, len(content)-n):
        nword =""
        for j in range(0,n):
            if content[i+j] != '\n':
                nword += content[i+j]
        if nword in ngram_dictionary:
            ngram_dictionary[nword] +=1
        else:
            ngram_dictionary[nword] =1
    return ngram_dictionary


'''

# a = getTextSection()
# print("a",a)
DATA=sectionData()

a = "033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34"
b = "033C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A3433CBA34"
c = "0020C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033CA34033C0A3433CBA34"
# 4-gram
r4, word4  = diff_ngram(a, DATA, 4)

print("4-gram:", r4, word4)
'''