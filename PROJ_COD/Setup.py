import sys
from cx_Freeze import setup, Executable
import PROJ_COD.Machine.lee.crawler as crawler

setup(  name = "parser",
        version = "1.0",
        description = "Parser",
        author = "sh1n2",
        executables = [Executable(crawler)])
