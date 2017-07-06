import sys
import pefile
'''
if len(sys.argv) is 1:
    print >> sys.stderr, '읽을 파일명을 입력해 주세요'
    exit(1)
'''
try:
   # IN = open(sys.argv[1], 'rb') # 파일 오픈
    IN = open("c:\\windows\\system32\\notepad.exe", 'rb')  # 파일 오픈
except IOError:
    print >> sys.stderr, '그런 파일이 없거나, 열기 에러입니다.'
    exit(1)

#pe = pefile.PE(sys.argv[1])
pe = pefile.PE("c:\\windows\\system32\\notepad.exe")
pointerToRawData = ""
textArea = 0
for section in pe.sections:
    if section.Name == b'.text\x00\x00\x00':
        print(section)
        print("%x" % section.PointerToRawData)
        pointerToRawData = "%x" % section.PointerToRawData
        sizeOfRawData = "%x" % section.SizeOfRawData
        print(sizeOfRawData)
        textArea = int(pointerToRawData, 16) + int(sizeOfRawData, 16)
    print("%x" % textArea)
print("***********************************************\n")
offset = 0 # 번지 변수 초기화
output = ""
while True: # 무한 루프
    print("***********************************************\n")
    buf16 = IN.read(8) # 파일을 16바이트씩 읽어 버퍼에 저장
    buf16Len = len(buf16) # 버퍼의 실제 크기 알아내기
    if buf16Len == 0: break
    # print("%08X  " % (offset))
    # print("pointerToRawData : {}".format(pointerToRawData.zfill(8)))

    if "%08X  " % (offset) > pointerToRawData.zfill(8) and "%08X  " % (offset) < "%08X" % (textArea) :
        #  output = "%08X  " % (offset) # Offset(번지)을, 출력 버퍼에 쓰기    -> 주소값!!!!!!!!!!!!!!
        for i in range(buf16Len): # 헥사 부분의 헥사 값 16개 출력 (8개씩 2부분으로)
            if (i == 4): output += "\n" # 8개씩 분리
            # print(buf16Len)
            # print(buf16[i])
            # output += "%02X " % (ord(buf16[i])) # 헥사 값 출력
            output += "%02X 간다 " % (buf16[i]) # 헥사 값 출력

        for i in range( ((8 - buf16Len) * 3) + 1 ): # 한 줄이 16 바이트가 되지 않을 때, 헥사 부분과 문자 부분 사이에 공백들 삽입
            output += "|"
        if (buf16Len < 9):
            output += " " # 한줄이 9바이트보다 적을 때는 한칸 더 삽입
        print("********************************\n")
        print(buf16Len)
        print("\n***************************************")

        print("sddskfjsldkfjsldkfjs대체머냐fsdf"+output)  # 1행 분량의 헥사 덤프 문자열이 든 버퍼를 출력

    offset += 8  # 번지 값을 16 증가

'''
        for i in range(buf16Len): # 문자 구역 출력
            if (buf16[i] >= 0x20 and buf16[i] <= 0x7E): # 특수 문자 아니면 그대로 출력
                output += "%c" % int(buf16[i])
            else: output += "." # 특수문자, 그래픽문자 등은 마침표로 출력
'''




if (offset == 0):

    print ("주소값 : %08X:  " % (offset)) # 0바이트 파일일 경우 처리

IN.close # 파일 닫기