import os
import mne
import numpy as np
from sklearn.preprocessing import StandardScaler

def edf_to_numpy(file_path, selected_channels, window_size_sec=5, overlap=0.5):
    """
    将 EDF 文件转换为 NumPy 数组，包含预处理步骤。
    返回 shape 为 (样本数, 通道数, 步长) 的数组。
    """
    raw = mne.io.read_raw_edf(file_path, preload=True)
    raw.pick_channels(selected_channels)
    #带通滤波变换
    raw.filter(1, 40, fir_design='firwin')

    data = raw.get_data()
    sfreq = raw.info['sfreq']
    window_size = int(window_size_sec * sfreq)
    step_size = int(window_size * (1 - overlap))
    n_channels, n_samples = data.shape
    n_segments = (n_samples - window_size) // step_size + 1

    segments = np.zeros((n_segments, n_channels, window_size))
    for i in range(n_segments):
        start = i * step_size
        end = start + window_size
        segments[i] = data[:, start:end]

    # 每个通道做 Z-score 标准化
    scaler = StandardScaler()
    segments = np.array([scaler.fit_transform(seg.T).T for seg in segments])
    return segments

if __name__ == "__main__":
    # 输入文件所在的文件夹
    in_dir = "emotion"

    # 输出目录
    #####################################
    out_dir = "MDD_S31~34_EO"
    ####################################


    os.makedirs(out_dir, exist_ok=True)



    # 要选的前额叶通道
    #由于MDD数据集里的通道命名方式不同需要改
    ##################################
    selected_channels = [
        'EEG Fp1-LE', 'EEG Fp2-LE',
        'EEG F3-LE',  'EEG F4-LE',
        'EEG F7-LE',  'EEG F8-LE'
    ]
    ####################################






########################################################
    # 批量处理 H S1 EC 到 H S27 EC，如果换成其他文件的可以改
    for idx in range(31, 35):
        # 构造文件名，比如 "H S1 EC.edf"
        fname = f"MDD S{idx} EO.edf"
        #########################################





        fpath = os.path.join(in_dir, fname)
        if not os.path.isfile(fpath):
            print(f"[跳过] 未找到文件：{fpath}")
            continue

        print(f"[处理] {fpath}")
        segments = edf_to_numpy(fpath, selected_channels,
                                window_size_sec=5, overlap=0.5)###这里修改步长



        # 保存为 .npy，文件名如 "H_S1_EC.npy"
        ##################################
        out_name = f"MDD_S{idx}_EO.npy"
        ####################################




        out_path = os.path.join(out_dir, out_name)
        np.save(out_path, segments)
        print(f"→ 已保存 {out_path}，shape = {segments.shape}")

    print("全部处理完成！")
