import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from fx_write import b1T, s1T

fig = plt.figure(figsize=(10, 6))
ax1, ax2 = fig.add_subplot(221), fig.add_subplot(222)
ax3, ax4 = fig.add_subplot(223), fig.add_subplot(224)


def animate():
    pullData = open("results.txt","r").read()
    dataArray = pullData.split('\n')
    pts, net, b1, s1 = [], [], [], []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            pts.append(float(x))
            net.append(float(y))
    
    pullData1 = open("b1s1.txt", "r").read()
    dataArray1 = pullData1.split('\n')
    for eachLine in dataArray1:
        if len(eachLine)>1:
            j,b = eachLine.split(',')
            b1.append(float(j))
            s1.append(float(b))

    ax1.clear()
    ax1.stackplot(pts,b1)
    ax1.set_title(b1T, fontsize=16)
    ax1.set_ylabel('Result($)', fontsize=14)
    ax2.clear()
    ax2.stackplot(pts,s1)
    ax2.set_title(s1T, fontsize=16)
    ax2.set_ylabel('Result($)', fontsize=14)
    ax3.clear()
    ax3.stackplot(pts,net)
    ax3.set_ylabel('Net($)', fontsize=14)
    ax4.clear()
    ax4.stackplot(pts,b1, labels=['over'])
    ax4.stackplot(pts,s1, labels=['under'])
    ax4.stackplot(pts,net, labels=['net'])
    ax4.set_xlabel('Strike Price', fontsize=16)
    ax4.set_ylabel('All($)', fontsize=14)
    plt.legend(loc='lower left')

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
