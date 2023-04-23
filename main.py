import math
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from celluloid import Camera
import numpy as np
Ax = -0.353
Bx = 0.353
'''Ay = 0.3'''
By = 0.3
C = 3 * math.pi / 8
def F(x, Ay):
  Ax = -0.353
  Bx = 0.353
  C = 3 * math.pi / 8
  t = 0.005
  x_new = [0]*5
  x_new[0] = (x[0] + x[2]*(math.cos((3*math.pi/2 - x[3]))) - Ax)*t
  x_new[1] = (x[1] + x[2] * (math.cos(3 * math.pi / 2 + x[4])) - Bx)*t
  x_new[2] = (x[2] + x[2] * (math.sin((3 * math.pi / 2 - x[3]))) - Ay) * t
  x_new[3] = ((x[3]+x[4])*x[2]+(x[1]-x[0]) - C)*t
  x_new[4] = (x[2] + x[2]*math.sin(3 * math.pi / 2 + x[4]) - Ay)*t
  return x_new



t_true = 0.01
Ay = 0.3
Vy = 0.1
m = 100
p = 2000
g = 9.8
fig = plt.figure()
ax = fig.add_subplot()
camera = Camera(fig)
for n in range(250):
  X = np.array([-0.3, 0.66, 0.6, 0.7, -0.7])
  temp = np.array([0] * 5)
  delta = 0.0000001

  while True:
    temp = F(X, Ay)
    f = 1
    for j in range(5):
      if abs(temp[j]) > delta:
        f = 0
    X = X - temp
    if f == 1:
      break

  Ay = Ay + (Vy) * t_true
  l = X[1] - X[0]
  Vy = Vy + (1/m)*(p*l - m*g)*t_true



  R = math.sqrt((X[0] - Ax)**2 + (X[2] - Ay)**2)
  a = patches.Arc(xy=(X[0],X[2]), width=2*X[2], height=2*X[2], angle=0.0, theta1 = 270 - math.degrees(X[3]), theta2 = 270)
  ax.add_patch(a)


  R1 = math.sqrt((X[0] - Ax)**2 + (X[2] - Ay)**2)
  a1 = patches.Arc(xy=(X[1],X[2]), width=2*X[2], height=2*X[2], angle=0.0, theta1 = -90, theta2 = math.degrees(X[4])-90)
  ax.add_patch(a1)
  ax.hlines(Ay, Ax, Bx)
  ax.hlines(0, X[0], X[1])
  plt.xlim(-0.5, 0.5)
  plt.ylim(0, 1)
  camera.snap()

animation = camera.animate(interval=600, repeat=True, repeat_delay=100)

#animation.save('animation.gif', writer='pillow')
plt.show()

