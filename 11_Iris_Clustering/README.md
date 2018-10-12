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
