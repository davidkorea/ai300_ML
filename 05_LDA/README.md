> [https://www.kaggle.com/davidkor/ai300-lda](https://www.kaggle.com/davidkor/ai300-lda)

# Issue 1 - plt_subplot

1. Option1

```python
fig = plt.figure(figsize=(16,6))
ax1 = fig.add_subplot(1,2,1)
ax1.scatter(X_lda[:,0], X_lda[:,1], c=y, cmap=plt.cm.viridis_r)
ax1.set_title('good')
ax2 = fig.add_subplot(1,2,2)
ax2.scatter(X_lda[:,0], X_lda[:,1])
ax2.set_title('bad')
```
![](https://user-images.githubusercontent.com/26485327/46123449-8855c380-c259-11e8-8679-81b704ac977a.png)

2. Option2 

```python
fig, ax = plt.subplots(1,2)
ax[0].scatter(X_pca[:,0], X_pca[:,1], c=y)
ax[1].scatter(X_pca[:,0], X_pca[:,1])
```
![](https://user-images.githubusercontent.com/26485327/46123454-8e4ba480-c259-11e8-8d87-572e5ed5a855.png)

# Issue 2 - Axes3D

```python
from mpl_toolkits.mplot3d import Axes3D
```

```python
fig = plt.figure()
ax = Axes3D(fig, rect=[0,0,1,1], elev=30, azim=20)
plt.scatter(X[:,0], X[:,1], X[:,2], marker='o')
```
![](https://user-images.githubusercontent.com/26485327/46123367-006fb980-c259-11e8-8a24-fe442c0d2558.png)

# Issue 3 - Generate dataset

```python
from sklearn.datasets.samples_generator import make_classification
```
```python
X,y = make_classification(n_samples=1000, n_features=3, n_redundant=0, 
                          n_classes=3, n_informative=2, n_clusters_per_class=1, 
                          class_sep=0.5, random_state=10)
```
