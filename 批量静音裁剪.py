# 安装进度条工具（只需一次）
pip install tqdm

# 创建优化版静音裁剪脚本
cat > trim_silence_all_fast.py << 'EOF'
import soundfile as sf
from pathlib import Path
from tqdm import tqdm
import librosa

def trim_silence(audio, top_db=30):
    return librosa.effects.trim(audio, top_db=top_db)[0]

raw_path = Path("data/raw")
wav_files = list(raw_path.rglob("*.wav"))

print(f"🔍 找到 {len(wav_files)} 个音频，开始静音裁剪...")

for wav_file in tqdm(wav_files, desc="Trimming"):
    # 用 soundfile 直接读取，避免 librosa 重采样开销
    y, sr = sf.read(str(wav_file))
    
    # 转单声道（如为立体声）
    if y.ndim > 1:
        y = y.mean(axis=1)
    
    # 裁剪静音
    y_trimmed = trim_silence(y, top_db=30)
    
    # 安全写回（覆盖原文件）
    sf.write(str(wav_file), y_trimmed, sr)

print("✅ 静音裁剪完成！")
EOF

# 运行（预计 3~8 分钟）
python trim_silence_all_fast.py
