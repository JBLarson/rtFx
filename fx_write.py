import numpy as np

ro = lambda n : round(n, ndigits=2)
rp = lambda n : round(n, ndigits=4)


contract, stk_rng = "USD/JPY>", np.arange(108.50, 110.50, .1)

b1str, b1avgp, b1size = float(109.25), 79, 10
s1str, s1avgp, s1size = float(109.44), 45, 8

b1r, s1r = b1avgp * b1size, (100 - s1avgp) * s1size
b1w, s1w = 100*b1size - (b1r), (abs(s1size)*s1avgp)

b1T = "Buy " + str(b1size) + " contracts of " + contract + str(b1str) + " @ " + str(b1avgp) + "$"
s1T = "Sell " + str(s1size) + " contracts of " + contract + str(s1str) + " @ " + str(s1avgp) + "$"

b1T2, s1T2 = "Buy " + contract + str(b1str), "Sell " + contract + str(s1str)



b1_rez = [b1w if stk >= b1str else -b1r for stk in stk_rng]
s1_rez = [s1w if stk < abs(s1str) else -s1r for stk in stk_rng]

net_rez = [b1_rez[i]+s1_rez[i] for i in range(len(b1_rez))]
all_rez = [b1_rez, s1_rez, net_rez]

b1T, s1T, b1T2, s1T2 = b1T, s1T, b1T2, s1T2



def fx_write():
	import sys

	sys.stdout = open('rezults.txt', 'wt')


	"""
	for n in range(0,10):
		eval(f'print(stk_rng[{n}]), \',\', print(net_rez[{n}])')
		print(stk_rng[n]), ',', print(net_rez[n])

	"""


	print(stk_rng[0], ',', net_rez[0])
	print(stk_rng[1], ',', net_rez[1])
	print(stk_rng[2], ',', net_rez[2])
	print(stk_rng[3], ',', net_rez[3])
	print(stk_rng[4], ',', net_rez[4])
	print(stk_rng[5], ',', net_rez[5])
	print(stk_rng[6], ',', net_rez[6])
	print(stk_rng[7], ',', net_rez[7])
	print(stk_rng[8], ',', net_rez[8])
	print(stk_rng[9], ',', net_rez[9])
	print(stk_rng[10], ',', net_rez[10])
	print(stk_rng[11], ',', net_rez[11])
	print(stk_rng[12], ',', net_rez[12])
	print(stk_rng[13], ',', net_rez[13])
	print(stk_rng[14], ',', net_rez[14])
	print(stk_rng[15], ',', net_rez[15])
	print(stk_rng[16], ',', net_rez[16])
	print(stk_rng[17], ',', net_rez[17])
	print(stk_rng[18], ',', net_rez[18])
	print(stk_rng[19], ',', net_rez[19])




	#print(stk_rng[10], ',', net_rez[10])
	#print(stk_rng[11], ',', net_rez[11])
	sys.stdout = open('b1s1.txt', 'wt')


	"""
	for n in range(0,10):
	print(b1_rez[n]), ',', print(s1_rez[n])
	"""

	print(b1_rez[0], ',', s1_rez[0])
	print(b1_rez[1], ',', s1_rez[1])
	print(b1_rez[2], ',', s1_rez[2])
	print(b1_rez[3], ',', s1_rez[3])
	print(b1_rez[4], ',', s1_rez[4])
	print(b1_rez[5], ',', s1_rez[5])
	print(b1_rez[6], ',', s1_rez[6])
	print(b1_rez[7], ',', s1_rez[7])
	print(b1_rez[8], ',', s1_rez[8])
	print(b1_rez[9], ',', s1_rez[9])
	print(b1_rez[10], ',', s1_rez[10])
	print(b1_rez[11], ',', s1_rez[11])
	print(b1_rez[12], ',', s1_rez[12])
	print(b1_rez[13], ',', s1_rez[13])
	print(b1_rez[14], ',', s1_rez[14])
	print(b1_rez[15], ',', s1_rez[15])
	print(b1_rez[16], ',', s1_rez[16])
	print(b1_rez[17], ',', s1_rez[17])
	print(b1_rez[18], ',', s1_rez[18])
	print(b1_rez[19], ',', s1_rez[19])

fx_write()

