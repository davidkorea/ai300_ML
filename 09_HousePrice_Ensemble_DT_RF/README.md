


# Issue 1 - 特征之间的相关性

1. sns.pairplot
```python
sns.pairplot(data_df)
```
![](https://user-images.githubusercontent.com/26485327/46256227-b8fc5e00-c4e2-11e8-9a3f-3ae86a0791c0.png)

2. pd.scatter_matrix
```python
pd.scatter_matrix(data_df, diagonal='kde', # default=hist,
                     figsize=(16,9),
                     range_padding=0.1)
```
                     
3. sns.jointplot
```python
for i in cols[2:]:
    for j in cols[2:]:
        if i!=j:
            sns.jointplot(x=i,y=j,data=data_df)
            plt.title('i - j jointplot'.format(i,j))
            plt.tight_layout()
            plt.show()
```
4. sns.heatmap
```python
data_df_corr = data_df.corr()
sns.heatmap(data_df_corr, annot=True, cmap='coolwarm')
```
Reference
1. [Mobile App Analysis.ipynb](https://github.com/davidkorea/DATA_ANALYSIS/blob/master/8_Mobile_Apps_Analysis_Kaggle/Mobile%20App%20Analysis.ipynb)
2. [8_分析神奇宝贝的变量关系数据.ipynb](https://github.com/davidkorea/DATA_ANALYSIS/blob/master/4_pokemon_properties/8_%E5%88%86%E6%9E%90%E7%A5%9E%E5%A5%87%E5%AE%9D%E8%B4%9D%E7%9A%84%E5%8F%98%E9%87%8F%E5%85%B3%E7%B3%BB%E6%95%B0%E6%8D%AE.ipynb)
