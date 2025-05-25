## 数据集制作流程


数据格式（样本数量，通道数，步长），10s取样一次，label：（样本数量，）；0：健康；1：MDD

#### 使用的预处理技术：

带通滤波，除去1~40hz；

通道z-score标准化；




## 使用流程

1. **数据合并:**
   已处理了一些数据：分别放在：

   H_S1~24_EC，

   H_S25~27_EC，

   H_S28~30_EC，

   MDD_S1~27_EC，

   MDD_S28~30_EC，

   MDD_S31~34_EC里面，

   需要给各个目录下的所有样本合并输出一个整合版的npy数组

   （如H_S1~24_EC下的所有文件合并为H_S1~24_EC.npy,H_S28~30_EC合并为H_S28~30_EC.npy），输出到一个新的文件夹里面

   运行datahug.py

   

   

2. **制作标签:**
   给这些文件打标签，每一份都生成一个新的npy数组，如：H_S1~24_EC.npy生成一个H_S1~24_EC_label.npy,数组；数组类型为Dtype = int64 Shape = (样本总数,)，

   H_开头的文件一律为0，_

   _MDD_~开头的文件一律为1 

   运行labelmaker.py

   **合并文件:**

   依次运行：TTV_DATA.py; TTV_DATA_LABEL.py;  all_data_collect.py

   


