from os import walk
from os.path import join
import traceback


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
                for x in file.readlines():
                    line = x
        except UnicodeDecodeError as e:
            traceback.print_stack()
            print(full)
            print(line)