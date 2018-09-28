import numpy as np
import gzip
import pickle
import matplotlib.pyplot as plt

def plot_boundary(X, y, clf, h=.02):
    #参数解释：
    #X, y：数据的坐标（二维）和label
    #h: 网格间距

    unique_lables = set(y)

    # 选择绘制颜色
    colors = plt.cm.Spectral(np.linspace(0,1, len(unique_lables)))

    #绘制网格 [x_min, x_max]x[y_min, y_max]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    #得到每个网格点的分类
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 绘制网格点图
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)

    # 绘制训练集X
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral,
                edgecolor='k', s=80)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.show()
    return True

def load_data(filepath = r'../dataset/mnist.pkl.gz'):
    # 导入手写数字识别数据
    with gzip.open(filepath) as fp:
        training_data, valid_data, test_data = pickle.load(fp, encoding='unicode-escape')
    return training_data, valid_data, test_data

def create_data(train_data, valid_data, test_data, train_num=8000,
                valid_num=1000, test_num=1000, random_state=300):

    # 原数据集过大，随机抽取一部分
    np.random.seed(random_state)
    train_index = np.random.choice(len(train_data[1]), train_num)
    valid_index = np.random.choice(len(valid_data[1]), valid_num)
    test_index = np.random.choice(len(test_data[1]), test_num)

    x_train = train_data[0]
    y_train = train_data[1]

    x_valid = valid_data[0]
    y_valid = valid_data[1]

    x_test = test_data[0]
    y_test = test_data[1]

    x_train = x_train[train_index]
    y_train = y_train[train_index]

    x_valid = x_valid[valid_index]
    y_valid = y_valid[valid_index]

    x_test = x_test[test_index]
    y_test = y_test[test_index]

    return x_train, y_train, x_valid, y_valid, x_test, y_test
