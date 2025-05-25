import os
import numpy as np

def generate_labels(data_path, label_path, label_value):
    data = np.load(data_path)
    num_samples = data.shape[0]
    labels = np.full((num_samples,), fill_value=label_value, dtype=np.int64)
    np.save(label_path, labels)
    print(f"→ 标签已保存：{label_path}，标签值={label_value}，数量={num_samples}")

if __name__ == "__main__":
    # 合并后的数据目录
    data_dir = "merged_EC"

    for fname in os.listdir(data_dir):
        if fname.endswith(".npy") and not fname.endswith("_label.npy"):
            data_path = os.path.join(data_dir, fname)
            label_path = os.path.join(data_dir, fname.replace(".npy", "_label.npy"))

            if fname.startswith("H_"):
                label_value = 0
            elif fname.startswith("MDD_"):
                label_value = 1
            else:
                print(f"[跳过] 无法识别标签类别：{fname}")
                continue

            generate_labels(data_path, label_path, label_value)

    print("✅ 所有标签已生成完毕！")
