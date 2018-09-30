


# Issue 1 - 特征之间的相关性

1. ```sns.pairplot(data_df)```

2. ```pd.scatter_matrix(data_df, diagonal='kde', # default=hist,
                     figsize=(16,9),
                     range_padding=0.1)```
                     
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
