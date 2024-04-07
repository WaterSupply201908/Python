# Lesson 3

import matplotlib.pyplot as plt

data_in = """
x	3
y	2
x	5
y	2
x	3
y	4
x	5
y	4
x	4
y	2
x	5
y	3
x	3
y	3
x	4
y	4
x 3.1
y 2.1
x 4.8
y 2.3
x 3.5
y 3.8
x 4.4
y 3.2
"""
# data from Walker
'''data_in = """
x	2.1
y	2.3
x	3.99
y	3.99
x	2.01
y	3.99
x	3.99
y	2.01
x	2.01
y	2.01
x	3.9
y	3.9
x	2.3
y	3
x	3.9
y	2.1
x	3
y	2.4
x	3
y	3
"""
'''
data_out = """
x	7
y	8
x	2.1
y	5
x	5
y	8
x	1
y	1
x	7
y	1
x	6
y	0.5
x 1
y 7
x 2.2
y 8.3
x 1
y 4
x 6.4
y 5.9
x 3.3
y 0.4
x 4.4
y 5
"""

xlist_in = []
ylist_in = []
for line in data_in.split('\n') :
  if line :
    axis, coord = line.split()
    if axis == "x" :
      xlist_in.append(float(coord))
    if axis == "y" :
      ylist_in.append(float(coord))

xlist_out = []
ylist_out = []
for line in data_out.split('\n') :
  if line :
    axis,coord = line.split()
    if axis == "x" :
      xlist_out.append(float(coord))
    if axis == "y" :
      ylist_out.append(float(coord))

plt.title('title')
plt.plot(xlist_in, ylist_in, 'or')
plt.plot(xlist_out, ylist_out, 'py')
plt.show()