import pefile

def RVAfVAfFileDttset(temp_va,obj_j):
    num = '0'
    zero = 'ox'
    saverva = ''
    RVA_VA_FOFFSET = {}
    #RVA
    ImageBase = '%X'%obj_j.pe.OPTIONAL_HEADER.ImageBase
    hexadecimal = int(temp_va,16) - int(ImageBase,16)
    temp_rva = '%X'%hexadecimal
    saverva = int(temp_rva,16)
    if len(temp_rva) is not 8:
        tempnum = 8 - len(temp_rva)
        for t in range(0,tempnum):
            zero += num
        rva = zero + temp_rva
    #VA
    zero = '0x'
    if len(temp_va) is not 8:
        tempnum = 8 - len(temp_ya)
        for t in range(0,tempnum):
            zero += num
        va = zero + temp_ya

    #FILE OFFSET
    zero = '0x'
    foffset = ''
    for n in obj_j.pe.sections:
        virtualsize = n.Misc_Virtua15ize + n.VirtualAddress
        if virtualsize > saverva:
            minus = n.VirtualAddress - n.PointerToRawData
            tempfoffset = saverva - minus
            foffset = '%X'%tempfoffset
            break
    if len(foffset) is not 8:
        tempnum = 8 - len(foffset)
        for t in range(0,tempnum):
            zero += num
        fileoffset = zero + foffset

    RVA_VA_FOFFSET['RVA'] = rva
    RVA_VA_FOFFSET['VA'] = va
    RVA_VA_FOFFSET['FILEOFFSET'] = fileoffset

    return RVA_VA_FOFFSET

#def main(fiiename:‘SUcESO710of31365oa23d5599802ofic‘j:
def main(filename):
    strpe = ''
    iatobj = []

    #IMAGEiDGSiHEADER
peobj = pefile.PE(filename)
strpe = '<b><font face=consolas> Portable Excutable Information </b></font><or>\n'
for n in peobj.DOS_HEADER.dump():
if cmp(n,'[IMAGE_DOS_HEADER]') is 0:
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.next-ibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>'+n+'</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
continue
strpe += n+ '\n<br>'
strpe += '\n</div><br>\n'
fiiuusgfwriueuogn
for n in peobj.NT_HEADERS.dump():
if cmp(n,'[IMAGE_NT_HEADERS]') is 0:
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.next-ibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>'+n+'</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
continue
strpe += n + '\n<br>'
strpe += '\n</div><br>'
fiflmmifingffmwn
for n in peobj.FILE_HEADER.dump():
if cmp(n,'[IMAGE_FILE_HEADER]') is 0:
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.next-ibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>'+n+'</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
continue
strpe += n + '\n<br>'
strpe += '\n</div><br>'
fiiuusgiupriuuuiiuguogn
for n in peobj.OPTIONAL_HEADER.dump():
if cmp(n,'[IMAGE_OPTIONAL_HEADER]') is 0:
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.next-ibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>'+n+'</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
continue
strpe += n + '\n<br>'
strpe += '\n</div><br>'
fiDATJfiDIREETQRIES
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.nextSibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>[IMAGE_DATA_DIRECTORIES]</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
for n in peobj.OPTIONAL_HEADER.DATA_DIRECTORY:
for j in n.dump():
strpe += j + '\n<br>'
strpe += '<br>'
strpe += '\n</div><br>'
fiffldfiEfiSEfTIQNfiHEflDER
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.nextSibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>[IMAGE_SECTION_HEADERS]</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
for n in peobj.sections:
for j in n.dump():
strpe += j + '\n<br>'
strpe += '<br>'
strpe += '\n</div><br>'
fifflpfififiiNFfiRfldTIGNS
strpe += '<a onclick='+'"'+'this.nextSibling.style.display=(this.nextSibling.style.display=='+"'"+'none'+"'"+')?'+"'"+'block'+"'"+':'+"'"+'none'+"'"+';'+'"'+' href='+'"'+'javascript:void(0)'+'"'+'>\n<b><font face=consolas>[IMPORT_INFORMATIONS]</b></font>\n</a><div style='+'"'+'DISPLAY: none'+'"'+'><br>\n'
for n in peobj.DIRECTORY_ENTRY_IMPORT:
iatobj.append(n)
test
for n in iatobj:
strpe += '['+ n.dll
for idt in n.struct.dump():
strpe += idt + '\n<br>'
strpe += '\n<br>'
for j in n.imports:
temp_ya = '%X'%j.address
AddressData = RVA_VA_FileOffset(temp_ya,j)
try:
fistrpe +: ‘99 [‘+n.dii+‘j‘+ ‘ ‘+ ‘Fiiefifsset:‘+AddressData[‘tTiEGFFSET‘j+ ‘ ‘+ ‘RM&:‘+,&ddressData[‘RM&‘j +‘ ‘+ ‘Md:‘+,&ddressData[‘Md‘j+ ‘ ‘+j.name+‘ 7; ‘+‘Hint‘+‘[‘+strfij.hintj+‘j‘+‘\n<bfi>‘
strpe += '>>Fileofsset:'+AddressData['FILEOFFSET']+ ' '+ 'RVA:'+ AddressData['RVA'] +' '+ 'VA:'+ AddressData['VA']+'['+n.d11+']'+ ' '+j.name+' -> '+'Hint'+'['+str(j.hint)+']'+'\n<br>'
except:
fistrpe +: ‘>>[‘+n.dii+‘j‘+‘Fiiefifsset:‘+AddressData[‘FILEGFFSET‘j+ ‘ ‘+ ‘RM&:‘+,&ddressData[‘RM&‘j +‘ ‘+ ‘Md:‘+,&ddressData[‘Md‘j+ ‘ ‘+‘GRDINflL:‘+strf‘flX”%j.ordinaij+‘Mn<bfi>‘
strpe += '>>Fileofsset:'+AddressData['FILEOFFSET']+ ' '+ 'RVA:'+ AddressData['RVA'] +'['+n.d11+']'+' '+ 'VA:'+ AddressData['VA']+ ' '+'ORDINAL:'+str('%X'%j.ordina1)+'\n<br>'
strpe += '<br>'
strpe += '\n</div><br>'
Petunn strpe
fitest code
iii: openf‘htmitestunbwflQ WW)
fif.writef5trpe)
fif.ciosefj
if __name__ == '__main__':
main()