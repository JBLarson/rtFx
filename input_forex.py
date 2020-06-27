from pandas import DataFrame
import pandas as pd
import numpy as np

contract = "USD/JPY"

b1str, b1avgp, b1size = float(109.25), 51, 100

s1str, s1avgp, s1size = float(109.44), 65, 45

b1r, s1r = b1avgp * b1size, (100 - s1avgp) * s1size

b1w, s1w = 100*b1size - (b1r), (abs(s1size)*s1avgp)

strike_range = np.arange(109.04, 110.04, .1)

print(strike_range)
