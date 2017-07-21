import pefile
import distorm3
import sys
import pymongo
import glob
import re
import PROJ_COD.Con_Virustotal as vs
import PROJ_COD.MongoDB_Connection as mg
import PROJ_COD.Get_File_Hash as fh

"""
작성일   : 2017-07-14(최초작성)
수정일   : 2017-07-15(특정 디렉토리 모든 파일 검색)
           2017-07-18(몽고디비 연동)
버전     : v1.2(수정시 버전 올려주세요)
프로그램 : 악성코드의 opcode, ie_api, section_name 을 몽고디비에 저장하는 코드
"""

section_characteristics = [
    ('IMAGE_SCN_TYPE_REG', 0x00000000),  # reserved
    ('IMAGE_SCN_TYPE_DSECT', 0x00000001),  # reserved
    ('IMAGE_SCN_TYPE_NOLOAD', 0x00000002),  # reserved
    ('IMAGE_SCN_TYPE_GROUP', 0x00000004),  # reserved
    ('IMAGE_SCN_TYPE_NO_PAD', 0x00000008),  # reserved
    ('IMAGE_SCN_TYPE_COPY', 0x00000010),  # reserved
    ('IMAGE_SCN_CNT_CODE', 0x00000020),
    ('IMAGE_SCN_CNT_INITIALIZED_DATA', 0x00000040),
    ('IMAGE_SCN_CNT_UNINITIALIZED_DATA', 0x00000080),
    ('IMAGE_SCN_LNK_OTHER', 0x00000100),
    ('IMAGE_SCN_LNK_INFO', 0x00000200),
    ('IMAGE_SCN_LNK_OVER', 0x00000400),  # reserved
    ('IMAGE_SCN_LNK_REMOVE', 0x00000800),
    ('IMAGE_SCN_LNK_COMDAT', 0x00001000),
    ('IMAGE_SCN_MEM_PROTECTED', 0x00004000),
    ('IMAGE_SCN_NO_DEFER_SPEC_EXC', 0x00004000),
    ('IMAGE_SCN_GPREL', 0x00008000),
    ('IMAGE_SCN_MEM_FARDATA', 0x00008000),
    ('IMAGE_SCN_MEM_SYSHEAP', 0x00010000),
    ('IMAGE_SCN_MEM_PURGEABLE', 0x00020000),
    ('IMAGE_SCN_MEM_16BIT', 0x00020000),
    ('IMAGE_SCN_MEM_LOCKED', 0x00040000),
    ('IMAGE_SCN_MEM_PRELOAD', 0x00080000),
    ('IMAGE_SCN_ALIGN_1BYTES', 0x00100000),
    ('IMAGE_SCN_ALIGN_2BYTES', 0x00200000),
    ('IMAGE_SCN_ALIGN_4BYTES', 0x00300000),
    ('IMAGE_SCN_ALIGN_8BYTES', 0x00400000),
    ('IMAGE_SCN_ALIGN_16BYTES', 0x00500000),
    ('IMAGE_SCN_ALIGN_32BYTES', 0x00600000),
    ('IMAGE_SCN_ALIGN_64BYTES', 0x00700000),
    ('IMAGE_SCN_ALIGN_128BYTES', 0x00800000),
    ('IMAGE_SCN_ALIGN_256BYTES', 0x00900000),
    ('IMAGE_SCN_ALIGN_512BYTES', 0x00A00000),
    ('IMAGE_SCN_ALIGN_1024BYTES', 0x00B00000),
    ('IMAGE_SCN_ALIGN_2048BYTES', 0x00C00000),
    ('IMAGE_SCN_ALIGN_4096BYTES', 0x00D00000),
    ('IMAGE_SCN_ALIGN_8192BYTES', 0x00E00000),
    ('IMAGE_SCN_ALIGN_MASK', 0x00F00000),
    ('IMAGE_SCN_LNK_NRELOC_OVFL', 0x01000000),
    ('IMAGE_SCN_MEM_DISCARDABLE', 0x02000000),
    ('IMAGE_SCN_MEM_NOT_CACHED', 0x04000000),
    ('IMAGE_SCN_MEM_NOT_PAGED', 0x08000000),
    ('IMAGE_SCN_MEM_SHARED', 0x10000000),
    ('IMAGE_SCN_MEM_EXECUTE', 0x20000000),
    ('IMAGE_SCN_MEM_READ', 0x40000000),
    ('IMAGE_SCN_MEM_WRITE', 0x80000000)]
SECTION_CHARACTERISTICS = dict([(e[1], e[0]) for e in section_characteristics] + section_characteristics)

def retrieve_flags(flag_dict, flag_filter):
    return [(f[0], f[1]) for f in list(flag_dict.items()) if
            isinstance(f[0], (str, bytes)) and f[0].startswith(flag_filter)]

section_flags = retrieve_flags(SECTION_CHARACTERISTICS, 'IMAGE_SCN_')

insert_test_doc = {}
def get_info(fileName):
    try:
        pe = pefile.PE(fileName)
        op_list_count = {}

        for section in pe.sections:
            flags = []
            for flag in sorted(section_flags):
                if getattr(section, flag[0]):
                    flags.append(flag[0])
            if 'IMAGE_SCN_MEM_EXECUTE' in flags:
                iterable = distorm3.DecodeGenerator(0, section.get_data(), distorm3.Decode32Bits)

                for (offset, size, instruction, hexdump) in iterable:
                    op_code = instruction.split()[0]
                    op_code = str(op_code).lstrip('b')
                    op_code = str(op_code).replace("'","")
                    if op_code not in op_list_count.keys():
                        op_list_count[op_code] = 1
                    elif op_code in op_list_count.keys():
                        op_list_count[op_code] = op_list_count[op_code] + 1

        pe.parse_data_directories(
            pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT'])

        insert_test_doc.update(op_list_count)
        print("[+] insert_test_doc  =====> ",insert_test_doc)
        return insert_test_doc
    except:
        print("[+] GET_MAL_INFO ERROR")
