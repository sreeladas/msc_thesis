import matplotlib.pyplot as plt

x = [0.0, .25, .5, .75, 1.0, 1.25, 1.5, 1.75, 2.00]
oy = [242, 1940, 3880, 5810, 6000, 6000, 6000, 6000, 6000]
oy = [i/726.0 for i in oy]
oy2 = [242, 1940, 3880, 5810, 7750, 9690, 11600, 13600, 15500]
oy2 = [i/726.0 for i in oy2]
ty = [(i*2.0/.5+1.0)/3.0 for i in x]
test1 = [(i*4.0/.5+1.0)/3.0 for i in x]
test2 = [(i*6.25/.5+1.0)/3.0 for i in x]
test3 = [min((i*15/.5+1.0)/3.0, 8.25) for i in x]

ax1=plt.subplot(1,2,2)
plt.plot(x, ty, 'b-', label='Default')
plt.plot(x, oy, 'r-', label='Old Script 1')
plt.plot(x, oy2, 'g-', label='Old Script 2')
plt.plot(x, test1, 'c-', label='Test 1')
plt.plot(x, test2, 'm-', label='Test 2')
plt.plot(x, test3, 'k-', label='Test 3')
plt.legend()
plt.xlabel("Offset from camera center (deg)")
plt.ylabel("Relative weight")

ax2=plt.subplot(1,2,1)
plt.plot(x, ty, 'b-', label='Default')
plt.plot(x, test1, 'c-', label='Test 1')
plt.plot(x, test2, 'm-', label='Test 2')
plt.plot(x, test3, 'k-', label='Test 3')
plt.legend()
plt.xlabel("Offset from camera center (deg)")
plt.ylabel("Relative weight")
plt.show()

plt.savefig("../images/weights.png")
