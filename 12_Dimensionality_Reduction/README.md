 # 5. Elasticsearch(Apache Lucene)全文搜索
 
 # 4. 存储选择
 
 1. 硬件选择
- 一次内存随机读取， 几十纳秒
  - 几个TB的数据，内存成本代价极高
- 一次SSD硬盘随机读取， 几十微妙
- 一次SATA机械硬盘随机读取， 几十毫秒
  - SSD的性能比SATA高出三个数量级， 价格只高出一倍
 
 2. SQL or NoSQL
 
 - 传统关系型SQL数据库（RDBMS），对于机构化，非稀疏性数据的存储非常成熟稳定
 - NoSQL的众多组建适合用户画像存储
   - 像日志一样顺序追加写入，保证系统极高的写入吞吐量
   - HBase, Riak, Tair, LSM-Tree(Log-strcutured Merge Tree)


# 3. Model
- XGBoost梯度提升树, GBDT
- FM/FFM

# 2. Hadoop生态

- 海量存储
  - HDFS, HBase, MongoDB, RocksDB
- 离线批量计算
  - MapReduce, Hive, Spark
- 实时计算框架
  - Storm, Spark-Streaming, Flink
  
# 1. 数据埋点

[数据埋点(浅谈埋点方式与上报收集)](https://www.jianshu.com/p/58063f964820)
