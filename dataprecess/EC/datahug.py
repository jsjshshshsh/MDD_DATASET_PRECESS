import os
import numpy as np

def merge_npy_files(input_dir, output_file):
    all_data = []

    for fname in os.listdir(input_dir):
        if fname.endswith(".npy"):
            fpath = os.path.join(input_dir, fname)
            data = np.load(fpath)
            all_data.append(data)
            print(f"→ 加载 {fname}, shape = {data.shape}")

    # 合并所有样本维度（第0维）
    merged = np.concatenate(all_data, axis=0)
    np.save(output_file, merged)
    print(f"✅ 合并完成：{output_file}, 总 shape = {merged.shape}")

if __name__ == "__main__":
    # 输入目录列表
    input_dirs = [
        "H_S1~24_EC",
        "H_S25~27_EC",
        "H_S28~30_EC",
        "MDD_S1~27_EC",
        "MDD_S28~30_EC",
        "MDD_S31~34_EC"
    ]

    # 输出目录
    output_root = "merged_EC"
    os.makedirs(output_root, exist_ok=True)

    for folder in input_dirs:
        input_path = folder
        output_path = os.path.join(output_root, folder + ".npy")
        merge_npy_files(input_path, output_path)

    print("🎉 所有目录合并完成！")
