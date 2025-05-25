import os
import numpy as np

# 指定目标文件夹
in_dir = 'final_dataset'
# 保存文件名
out_file = 'MDD2.npy'

# 初始化字典
all_data = {}

# 遍历目录下的所有 .npy 文件
for fname in os.listdir(in_dir):
    if fname.endswith('.npy'):
        key = fname.replace('.npy', '')  # 去掉后缀作为字典的键
        ke = key.replace('MDDH_','')
        path = os.path.join(in_dir, fname)
        print(f"[读取] {fname}")
        all_data[ke] = np.load(path, allow_pickle=True)

# 保存成 .npy 文件（字典形式）
np.save(out_file, all_data)
print(f"\n✅ 所有数据已打包保存为 {out_file}")
