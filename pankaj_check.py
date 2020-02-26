from mmap import mmap, ACCESS_READ
import contextlib
from os import path
from shutil import move

for filename in glob.iglob('*.txt'):
    with open(filename) as f:
        with contextlib.closing(mmap(f.fileno(), 0, access=ACCESS_READ)) as s:
            if s.find('* Test Outcome : failure') != -1:
                src_file = path.join(dirSTART, filename)
                dst_file = path.join(dirFAIL, filename)
                move(src_file, dst_file)
