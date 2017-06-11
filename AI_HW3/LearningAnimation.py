import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#     pullData = open("result.csv","r").read()
#     dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     for eachLine in dataArray:
#         if len(eachLine)>1:
#             x,y = eachLine.split(',')
#             xar.append(float(x))
#             yar.append(float(y))
#
#     ax1.clear()
#     ax1.plot(xar,yar)
#     plt.pause(0.05)
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()

# style.use('fivethirtyeight')
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
#
# def animate(i):
#   graph_data = open('result.csv','r').read()
#   lines = graph_data.split('\n')
#   xs = []
#   ys = []
#   for line in lines:
#     if len(line) > 1:
#       x, y = line.split(',')
#       xs.append(float(x))
#       ys.append(float(y))
#
#   ax1.clear()
#   ax1.plot(xs,ys)
#
# ani = animation.FuncAnimation(fig, animate, interval=6000)
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
#
# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))  # update the data
#     return line,
#
#
# # Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.ma.array(x, mask=True))
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#                               interval=25, blit=False)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import pylab as p

graph_data = open('result.csv','r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
  if len(line) > 1:
    x, y = line.split(',')
    xs.append(float(x))
    ys.append(float(y))

#plt.axis([-1, 1, -1, 1])
print len(xs)
#print ys
plt.ion()

for i in range(len(xs)):
    y = ys[i]
    x = xs[i]
    #plt.plot(x, y, color='k',)
    #plt.scatter(x, y,c='c')
    print (x,y)
    plt.plot((x,y),c='r')
    plt.pause(0.05)
    plt.show()


while True:
  plt.pause(0.05)

graph_data = open('result.csv', 'r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
  if len(line) > 1:
    x, y = line.split(',')
    xs.append(float(x))
    ys.append(float(y))

# plt.axis([-1, 1, -1, 1])
print len(xs)
# print ys
plt.ion()

for i in range(0, len(xs), 2):
  y = ys[i]
  x = xs[i]
  x1 = ys[i + 1]
  y1 = ys[i + 1]

  # plt.plot(x, y, color='k',)
  plt.scatter(x, y, c='c')
  print (x, y)
  plt.plot((x, y), (x1, y1), c='r')
  plt.pause(0.05)
  plt.show()

while True:
  plt.pause(0.05)
