import numpy as np

ro = lambda n : round(n, ndigits=2)
rp = lambda n : round(n, ndigits=4)


contract, stk_rng = "USD/JPY>", np.arange(109.04, 110.04, .1)

b1str, b1avgp, b1size = float(109.25), 65, 10
s1str, s1avgp, s1size = float(109.44), 45, 8

b1r, s1r = b1avgp * b1size, (100 - s1avgp) * s1size
b1w, s1w = 100*b1size - (b1r), (abs(s1size)*s1avgp)

b1T = "Buy " + str(b1size) + " contracts of " + contract + str(b1str) + " @ " + str(b1avgp) + "$"
s1T = "Sell " + str(s1size) + " contracts of " + contract + str(s1str) + " @ " + str(s1avgp) + "$"

b1T2, s1T2 = "Buy " + contract + str(b1str), "Sell " + contract + str(s1str)

b1_rez = [b1w if stk >= b1str else -b1r for stk in stk_rng]
s1_rez = [s1w if stk < abs(s1str) else -s1r for stk in stk_rng]

net_rez = [b1_rez[i]+s1_rez[i] for i in range(len(b1_rez))]
