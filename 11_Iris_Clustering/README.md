
Issue 1 - sklearn.datasets

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
