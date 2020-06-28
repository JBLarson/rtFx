import numpy as np

contract = "USD/JPY>"
strike_range = np.arange(109.04, 110.04, .1)

b1str, b1avgp, b1size = float(109.25), 65, 10
s1str, s1avgp, s1size = float(109.44), 45, 8

b1r, s1r = b1avgp * b1size, (100 - s1avgp) * s1size
b1w, s1w = 100*b1size - (b1r), (abs(s1size)*s1avgp)

b1T = "Buy " + str(b1size) + " contracts of " + contract + str(b1str) + " @ " + str(b1avgp) + "$"
s1T = "Sell " + str(s1size) + " contracts of " + contract + str(s1str) + " @ " + str(s1avgp) + "$"

b1T2, s1T2 = "Buy " + contract + str(b1str), "Sell " + contract + str(s1str)
