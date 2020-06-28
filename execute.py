import matplotlib.pyplot as plt

import input_forex as inp

ro = lambda n : round(n, ndigits=2)
rp = lambda n : round(n, ndigits=4)

b1s, b1w, b1r = inp.b1str, inp.b1w, inp.b1r
s1s, s1w, s1r = abs(inp.s1str), inp.s1w, inp.s1r
contract = inp.contract
stk_rng = inp.strike_range

b1_rez = [b1w if stk >= b1s else -b1r for stk in stk_rng]
s1_rez = [s1w if stk < s1s else -s1r for stk in stk_rng]

net_rez = [b1_rez[i]+s1_rez[i] for i in range(len(b1_rez))]
all_rez = [b1_rez, s1_rez, net_rez]

b1T, s1T, b1T2, s1T2 = inp.b1T, inp.s1T, inp.b1T2, inp.s1T2

def quad_plot():
	fig = plt.figure(figsize=(10,6))
	ax1, ax2 = fig.add_subplot(221), fig.add_subplot(222)
	ax3, ax4 = fig.add_subplot(223), fig.add_subplot(224)
	b1pl = ax1.stackplot(stk_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T2)
	ax1.set_ylabel('Result ($)', fontsize=16)
	ax1.set_xticks([])
	s1pl = ax2.stackplot(stk_rng, s1_rez, labels=['s1'])
	ax2.set_title(s1T2)
	ax2.set_xticks([])
	netpl = ax3.stackplot(stk_rng, net_rez, labels=['net'])
	ax3.set_ylabel('Result ($)', fontsize=16)
	ax3.set_xlabel('Strike Price', fontsize=16)
	ax3.set_title('Net Outcome')
	b1plo = ax4.stackplot(stk_rng, b1_rez, labels=['b1'])
	s1plo = ax4.stackplot(stk_rng, s1_rez, labels=['s1'])
	netplo = ax4.stackplot(stk_rng, net_rez, labels=['net'])
	ax4.set_title("Buy, Sell, and Net")
	ax4.set_xlabel('Strike Price', fontsize=16)
	plt.show()


def b12_plot():
	fig = plt.figure(figsize=(10,6))
	ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)
	b1pl = ax1.stackplot(stk_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T2, fontsize=18)
	ax1.set_xticks([])
	ax1.set_ylabel('Result ($)', fontsize=16)
	s1pl = ax2.stackplot(stk_rng, s1_rez, labels=['s1'])
	ax2.set_title(s1T2, fontsize=18)
	ax2.set_ylabel('Result ($)', fontsize=16)
	ax2.set_xlabel('Strike Price', fontsize=16)
	plt.show()


def b1_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(stk_rng, b1_rez, labels=['b1'])
	ax1.set_title(b1T, fontsize=20)
	ax1.set_ylabel('Result ($)', fontsize=16)
	ax1.set_xlabel('Strike Price', fontsize=16)
	plt.show()


def s1_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(stk_rng, s1_rez, labels=['s1'])
	ax1.set_title(s1T, fontsize=20)
	ax1.set_ylabel('Result ($)', fontsize=16)
	ax1.set_xlabel('Strike Price', fontsize=16)
	plt.show()



def net_plot():
	fig = plt.figure(figsize=(10,6))
	ax1 = fig.add_subplot(111)
	b1pl = ax1.stackplot(stk_rng, net_rez, labels=['net'])
	ax1.set_title('Net', fontsize=20)
	ax1.set_ylabel('Result ($)', fontsize=16)
	ax1.set_xlabel('Strike Price', fontsize=16)
	plt.show()


def all_plot():
	fig = plt.figure(figsize=(10,6))
	ax4 = fig.add_subplot(111)
	b1plo = ax4.stackplot(stk_rng, b1_rez, labels=['b1'])
	s1plo = ax4.stackplot(stk_rng, s1_rez, labels=['s1'])
	netplo = ax4.stackplot(stk_rng, net_rez, labels=['net'])

	ax4.set_title('Buy, Sell, and Net', fontsize=20)
	ax4.set_ylabel('Result ($)', fontsize=16)
	plt.legend(loc='upper left')
	plt.show()

#b1_plot()
#s1_plot()
#b12_plot()
#net_plot()
#all_plot()
quad_plot()
