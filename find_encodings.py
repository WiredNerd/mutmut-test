from os import walk
from os.path import join
import traceback
import sys


print(sys.getdefaultencoding())


for r, d, fs in walk('.'):
    for f in fs:
        if f == ".mutmut-cache" \
            or f.endswith('.pyc') \
            or '.git' in r \
            or 'venv' in r :
            continue
        full = join(r, f)
        line = str()
        try:
            with open(full) as file:
                print(f"filename: {full} \tencoding: {file.encoding}")
                for x in file.readlines():
                    pass
        except UnicodeDecodeError as e:
            print(f"filename: {full} {e}")
            traceback.print_exc()

# with open("./src/hello.py", encoding='ascii') as file:
#     line = "see first line"
#     while(line != ""):
#         try:
#             line = file.readline().strip('\n')
#         except UnicodeDecodeError as e:
#             print("line before failed line: \n" + line)