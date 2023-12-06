def Pitch_Extraction():
    import librosa
    import numpy as np
    import os

    def extract_pitch(filename):
        y, sr = librosa.load(filename, sr=None)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch = [pitches[magnitudes[:, t].argmax(), t] for t in range(pitches.shape[1]) if magnitudes[:, t].max() > 0]
        return np.mean(pitch) if pitch else 0

    def calculate_average_pitch(directory):
        pitches = [extract_pitch(os.path.join(directory, f)) for f in os.listdir(directory) if f.endswith('.wav')]
        return np.mean([p for p in pitches if p > 0])

    # 추론할 파일과 학습할 파일의 디렉터리 경로
    infer_directory = './audio/infer_file_spleet/vocal'
    train_directory = './audio/train_file_wav'

    # 평균 피치 계산
    average_pitch_infer = calculate_average_pitch(infer_directory)
    average_pitch_train = calculate_average_pitch(train_directory)

    print(f"추론할 파일의 평균 피치: {average_pitch_infer}")
    print(f"학습할 파일의 평균 피치: {average_pitch_train}")

    return average_pitch_infer, average_pitch_train
