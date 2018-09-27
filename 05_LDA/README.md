
# Issue 1 - plt_subplot

## Option1

```python

```

## Option2 

```pytgon

```


# Issue 2 - Axes3D

```python
from mpl_toolkits.mplot3d import Axes3D
```
```python
fig = plt.figure()
ax = Axes3D(fig, rect=[0,0,1,1], elev=30, azim=20)
plt.scatter(X[:,0], X[:,1], X[:,2], marker='o')
```
