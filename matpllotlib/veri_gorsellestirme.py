import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
print(x)
y = np.arange(2,11,2)
print(y)

plt.plot(x, y,"red")

plt.subplot(2,2,1)
plt.plot(x, y,"blue")
plt.subplot(2,2,2)
plt.plot(y, x,"red")
plt.subplot(2,2,3)
plt.plot(y, x,"orange")
plt.subplot(2,2,4)
plt.plot(x, x ** 2,"green")

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.2,0.8,0.8])
axes2 = fig.add_axes([0.4,0.5,0.4,0.3])

axes1.plot(y,x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")

axes2.plot(y,x)
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")

fig,axes = plt.subplots(nrows = 2,ncols = 1)

axes[0].plot(x,y)
axes[0].set_title("axes 1")

axes[1].plot(x,x ** 3)
axes[1].set_title("axes 2")

plt.tight_layout()

fig = plt.figure(figsize = (8,6))
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color = "purple")

fig,axes = plt.subplots(nrows = 2, ncols = 1,figsize = (8,6))
axes[0].plot(x,y,color = "red")
axes[0].set_title("axes 1")
axes[1].plot(x,x ** 0.5,color = "purple")
axes[1].set_title("axes 2")

plt.tight_layout()

fig.savefig("Figure 1.png")

fig = plt.figure(figsize = (6,4))
axes = fig.add_axes([0,0,1,1])

axes.plot(x,x ** 0.5,color = "red",label = "x karekök")
axes.plot(x,x ** 2,color = "yellow",label = "x kare")
axes.plot(x,x ** 3,color = "#4055c2",label = "x küp")

axes.legend()

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,x**2,color = "red",lw = 3,ls = "-.",marker = "o",ms = 20,mfc = "black",mec = "yellow",mew = 10)

axes.set_xlim(0,6)
axes.set_ylim(0,30)
