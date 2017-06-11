import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib
import matplotlib.dates as mdates
x = [1,2,3]
y = [5, 7, 4]

x2 = [5,6,7]
y2 = [1,2,3]

# load csv data

with open('example', 'r') as csvfile:
  plots =csv.reader(csvfile, delimiter=',')
  for row in plots:
    x.append(int(row[0]))
    y.append(int(row[1]))
'''

# load data with numpy
x, y = np.loadtxt('example', delimiter=',', unpack=True) # unpack just separate values for x and y

# load data from internet
def bytespdate2num(fmt,encoding='utf-8'):
  strconverter = mdates.strpdate2num(fmt)
  def bytesconverter(b):
    s = b.decode(encoding)
    return strconverter(s)
  return bytesconverter

def graph_data(stock):
  stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
  #source_code = urllib.request.urlopen(stock_price_url).read().decode()
  source_code = urllib.request.urlopen(stock_price_url).read().decode()

  stock_data = []
  split_source = source_code.split('\n')

  for line in split_source:
    split_line = line.split(',')
    if len(split_line) == 6:
      if 'value' not in line:
        stock_data.append(line)

  date, closep, highp, lowp, openp, volumn = np.loadtxt(stock_data, delimiter=',',unpack=True,
                                                        # %Y = full year
                                                        # %Y = partial year
                                                        # %m = number month
                                                        # %d = number day
                                                        # %H = hours
                                                        # %M = minutes
                                                        # %S = seconds
                                                        # 12-06-2016
                                                        # %m-%d-%Y
                                                        converters={0: bytespdate2num('%Y%m%d')})
  plt.plot_date(date, closep, '-')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.show()

graph_data('TSLA')
'''
plt.plot(x,y, label = 'First Line')
#plt.plot(x2,y2,label = 'Second Line')
#plt.bar(x,y,label = 'Bars1', color='r')
#plt.bar(x2,y2,label = 'Bars2', color='c')
#plt.xlabel('Plot Number')
#plt.ylabel('Y value')
plt.scatter(x,y,label = 'scat', color='k', s=100, marker='*')
plt.title('Result')
#plt.legend()
#plt.show()
'''
population_ages = [22, 55, 62, 35, 20,5,7,98,87]
#ids = [x for x in range(len(population_ages))]
bins = [0,10,20,30,40,50,60,70,80,90,100]

# distributions of ages
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)'''
plt.show()