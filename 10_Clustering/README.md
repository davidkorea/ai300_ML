# 1. 肘部法则

```python
sum(np.min(cdist(X,km.cluster_centers_, metric='euclidean'), axis=1))/X.shape[0]
```

![](https://i.loli.net/2018/10/13/5bc1718dc6426.png)
