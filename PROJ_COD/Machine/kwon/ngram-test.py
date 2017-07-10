import sys
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD\\Machine')
sys.path.append('C:\\Users\\zzabz\\PycharmProjects\\Shutdown\\kitri\\PROJ_COD')

from .get_BinToHex22222 import sectionData

def ngram(s, num):
    res = []
    slen = len(s) - num + 1
    for i in range(slen):
        ss = s[i:i+num]
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1
                r.append(i)
    return cnt / len(a), r
# a = getTextSection()
# print("a",a)
a = "033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34"
b = "033C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A3433CBA34"
c = "0020C0A34033C0A21302456334033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033C0A34033CA34033C0A3433CBA34"
# 1-gram
r1, word1 = diff_ngram(a, b, 1)
print("1-gram:", r1, word1)
# 2-gram
r2, word2 = diff_ngram(a, b, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(a, b, 3)
print("3-gram:", r3, word3)
# 4-gram
r4, word4  = diff_ngram(a, b, 4)
print("4-gram:", r4, word4)