# High-Performance-Batch-Silence-Remover-for-Audio-Datasets
这是一个专为大规模音频数据集清洗设计的高效 Python 脚本。它能够递归扫描指定目录下的所有 .wav 文件，利用 librosa 的智能算法自动检测并切除首尾的静音部分，同时保留核心的演奏/语音内容。
# 🎵 批量音频静音裁剪工具 (Batch Silence Trimmer)

一个高效、优化的 Python 脚本，用于批量移除 `data/raw` 目录下所有 `.wav` 音频文件首尾的静音部分。

该脚本专为大规模数据处理设计，通过结合 `soundfile` 的快速读取能力和 `librosa` 的智能静音检测算法，在保证音质的同时显著提升了处理速度，并带有实时进度条显示。

## ✨ 主要特点

- **🚀 极速处理**：使用 `soundfile` 直接读取音频数据，避免了 `librosa` 默认的重采样开销，处理速度提升明显。
- **📊 实时进度**：集成 `tqdm` 库，清晰展示当前处理进度、速度和预计剩余时间。
- **🎯 智能裁剪**：基于能量阈值（默认 30dB）自动精准识别并切除首尾静音。
- **🔄 自动适配**：自动检测并将立体声音频转换为单声道，确保后续处理的一致性。
- **💾 原地优化**：处理完成后直接覆盖原文件，无需额外存储空间（*运行前请务必备份*）。

## 📋 环境依赖

在运行脚本之前，请确保你的环境中已安装以下 Python 库：

    pip install tqdm soundfile librosa

> **💡 系统依赖提示**：
> `soundfile` 库依赖底层的 `libsndfile`。如果安装报错，请先安装系统级依赖：
> - **Ubuntu/Debian**: `sudo apt-get install libsndfile1`
> - **macOS**: `brew install libsndfile`
> - **Windows**: 通常 `pip` 会自动处理，若失败请尝试安装 `Microsoft Visual C++ Redistributable`。

## 🚀 快速开始

### 1. 目录结构准备
确保你的项目结构如下，所有待处理的 `.wav` 文件需放置在 `data/raw` 文件夹内（支持子文件夹递归查找）：

    your_project/
    ├── trim_silence_all_fast.py   # 本脚本文件
    └── data/
        └── raw/
            ├── audio_001.wav
            ├── audio_002.wav
            └── sub_folder/
                └── audio_003.wav

### 2. 运行脚本
在终端进入项目根目录，执行以下命令：

    python trim_silence_all_fast.py

脚本将自动：
1. 扫描 `data/raw` 下所有 `.wav` 文件。
2. 逐个读取、转换单声道、裁剪静音。
3. 覆盖保存处理后的文件。
4. 显示完成提示。

> ⏱️ **预计耗时**：根据文件数量和大小，通常需要 3~8 分钟。

## ⚙️ 参数配置

如果你需要调整静音检测的灵敏度，可以直接编辑 `.py` 文件中的 `top_db` 参数：

    y_trimmed = trim_silence(y, top_db=30)

- **更严格**（切除更多背景噪点）：设置为 `20` ~ `25`
- **更宽松**（保留更多微弱声音）：设置为 `35` ~ `40`

## ⚠️ 注意事项

1. **数据备份**：本脚本采用**覆盖模式**运行，会直接修改原始文件。在生产环境使用前，**强烈建议备份** `data/raw` 目录。
2. **文件格式**：目前仅支持 `.wav` 格式文件。
3. **空文件保护**：脚本包含安全检查，如果裁剪后音频为空，将跳过写入以防止文件损坏。

## 📄 许可证

本项目仅供学习和数据处理交流使用。
