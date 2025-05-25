import os
import numpy as np

def merge_and_save(filenames, out_path):
    all_data = []
    for fname in filenames:
        data = np.load(fname)
        print(f"[加载] {fname}, shape={data.shape}")
        all_data.append(data)
    merged = np.concatenate(all_data, axis=0)
    np.save(out_path, merged)
    print(f"→ 已保存合并数据到 {out_path}，shape={merged.shape}")

if __name__ == "__main__":
    base_dir = "merged_EC"       # 存放合并数据的目录
    out_dir = "final_dataset"    # 最终输出目录
    os.makedirs(out_dir, exist_ok=True)

    # 指定各组要合并的文件
    train_files = [
        os.path.join(base_dir, "H_S1~24_EC.npy"),
        os.path.join(base_dir, "MDD_S1~27_EC.npy")
    ]
    test_files = [
        os.path.join(base_dir, "H_S25~27_EC.npy"),
        os.path.join(base_dir, "MDD_S28~30_EC.npy")
    ]
    val_files = [
        os.path.join(base_dir, "H_S28~30_EC.npy"),
        os.path.join(base_dir, "MDD_S31~34_EC.npy")
    ]

    # 合并数据
    merge_and_save(train_files, os.path.join(out_dir, "MDDH_train_data.npy"))
    merge_and_save(test_files, os.path.join(out_dir, "MDDH_test_data.npy"))
    merge_and_save(val_files, os.path.join(out_dir, "MDDH_val_data.npy"))
