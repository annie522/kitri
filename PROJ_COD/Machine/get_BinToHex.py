import sys
import pefile
'''
if len(sys.argv) is 1:
    print >> sys.stderr, '읽을 파일명을 입력해 주세요'
    exit(1)
'''
# try:
#     IN = open("c:\\windows\\system32\\notepad.exe", 'rb')  # 파일 오픈
# except IOError:
#     print >> sys.stderr, '그런 파일이 없거나, 열기 에러입니다.'
#     exit(1)
#
#
# pe = pefile.PE("c:\\windows\\system32\\notepad.exe")
# pointerToRawData = ""
# textArea = 0
# for section in pe.sections:
#     if section.Name == b'.text\x00\x00\x00':
#         pointerToRawData = "%x" % section.PointerToRawData
#         sizeOfRawData = "%x" % section.SizeOfRawData
#         textArea = int(pointerToRawData, 16) + int(sizeOfRawData, 16)
#
# offset = 0 # 번지 변수 초기화
#
# # output = ""
# while True: # 무한 루프
#     output = ""
#     buf16 = IN.read(8) # 파일을 16바이트씩 읽어 버퍼에 저장
#     buf16Len = len(buf16) # 버퍼의 실제 크기 알아내기
#     if buf16Len == 0: break
#
#     if "%08X" % (offset) > pointerToRawData.zfill(8) and "%08X  " % (offset) < "%08X" % (textArea) :
#         for i in range(buf16Len): # 헥사 부분의 헥사 값 16개 출력 (8개씩 2부분으로)
#             if (i == 8): output += " " # 8개씩 분리
#             output += "%02X" % (buf16[i]) # 헥사 값 출력
#         for i in range( ((16 - buf16Len) * 3) + 1 ): # 한 줄이 16 바이트가 되지 않을 때, 헥사 부분과 문자 부분 사이에 공백들 삽입
#             output += ""
#         if (buf16Len < 9):
#             output += "" # 한줄이 9바이트보다 적을 때는 한칸 더 삽입
#         print(output)  # 1행 분량의 헥사 덤프 문자열이 든 버퍼를 출력
#     offset += 8 # 번지 값을 16 증가
#
#
# if (offset == 0):
#     print ("%08X:  " % (offset)) # 0바이트 파일일 경우 처리
#
# IN.close # 파일 닫기

def getTextSection():
    try:
        IN = open("c:\\windows\\system32\\notepad.exe", 'rb')  # 파일 오픈
    except IOError:
        print >> sys.stderr, '그런 파일이 없거나, 열기 에러입니다.'
        exit(1)

    pe = pefile.PE("c:\\windows\\system32\\notepad.exe")
    pointerToRawData = ""
    textArea = 0
    for section in pe.sections:
        if section.Name == b'.text\x00\x00\x00':
            pointerToRawData = "%x" % section.PointerToRawData
            sizeOfRawData = "%x" % section.SizeOfRawData
            textArea = int(pointerToRawData, 16) + int(sizeOfRawData, 16)

    offset = 0  # 번지 변수 초기화

    output = ""
    while True:  # 무한 루프
        # output = ""
        buf16 = IN.read(8)  # 파일을 16바이트씩 읽어 버퍼에 저장
        buf16Len = len(buf16)  # 버퍼의 실제 크기 알아내기
        if buf16Len == 0: break

        if "%08X" % (offset) > pointerToRawData.zfill(8) and "%08X  " % (offset) < "%08X" % (textArea):
            for i in range(buf16Len):  # 헥사 부분의 헥사 값 16개 출력 (8개씩 2부분으로)
                if (i == 8): output += " "  # 8개씩 분리
                output += "%02X" % (buf16[i])  # 헥사 값 출력
            for i in range(((16 - buf16Len) * 3) + 1):  # 한 줄이 16 바이트가 되지 않을 때, 헥사 부분과 문자 부분 사이에 공백들 삽입
                output += ""
            if (buf16Len < 9):
                output += ""  # 한줄이 9바이트보다 적을 때는 한칸 더 삽입

        offset += 8  # 번지 값을 16 증가
    # print(output)  # 1행 분량의 헥사 덤프 문자열이 든 버퍼를 출력

    if (offset == 0):
        print("%08X:  " % (offset))  # 0바이트 파일일 경우 처리

    IN.close  # 파일 닫기

    return output
#
# if __name__ == '__main__':
#     getTextSection()