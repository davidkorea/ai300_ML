
# Issue 3 - validation_curve
```python
from sklearn.model_selection import validation_curve

validation_curve(estimator, X, y, param_name, param_range, cv=5)
```
```python
k_list = [1, 5, 10, 20, 50]
train_scores, valid_scores = validation_curve(KNeighborsClassifier(), valid_sample, valid_label, 
                            'n_neighbors', k_list, cv=5)
>> train_scores
array([[1.        , 1.        , 1.        , 1.        , 1.        ],
       [0.93207547, 0.91864831, 0.9025    , 0.92384519, 0.90807453],
       [0.89937107, 0.88485607, 0.88625   , 0.89013733, 0.88944099],
       [0.87169811, 0.85106383, 0.86      , 0.85642946, 0.85962733],
       [0.79119497, 0.75093867, 0.7875    , 0.78651685, 0.78012422]])

>> valid_scores
array([[0.86829268, 0.91044776, 0.9       , 0.84924623, 0.9025641 ],
       [0.82926829, 0.88557214, 0.91      , 0.85427136, 0.88205128],
       [0.83414634, 0.89552239, 0.89      , 0.84422111, 0.9025641 ],
       [0.80487805, 0.88557214, 0.815     , 0.8241206 , 0.89230769],
       [0.70243902, 0.82587065, 0.755     , 0.75879397, 0.77948718]])

```



# Issue 2 - Select samples randomly

```python
np.random.seed(0)
train_idx = np.random.choice(len(train_data[0]), 3)
print(train_idx)
train_sample = train_data[0][train_idx]
train_label = train_data[1][train_idx]
print(train_sample)
print(train_label)
for i,v in enumerate(train_sample):
    plot(v, train_label[i])
    
>>
[ 2732 43567 42613]
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[4 1 7]
```
```python
import matplotlib.pyplot as plt
def plot(arr_784, label):
    arr_28 = arr_784.reshape(-1,28)
    plt.imshow(arr_28, cmap=plt.cm.Greys)
    plt.title(label)
    plt.show()
```
![4](https://user-images.githubusercontent.com/26485327/46191624-2ec1c780-c333-11e8-98e7-f60127529c92.png)

![1](https://user-images.githubusercontent.com/26485327/46191622-2d909a80-c333-11e8-807d-1bf0c2334cea.png)

![7](https://user-images.githubusercontent.com/26485327/46191629-2ff2f480-c333-11e8-88f3-7752f2ccd264.png)


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
>>
print('Unzip pickle dataset len: %s, type: %s ' %(len(a), type(a)))
for idx,value in enumerate(a):
    print('in tuple[%s]:\n len=%s (data + label), \n\n data: len(data)=%s \n %s, \n each data row len=%s,\n\n label:\n %s' %
          (idx,len(value),len(value[0]),value[0], len(value[0][0]),value[1]))
    print('-----'*10)
    
>>
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
**pickle.load() returns 3 results(tuples), each tuple has features ndarray & labels array**

**so we need to pass them to 3 paras: ```train_data, valid_data, test_data```. train_data[0]=features, train_data[1]=labels**

```python
with gzip.open('../input/mnist.pkl.gz') as f:
    train_data, valid_data, test_data = pickle.load(f, encoding='bytes')
```



