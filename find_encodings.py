from os import walk
from os.path import join


for r, d, fs in walk('.'):
    for f in fs:
        if f == ".mutmut-cache" \
            or f.endswith('.pyc')\
            or '.git' in r:
            continue
        full = join(r, f)
        print(full)
        with open(full, encoding='utf8') as foo:
            foo.read()