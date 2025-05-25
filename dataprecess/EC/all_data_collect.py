import os
import numpy as np

def merge_npy_files(file_list, out_path):
    all_data = []
    for f in file_list:
        arr = np.load(f)
        print(f"[加载] {f}, shape={arr.shape}")
        all_data.append(arr)
    merged = np.concatenate(all_data, axis=0)
    np.save(out_path, merged)
    print(f"→ 已保存 {out_path}, shape={merged.shape}")

if __name__ == "__main__":
    base_dir = "final_dataset"

    # 要合并的文件路径
    data_files = [
        os.path.join(base_dir, "MDDH_train_data.npy"),
        os.path.join(base_dir, "MDDH_test_data.npy"),
        os.path.join(base_dir, "MDDH_val_data.npy")
    ]

    label_files = [
        os.path.join(base_dir, "MDDH_train_label.npy"),
        os.path.join(base_dir, "MDDH_test_label.npy"),
        os.path.join(base_dir, "MDDH_val_label.npy")
    ]

    # 合并并保存
    merge_npy_files(data_files, os.path.join(base_dir, "MDDH_All_train_data.npy"))
    merge_npy_files(label_files, os.path.join(base_dir, "MDDH_All_train_label.npy"))
