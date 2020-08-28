import numpy as np

start = '<<DATA>>'
end = '<<END>>'
with open('demofile.txt') as f:
    array = []
    for line in f: # read rest of lines
        array.append(line.strip())
idx1 = array.index(start)
idx2 = array.index(end)
print(array[idx1+1:idx2])