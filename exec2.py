import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import binput2 as inp

ro = lambda n : round(n, ndigits=2)
rp = lambda n : round(n, ndigits=4)

b1s, b1w, b1r = inp.b1str, inp.b1w, inp.b1r
s1s, s1w, s1r = abs(inp.s1str), inp.s1w, inp.s1r
contract = inp.contract
str_rng = inp.strike_range

b1_rez = [b1w if n >= b1s else -b1r for n in str_rng]
s1_rez = [s1w if pt < s1s else -s1r for pt in str_rng]

net_rez = [b1_rez[i]+s1_rez[i] for i in range(len(b1_rez))]
all_rez = [b1_rez, s1_rez, net_rez]

#string formatting for title variables
b1rT, s1rT = str(b1r).split("."), str(s1r).split(".")


b1T, s1T = contract + ' Over ' + str(b1s), contract + ' Under ' + str(s1s)
b12T = b1T + ' ' + s1T

b1_desc = "Bet 1: Over " + str(b1s) + " | Risk:$" + str(b1rT[0]) + " | Win:$" + str(b1w)
s1_desc = "Bet 2: Under " + str(s1s) + " | Risk:$" + str(s1rT[0]) + " | Win:$" + str(s1w)




def quad_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(221)
	ax2 = fig.add_subplot(222)
	ax3 = fig.add_subplot(223)
	ax4 = fig.add_subplot(224)
	b1pl = ax1.stackplot(str_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T)
	ax1.set_ylabel('Result ($)')
	ax1.set_xticks([])
	s1pl = ax2.stackplot(str_rng, s1_rez, labels=['s1'])
	ax2.set_title(s1T)
	ax2.set_ylabel('Result ($)')
	ax2.set_xticks([])
	netpl = ax3.stackplot(str_rng, net_rez, labels=['net'])
	ax3.set_ylabel('Result ($)')
	ax3.set_xlabel('Strike Price')
	ax3.set_title('Net Outcome')
	b1plo = ax4.stackplot(str_rng, b1_rez, labels=['b1'])
	s1plo = ax4.stackplot(str_rng, s1_rez, labels=['s1'])
	netplo = ax4.stackplot(str_rng, net_rez, labels=['net'])
	ax4.set_title("Both positions and net")
	ax4.set_ylabel('Result ($)')
	ax4.set_xlabel('Strike Price')
	
	return plt.show()


def b12_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)
	b1pl = ax1.stackplot(str_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T)
	ax1.set_ylabel('Result ($)')
	s1pl = ax2.stackplot(str_rng, s1_rez, labels=['s1'])
	ax2.set_title(s1T)
	ax2.set_ylabel('Result ($)')
	ax2.set_xlabel('Strike Price')
	plt.show()


def b1_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(str_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T)
	ax1.set_ylabel('Result ($)')
	ax1.set_xlabel('Strike Price')
	plt.show()


def s1_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(str_rng, s1_rez, labels=['s1'])
	ax1.set_title(s1T)
	ax1.set_ylabel('Result ($)')
	ax1.set_xlabel('Strike Price')
	plt.show()



def net_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(str_rng, net_rez, labels=['net'])
	ax1.set_title('USD / JPY 5PM')
	ax1.set_ylabel('Result ($)')
	ax1.set_xlabel('Strike Price')
	plt.show()


def all_plot():
	fig = plt.figure(figsize=(10,6))
	ax4 = fig.add_subplot(111)
	b1plo = ax4.stackplot(str_rng, b1_rez, labels=['b1'])
	s1plo = ax4.stackplot(str_rng, s1_rez, labels=['s1'])
	netplo = ax4.stackplot(str_rng, net_rez, labels=['net'])

	ax4.set_title('Iron Condor - Bull Put Spread & Bear Call Spread')
	ax4.set_ylabel('Result ($)')
	plt.legend(loc='upper left')
	plt.show()

print(net_rez)


#b1_plot()
#s1_plot()
#b12_plot()
#net_plot()

#all_plot()
quad_plot()


