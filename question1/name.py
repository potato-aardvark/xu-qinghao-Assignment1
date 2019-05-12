import os
import sys

find = sys.argv[1]
replace = sys.argv[2]
cwd = os.getcwd()

try:
    os.makedirs(os.path.join(cwd, replace))
except FileExistsError:
    pass  # ew

with os.scandir(cwd) as scan:
    for thing in scan:
        if thing.is_file() and thing.path.endswith('.txt'):
            with open(thing.path, 'r') as read_from:
                text = read_from.read()
                if find in text:
                    with open(os.path.join(cwd, replace, thing.name), 'w') \
                        as write_to:
                        write_to.write(text.replace(find, replace))

