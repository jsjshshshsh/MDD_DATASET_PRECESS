import os
import numpy as np

def merge_labels_and_save(label_files, out_path):
    all_labels = []
    for fname in label_files:
        labels = np.load(fname)
        print(f"[加载标签] {fname}, shape={labels.shape}")
        all_labels.append(labels)
    merged_labels = np.concatenate(all_labels, axis=0)
    np.save(out_path, merged_labels)
    print(f"→ 已保存标签到 {out_path}，shape={merged_labels.shape}")

if __name__ == "__main__":
    base_dir = "merged_EC"       # 存放合并后的 .npy 数据及标签的文件夹
    out_dir = "final_dataset"    # 最终输出目录，和数据保存到一起
    os.makedirs(out_dir, exist_ok=True)

    # 各组标签文件
    train_label_files = [
        os.path.join(base_dir, "H_S1~24_EC_label.npy"),
        os.path.join(base_dir, "MDD_S1~27_EC_label.npy")
    ]
    test_label_files = [
        os.path.join(base_dir, "H_S25~27_EC_label.npy"),
        os.path.join(base_dir, "MDD_S28~30_EC_label.npy")
    ]
    val_label_files = [
        os.path.join(base_dir, "H_S28~30_EC_label.npy"),
        os.path.join(base_dir, "MDD_S31~34_EC_label.npy")
    ]

    # 合并标签
    merge_labels_and_save(train_label_files, os.path.join(out_dir, "MDDH_train_label.npy"))
    merge_labels_and_save(test_label_files, os.path.join(out_dir, "MDDH_test_label.npy"))
    merge_labels_and_save(val_label_files, os.path.join(out_dir, "MDDH_val_label.npy"))
