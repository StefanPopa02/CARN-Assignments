import numpy as np
import matplotlib.pyplot as plt


def isToTheLeftOfLine(x_point, y_point):
    return (a * x_point + b * y_point + c) < 0


def classifyPoint(x, y, label):
    leftSide = isToTheLeftOfLine(x, y)
    if label == -1 and leftSide is True:
        return True
    else:
        return False


x1 = np.random.uniform(0, 45, 50)
y1 = np.random.uniform(0, 100, 50)
leftPoints = np.vstack((x1, y1, np.ones(50))).T

x2 = np.random.uniform(55, 100, 50)
y2 = np.random.uniform(0, 100, 50)
rightPoints = np.vstack((x2, y2, np.ones(50) * -1)).T

allPoints = np.concatenate((leftPoints, rightPoints))
print("Number of points:", len(allPoints))

for point in allPoints:
    a = 1
    b = -1
    c = 0
    classification = classifyPoint(point[0], point[1], point[2])
    print("x=", point[0], " y=", point[1], " label=", point[2], "classif", classification)

x = np.linspace(0, 100, 100)
a = 1
b = -1
c = 0
y = (a * x + c) / (-1 * b)
plt.plot(x, y, '-r')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.grid()

plt.scatter(x1, y1, edgecolors='red')
plt.scatter(x2, y2, edgecolors='pink')
plt.show()
