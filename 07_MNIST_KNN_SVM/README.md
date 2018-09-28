

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

```python
>>a

>>
((array([[0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         ...,
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.]], dtype=float32),
  array([5, 0, 4, ..., 8, 4, 8])),
 (array([[0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         ...,
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.]], dtype=float32),
  array([3, 8, 6, ..., 5, 6, 8])),
 (array([[0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         ...,
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.],
         [0., 0., 0., ..., 0., 0., 0.]], dtype=float32),
  array([7, 2, 1, ..., 4, 5, 6])))
```

```python
print('Unzip pickle dataset len: %s, type: %s ' %(len(a), type(a)))
for idx,value in enumerate(a):
    print('in tuple[%s]:\n len=%s (data + label), \n\n data: len(data)=%s \n %s, \n each data row len=%s,\n\n label:\n %s' %
          (idx,len(value),len(value[0]),value[0], len(value[0][0]),value[1]))
    print('-----'*10)
    

Unzip pickle dataset len: 3, type: <class 'tuple'> 
in tuple[0]:
 len=2 (data + label), 

 data: len(data)=50000 
 [[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]], 
 each data row len=784,

 label:
 [5 0 4 ... 8 4 8]
--------------------------------------------------
in tuple[1]:
 len=2 (data + label), 

 data: len(data)=10000 
 [[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]], 
 each data row len=784,

 label:
 [3 8 6 ... 5 6 8]
--------------------------------------------------
in tuple[2]:
 len=2 (data + label), 

 data: len(data)=10000 
 [[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]], 
 each data row len=784,

 label:
 [7 2 1 ... 4 5 6]
--------------------------------------------------
```
