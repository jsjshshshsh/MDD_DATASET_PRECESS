import mne
import numpy as np


def edf_to_numpy(file_path, selected_channels, window_size_sec=10, overlap=0.5):
    # 读取EDF文件
    raw = mne.io.read_raw_edf(file_path, preload=True)

    # 选择指定的通道
    raw.pick(selected_channels)

    # 获取数据和采样率
    data = raw.get_data()
    sfreq = raw.info['sfreq']

    # 计算窗口大小和步长
    window_size = int(window_size_sec * sfreq)
    step_size = int(window_size * (1 - overlap))
    n_channels, n_samples = data.shape
    n_segments = (n_samples - window_size) // step_size + 1

    # 初始化结果数组
    segments = np.zeros((n_segments, n_channels, window_size))

    # 分段
    for i in range(n_segments):
        start = i * step_size
        end = start + window_size
        segments[i] = data[:, start:end]

    return segments
file_path = 'emotion/H S1 EC.edf'
selected_channels = ['EEG Fp1-LE', 'EEG Fp2-LE', 'EEG F3-LE', 'EEG F4-LE', 'EEG F7-LE', 'EEG F8-LE']

segments = edf_to_numpy(file_path, selected_channels, window_size_sec=5, overlap=0.5)
print(segments.shape)  # 输出形状为 (样本数, 6, 步长)



