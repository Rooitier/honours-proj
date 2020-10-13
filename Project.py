import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
from array import array



start = '<<DATA>>'
end = '<<END>>'
array = []



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


# ***************************************************************************************
# Calculation#
# ***************************************************************************************

n = len(array)
x = list(range(n))
y = array




aspline = InterpolatedUnivariateSpline(x,y,k=2)
area = aspline.integral(769,848)
print(area)
#plt.plot(array)
#plt.show()



