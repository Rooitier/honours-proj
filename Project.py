import numpy as np
import matplotlib.pyplot as plt
import ROOT

start = '<<DATA>>'
end = '<<END>>'
array = []

f = ROOT.TF1("f1", "sin(x)/x", 0., 10.)
f.Draw()

# ***************************************************************************************
# File preparation#
# ***************************************************************************************

with open("demofile.txt") as f:

        for line in f:
                array.append(line.strip())
idx1 = array.index(start)
idx2 = array.index(end)
array = array[idx1+1:idx2]
array = [int(x) for x in array]

plt.plot(array)
plt.show()

