import librosa
import soundfile as sf
import numpy as np

def change_pitch_and_maintain_speed(original_file, orig_pitch, target_pitch, output_file):
    # 오디오 파일 로드
    y, sr = librosa.load(original_file, sr=None)

    # 피치 조정 계수 계산
    pitch_shift = 12 * np.log2(target_pitch / orig_pitch)

    # 피치 변경
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=pitch_shift)

    # 조정된 오디오 저장
    sf.write(output_file, y_shifted, sr)

# 파일 경로와 피치 지정
original_file = './audio/output/vocals.wav'
output_file = './audio/output/adjusted_vocals.wav'
orig_pitch = 621.78656  # 원본 파일의 피치
target_pitch = 446.15906  # 조정하고자 하는 피치

# 피치 조정 함수 호출
change_pitch_and_maintain_speed(original_file, orig_pitch, target_pitch, output_file)
