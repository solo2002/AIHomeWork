import random
import math
import matplotlib.pyplot as plt

def circle_data(sample_number, data, labels):
  if sample_number%2 != 0:
    sample_number += 1
  if sample_number <= 0:
    sample_number = 100
  # generate '1' data
  for i in range(sample_number/2):
    r = random.uniform(0.0, 2.0);
    t = random.uniform(0.0, 2 * math.pi)
    data.append((r * math.sin(t), r * math.cos(t)))
    labels.append(1)

  # generate '0' data
  for i in range(sample_number/2):
   r = random.uniform(3.0, 5.0)
   t = 2 * math.pi * i / 50.0
   data.append((r * math.sin(t), r * math.cos(t)))
   labels.append(0)

def spiral_data(sample_number, data, labels):
  if sample_number % 2 != 0:
    sample_number += 1
  if sample_number <= 0:
    sample_number = 100
  # generate '1' data
  for i in range(sample_number / 2):
    r = i / (sample_number / 2.0) * 5 + random.uniform(-0.1, 0.1)
    t = 1.25 * i / (sample_number / 2.0) * 2 * math.pi + random.uniform(-0.1, 0.1)
    data.append((r * math.sin(t), r * math.cos(t)))
    labels.append(1)

  # generate '0' data
  for i in range(sample_number / 2):
    r = i / (sample_number / 2.0) * 5.0 + random.uniform(-0.1, 0.1)
    t = 1.25 * i / (sample_number / 2.0) * 2 * math.pi + \
        random.uniform(-0.1, 0.1) + math.pi
    data.append((r * math.sin(t), r * math.cos(t)))
    labels.append(0)

def xor_data(sample_number, data, labels):
  if sample_number <= 0:
    sample_number = 100

  padding = 0.3
  for i in range(sample_number):
    x = random.uniform(-5.0, 5.0)
    if x > 0:
      x += padding
    else:
      x -= padding
    y = random.uniform(-5.0, 5.0)
    if x > 0:
      x += padding
    else:
      x -= padding
    data.append((x, y))
    if x * y >= 0:
      labels.append(1)
    else:
      labels.append(0)

def gauss_data(sample_number, data, labels):
  if sample_number <= 0:
    sample_number = 100

  # generate '0' data
  for i in range(sample_number / 2):
    r = random.uniform(0, 0.4)
    t = random.uniform(0, 0.4)
    data.append((r, t))
    labels.append(0)

  # generate '1' data
  for i in range(sample_number / 2):
    r = random.uniform(0.5, 1)
    t = random.uniform(0.5, 1)
    data.append((r, t))
    labels.append(1)
def main():
  cdata = []
  clabels = []
  csample_number = 100
  circle_data(csample_number, cdata, clabels)

  cx =[]
  cy =[]
  cx1 = []
  cy1=[]

  # #for gauss, circle and spiral data plot
  for i in range(csample_number/2):
    cx.append(cdata[i][0])
    cy.append(cdata[i][1])
  for i in range(csample_number/2, csample_number):
    cx1.append(cdata[i][0])
    cy1.append(cdata[i][1])
  plt.title('Circle Data')
  plt.scatter(cx, cy,color='b')
  plt.scatter(cx1, cy1,color='r')
  plt.show()

  cx =[]
  cy =[]
  cx1 = []
  cy1=[]
  cdata = []
  clabels = []
  spiral_data(csample_number, cdata, clabels)
  # #for gauss, circle and spiral data plot
  for i in range(csample_number/2):
    cx.append(cdata[i][0])
    cy.append(cdata[i][1])
  for i in range(csample_number/2, csample_number):
    cx1.append(cdata[i][0])
    cy1.append(cdata[i][1])
  plt.title('Spiral Data')
  plt.scatter(cx, cy,color='b')
  plt.scatter(cx1, cy1,color='r')
  plt.show()

  cx =[]
  cy =[]
  cx1 = []
  cy1=[]
  cdata = []
  clabels = []
  gauss_data(csample_number, cdata, clabels)
  # #for gauss, circle and spiral data plot
  for i in range(csample_number/2):
    cx.append(cdata[i][0])
    cy.append(cdata[i][1])
  for i in range(csample_number/2, csample_number):
    cx1.append(cdata[i][0])
    cy1.append(cdata[i][1])
  plt.title('Gauss Data')
  plt.scatter(cx, cy,color='b')
  plt.scatter(cx1, cy1,color='r')
  plt.show()

  x =[]
  y =[]
  x1 = []
  y1=[]
  data = []
  labels = []
  sample_number = 100
  xor_data(sample_number, data, labels)
  # for xor data plot
  for i in range(sample_number):
    if labels[i] == 0:
      x.append(data[i][0])
      y.append(data[i][1])
    if labels[i] == 1:
      x1.append(data[i][0])
      y1.append(data[i][1])
  plt.title('XOR Data')
  plt.scatter(x, y,color='b')
  plt.scatter(x1, y1,color='r')
  plt.show()

if __name__ == '__main__':
  main()