import re

a = ["b'.text\x00\x00\x00'","b'.rdata\x00\x00\x00'"]
a = str(a)
#a = "b'.text\x00\x00\x00'"
#print (a)
#print(a[0])
print (re.split(r"[\b'|\x00]","b'.text\x00\x00\x00'")[1])
b = (re.sub(r"[b'|'\\x00']","",a))
print ('b = ',b)
print(type(b))