import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

X= []
def Lorenz(s, p, b, x, y, z, N, dt):

	for i in range(N):
		x = x + (s*(y-x))*dt
		y = y + (x*(p-z)-y)*dt
		z = z + (x*y - b*z)*dt

		X.append([x,y,z])

# common parameters
Lorenz(10, 28, 8/3, 1, 1, 1, 5000, 0.01)



x=[]
y=[]
z=[]
for i in X:
	print(i)
	x.append(i[0])
	y.append(i[1])
	z.append(i[2])


fig = plt.figure()
ax = plt.axes(projection='3d')


ax.plot3D(x, y, z, linewidth=0.5);
# ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);

plt.show()
