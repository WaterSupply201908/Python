# Lesson 4

import requests
import matplotlib.pyplot as plt

api_key = "b6a535e0-b5fc-11ed-bd8c-bd5c6dca099d45ce4cf3-33f3-4155-bc38-0db0e1f18902"

#testingPoint = [10, 11]
testingPoint = [3.14159265358, 2.1]
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

url = "https://machinelearningforkids.co.uk/api/scratch/"+ api_key + "/classify"
prediction = requests.post(url, json={ "data" : testingPoint }).json()[0]["class_name"]

plt.title("Prediction : " + prediction)
plt.plot(testingPoint[0],testingPoint[1],'sk')
plt.plot(xlist_in, ylist_in, 'or')
plt.plot(xlist_out, ylist_out, 'py')
plt.show()