# -*- coding: utf-8 -*-
"""
Code description goes in here
"""

# Import modules
import numpy
import EoSeq
import EOS
import matplotlib.pyplot as plt


# Prompt user for filename string
# filename = raw_input("Please enter a file path for P and V data")

# Load in data file
# data = numpy.loadtxt(filename, delimiter = ',')

PV = numpy.loadtxt("/Users/Grace/Documents/EoSeval/data/ferropericlase_Mao_2011_2000K.csv", delimiter = ',', skiprows=6)
P = PV[:,0]
V = PV[:,1]

plt.plot(P,V,'bo')

parameters = [1.0,10.0,1.0]

testfunc = EoSeq.BM3EOS

BM3 = EOS.EOS(testfunc)

BM3.fit(P, V, parameters)

Vfit = numpy.linspace(V.min(), V.max(), 100)
#
Pfit = BM3.evaluate_list(Vfit)
#
plt.plot(P, V, 'bo', Pfit, Vfit, 'r-')