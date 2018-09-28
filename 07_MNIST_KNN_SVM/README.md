

# Issue 1 - pkl.gz

```python
import gzip
import pickle
```
```python
with gzip.open('../input/mnist.pkl.gz') as f:
    a = pickle.load(f, encoding='bytes') # or encoding='unicode-escape'
```

open ```.gz``` first and then load pickle.
