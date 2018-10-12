Issue 5 - sns.scatterplot() vs sns.FacetGrid().map().add_legend()

1. sns.FacetGrid
```python
sns.FacetGrid(test_df, hue='label',size=5).map(plt.scatter, 'petallength','petalwidth').add_legend()
sns.FacetGrid(pred_df, hue='label',size=5).map(plt.scatter, 'petallength','petalwidth').add_legend()
```


2. sns.scatterplot()
```python
fig = plt.figure(figsize=(16,6))
ax1 = fig.add_subplot(1,2,1)
ax1 = sns.scatterplot('petallength','petalwidth', hue='label', data=test_df, palette=plt.cm.plasma_r)
ax1.set_title('test_df')
ax2 = fig.add_subplot(1,2,2)
ax2 = sns.scatterplot('petallength','petalwidth', hue='label', data=pred_df, palette=plt.cm.plasma_r)
ax2.set_title('pred_df')
```

# Issue 4 - cmap, palette

```plt.scatter(cmap=)```

```sns.scatterplot(palette=)```


# Issue 3 - if...elif..else transfer to lambda expression

```python
 data_df['label'].apply(lambda x: 0 if x==2 else 1 if x==0 else 2)
```

# Issue 2 - plt.rcParams

```python
plt.rcParams['figure.figsize'] = (12, 8)      # 设置绘图图像大小
plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
# 设置figsize可以在不改变分辨率情况下改变比例
```


# Issue 1 - sklearn.datasets

```python
from sklearn.datasets import load_iris
```
```python
iris_data = load_iris().data
iris_label = load_iris().target
feature_names = [i.split()[0]+i.split()[1] for i in load_iris().feature_names]

data_df = pd.Dataframe(iris_data, columns = feature_names)
data_df['label'] = iris_label
```
