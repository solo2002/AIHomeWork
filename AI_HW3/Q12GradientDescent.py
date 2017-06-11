import numpy as np
import matplotlib.pyplot as plt
from sys import maxint

def E(w):
  return (w+1) * (w-1) * (w-3) * (w-4)

# calculate delta w
def f(a, w):
  return -a * (4 * pow(w, 3) - 2 * pow(w, 2) + 22 * w + 7)

def main():
  w = 3
  a = 0.01
  minE = maxint
  elist =[]
  wlist =[]
  for i in range(0, 100):
    elist.append(E(w))
    wlist.append(w)
    w = w + f(a, w)
    if minE > E(w):
      minE = E(w)
    if w < -2 or w > 5:
      print 'w ', w, ' is out of range (-2, 5)'
      break

  print 'Minimum value of E is ', minE
  plt.xlabel("Value of w")
  plt.ylabel("Value of E(w)")
  plt.scatter(wlist, elist)
  X = np.linspace(-1, 5, 100, endpoint=True)
  C = (X + 1)*(X - 1)*(X - 3)*(X - 4)
  plt.plot(X, C, color = 'r')
  plt.show()

if __name__ == '__main__':
  main()