import numpy as np
from scipy.optimize import curve_fit

def fit(func, xdata, ydata)

  popt, pcov = curve_fit(func, xdata, ydata)

  return popt, pcov

# print tests only to the screen
if __name__=="__main__":
#  print av(list_of_num)
  import sys
  print fit(sys.argv[1:])
  print "run from the command line"