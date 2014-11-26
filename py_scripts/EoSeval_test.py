# -*- coding: utf-8 -*-
"""
Code description goes in here
"""
import numpy
import EoSeq
from scipy.optimize import curve_fit

# Prompt user for filename string
# filename = raw_input("Please enter a file path for P and V data")

# Load in data file
# data = numpy.loadtxt(filename, delimiter = ',')

data = numpy.loadtxt("/Users/Grace/Documents/EoSeval/data/ferropericlase_Mao_2011_2000K.csv", delimiter = ',')

init_params = [0,0,0,0]

testfunc = BM3EOS(init_params)

BM3 = EOS(testfunc)

