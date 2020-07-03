import sys
import numpy as np
import os

ro = lambda n : round(n, ndigits=2)

contract, stk_rng = "USD/JPY>", np.arange(108.50, 109.50, .1)

b1str, b1avgp, b1size = float(109.25), 59, 4

s1a = True

if s1a == True: s1str, s1avgp, s1size = float(109.44), 40, 20
elif s1a == False: s1str, s1avgp, s1size = float(109.54), 35, 50

#risk and win variables
b1r, s1r = b1avgp * b1size, (100 - s1avgp) * s1size
b1w, s1w = ro(100*b1size - (b1r)), ro((abs(s1size)*s1avgp))
#result lists
b1_rez = [b1w if stk >= b1str else -b1r for stk in stk_rng]
s1_rez = [s1w if stk < abs(s1str) else -s1r for stk in stk_rng]
net_rez = [b1_rez[i]+s1_rez[i] for i in range(len(b1_rez))]

#title variables
b1T, s1T = "Buy " + contract + str(b1str), "Sell " + contract + str(s1str)


def fx_write():
	dir_fd = os.open('results', os.O_RDONLY)
	def opener(path, flags):
			return os.open(path, flags, dir_fd=dir_fd)

	with open('results.txt', 'w', opener=opener) as f:
		for n in range(0,len(stk_rng)): print(stk_rng[n], ',', net_rez[n], file=f)

	with open('b1s1.txt', 'w', opener=opener) as f:
		for n in range(0,len(stk_rng)): print(b1_rez[n], ',', s1_rez[n], file=f)

	os.close(dir_fd)


fx_write()
