import numpy as np
import matplotlib.pyplot as plt

x1 = 0
x2 = 90
y1 = 0
y2 = 90
plt.axis([x1,x2,y1,y2])
plt.axis('on')

plt.grid(True,color = 'b')
plt.title('Mr. John')

xmin = x1
xmax = x2
dx = 10
ymin = y2
ymax = y1
dy = -10
plt.xticks(np.arange(xmin,xmax,dx))
plt.yticks(np.arange(ymin,ymax,dy))

plt.show()