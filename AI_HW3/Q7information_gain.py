# calculate information again

import math
def get_entropy(list_of_distribute):
  sum  = 0.0
  for l in list_of_distribute:
    sum += l
  #print sum

  result = 0.0
  for l in list_of_distribute:
    if l == 0:
      continue
    result += -1 * (l / float(sum)) * math.log(l / float(sum), 2)
    #print l / float(sum)
  return result

def info_gain(input):
  if len(input) == 0:
    return
  original_entropy = get_entropy(input[0])
  sum_entropy = 0.0
  sum =  input[0][0] + input[0][1]
  #print 'sum',sum
  print 'original_entropy', original_entropy
  if len(input) == 1:
    return original_entropy
  for i in range(1, len(input)):
    if isinstance(input[i], list):
      cur_entropy = get_entropy(input[i])
      print "For group ", i, ", ", input[i], "the entropy is ", cur_entropy
      sum_entropy += cur_entropy * ((input[i][0] + input[i][1]) * 1.0/sum)
    else:
      print "please follow this input format, for instance, [[4,6],[4,0],[5,1]]"
  print "The information gain is ", \
        original_entropy - sum_entropy

def main():
  ''' input = [[6, 6], [0, 2], [4, 0], [2, 4]]
  #input = [[6, 4],[3,2],[0,2],[3,0]]
  #input = [[6, 4], [4, 2], [2, 2]]
  #input = [[6, 4], [1, 2], [2, 1], [3, 1]]
  print input
  print info_gain(input)
  print '============='
'''
  print 'For Question 7 (1)'
  input = [[6, 4], [3, 2], [0, 2], [3, 0]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 4], [4, 2], [2, 2]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 4], [1, 2], [2, 1],[3,1]]
  print input
  print info_gain(input)
  print '============='


  print 'For Question 7 (2)'
  input = [[6, 6], [0, 2], [4, 0], [2, 4]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [3, 3],[3,3]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [2, 3], [4, 3]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [5, 2], [1, 4]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [4, 0], [2, 4], [0, 2]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [3, 4], [2, 0], [1, 2]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [2, 2], [4, 4]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [3, 2], [3, 4]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [1, 1], [2, 2], [2, 2],[1,1]]
  print input
  print info_gain(input)
  print '============='
  input = [[6, 6], [4, 2], [1, 1], [1, 1], [0, 2]]
  print input
  print info_gain(input)
  print '============='

####################### main #########################
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print "[FATAL] " + str(e)
        raise
