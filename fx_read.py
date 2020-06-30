import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure(figsize=(6, 10))
#ax1 = fig.add_subplot(111)

ax1, ax2 = fig.add_subplot(411), fig.add_subplot(412)
ax3, ax4 = fig.add_subplot(413), fig.add_subplot(414)


def animate(i):
    pullData = open("rezults.txt","r").read()
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
    ax1.set_title('Real-Time Forex Model', fontsize=20)
    ax1.set_ylabel('Buy($)', fontsize=14)
    ax2.clear()
    ax2.stackplot(pts,s1)
    ax2.set_ylabel('Sell($)', fontsize=14)
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






def animat3(i):
    pullData = open("rezults.txt","r").read()
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
    ax1.stackplot(pts,b1, labels=['over'])
    ax1.stackplot(pts,s1, labels=['under'])
    ax1.stackplot(pts,net, labels=['net'])

    ax1.set_title('Over, Under, and Net($)')
    ax1.set_xlabel('Strike Price')
    ax1.set_ylabel('Result($)')
    plt.legend(loc='upper left')



#anim = animation.FuncAnimation(fig, animat3, interval=1000)



plt.show()



