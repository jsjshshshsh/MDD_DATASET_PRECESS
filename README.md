# 用于抑郁症患者的数据集预处理说明

## 目前使用：6通道，window_size_sec=5, overlap=0.5，只生成了EC（eye open）作为示例

1. **读取EDF部分:**  
```bash
运行 mdd_with_giter.py
```

2. **读取后把数据集整合，打标签，分类封装:**  
```bash
示例目录：EC
按以下顺序运行
整合：datahug.py
输出路径：merged_EC
标签：labelmaker.py
输出路径：merged_EC
合并文件:TTV_DATA.py(合并data生成all); TTV_DATA_LABEL.py(合并label生成all); 
输出路径：final_dataset
最终合并：all_data_collect.py(最终文件以字典的形式打包为一个文件)
输出路径：final_dataset
//原本生成的数据迁移到FINALFINAL里了


```


## 补充说明

1. #### 使用的预处理技术：

  带通滤波，除去1~40hz；

  通道z-score标准化；

2. **数据:**
    一开始已处理的一些数据，分别放在：
    
    **train_data:**

  H_S1~24_EC

  MDD_S1~27_EC

​     **test_data :**

  H_S25~27_EC

  MDD_S28~30_EC

​      **val_data:**

  H_S28~30_EC

  MDD_S31~34_EC

**上述数据严格按受试者分类用于跨被试实验**





3. **数据类型**

  label:Dtype = int64    Shape = (样本总数,)

  data:Dtype = float32 Shape = (样本总数，通道数，步长)

  0：健康；1：MDD

## 最终输出标准

**先输出的npy类型:**  

![类型标准](11.png)

**上述标准tips:**

如果不能跑通就把‘MDDH_’全部删掉，如：变成All_train_data

**最终给ai的是一个文件，请用all_data_collect.py打包**

