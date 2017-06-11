# Perceptrons (single-layer neural network)
# update weights (bias input keeps same, only its weight changes)
import  random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
#from matplotlib import style

color = ['b','g','r','c','m','y','k','w']
class Perceptron(object):
  def __init__(self, input):
    self.input = input
    self.weight = random.uniform(0.1, 0.8)

  def setWeight(self, w):
    self.weight = w
  def setInput(self, i):
    self.input = i

class Bias(object):
  def __init__(self):
    self.weight = random.uniform(0.1, 0.8)
    self.input = -1

# t is the threshhold value
def step(a, t): # t = 0
  if a >= t:
    return 1
  else:
    return 0


# numOfPer does not include bias
def singleLayer(numOfPer, andInput, bias, threshold, iterations, learningRate):
  if bias is True:
    biasNode = Bias()
  listOfNode = []
  listOfWeight = []

  # initialize perceptrons
  for i in range(0,numOfPer):
    node = Perceptron(andInput[0][i])
    #print node.input, node.weight
    listOfNode.append(node)
    listOfWeight.append(node.weight)

  # initialize result
  res = []
  for i in range(0, len(andInput)):
    res.append(0)

  outfile = open('result.csv', 'w')
  for i in range (0, iterations):
    gloErr = 0.0
    for l in range(0, len(andInput)):
      # update node weight
      for j in range(0, len(andInput[l]) - 1):
        listOfNode[j].setInput(andInput[l][j])
        listOfNode[j].setWeight(listOfWeight[j])

      sumOfNode = 0.0
      for node in listOfNode:
        sumOfNode += node.weight * node.input
      if bias:
        sumOfNode += biasNode.weight * biasNode.input

      # draw boundary
      if bias == True:
        X = np.linspace(0, 1, 100, endpoint=True)
        C = -listOfNode[0].weight * X / listOfNode[1].weight + \
                       biasNode.weight / listOfNode[1].weight
        plt.ylim(0, 2)
        plt.plot(X, C)
        plt.xlabel('I0')
        plt.ylabel('I1')
        plt.pause(0.05)
      else:
        X = np.linspace(-3, 3, 100, endpoint=True)
        C = -listOfNode[0].weight * X / listOfNode[1].weight
        # plt.ylim(-2, 2)
        plt.plot(X, C)
        plt.xlabel('I0')
        plt.ylabel('I1')
        plt.pause(0.05)

      curOutput = step(sumOfNode, threshold)
      if curOutput >= threshold:
        curOutput = 1
      else:
        curOutput = 0
      if curOutput == andInput[l][len(andInput[l]) - 1]: # if correct, continue
        #print 'cur', curOutput, ': output ', andInput[l][len(andInput[l]) - 1]
        res[l] = curOutput
      else: # update weight
        res[l]= curOutput
        err = float(andInput[l][len(andInput[l]) - 1] - curOutput)/len(andInput[l])
        for num in range(0, len(listOfWeight)):
          listOfWeight[num] = listOfWeight[num] + learningRate * node.input * err
        if bias == True:
          biasNode.weight += learningRate * node.input * err
        # update threshhold t
        threshold = threshold - learningRate * err
        gloErr += abs(curOutput - andInput[l][len(andInput[l]) - 1])
    print 'For iteration', i, ', global error is ', gloErr
    if gloErr == 0.0:
      break
  for j in range(0, len(res)):
    print 'Target value: ', andInput[j][len(andInput[j]) - 1], 'Actual Output: ', res[j]
  print 'Weights: ', listOfWeight, ' Threshold: ', threshold

  while True:
    plt.pause(0.05)

def main():
  xorInput = [[1.0, 0.0, 1.0], [0, 1, 1], [0, 0, 0], [1, 1, 0]]
  singleLayer(2, xorInput, True, 0.5, 100, 0.1)

if __name__ == '__main__':
  main()