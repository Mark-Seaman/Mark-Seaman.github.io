from os import listdir
from os.path import join


for f in sorted(listdir('lesson')):
    path = join('lesson', f)
    # print(path)
    x = open(path).read().splitlines()[0:4]
    print (' - '.join(x))

