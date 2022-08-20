import matplotlib.pyplot as plt
import numpy as np

x = [3.8,3.9,3.8,4,4,4.7,4.8,4.8,5,5,5.6,5.7,5.7,5.9,6.1,6.5,6.6,6.7,6.9,7.2,7.6,7.6,7.6,8,8.5,10.6,9.7,9.4,10.2,12]
y = [1,3,5,7,9,1,3,5,7,9,1,3,5,7,9,1,3,5,7,9,1,3,5,7,9,1,3,5,7,9]
z = [1,1,1,1,1,1.5,1.5,1.5,1.5,1.5,2,2,2,2,2,2.5,2.5,2.5,2.5,2.5,3,3,3,3,3,4,4,4,4,4]
dv = [[],[],[],[],[],[]]#np.zeros(6)


d = [0,0,0,0,0]
x,y,z = np.array(x),np.array(y),np.array(z)
xs = x.reshape(6,5)
zs = z.reshape(6,5)
cp = plt.tricontourf(x, y, z)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parallel plane and Circle electrodes')
for i in range (1,len(xs)):
    for j in range(5):
        d.append((zs[i][j]-zs[i-1][j])/(xs[i][j]-xs[i-1][j]))
d =np.array(d)
plt.quiver(x,y,z,d)
plt.colorbar(cp)
plt.grid()
plt.show()