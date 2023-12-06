def Pitch_Control(orig_pitch, target_pitch):
    import librosa
    import soundfile as sf
    import numpy as np
    import os

    def change_pitch_and_save(file_path, output_directory, orig_pitch, target_pitch):
        y, sr = librosa.load(file_path, sr=None)
        pitch_shift = 12 * np.log2(target_pitch / orig_pitch)
        y_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=pitch_shift)


        output_file_path = os.path.join(output_directory, os.path.basename(file_path))
        sf.write(output_file_path, y_shifted, sr)

    def process_directory(input_directory, output_directory):
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for filename in os.listdir(input_directory):
            if filename.endswith('.wav'):
                file_path = os.path.join(input_directory, filename)
                change_pitch_and_save(file_path, output_directory, orig_pitch, target_pitch)

    # MR과 보컬 파일 경로
    mr_directory = './audio/infer_file_spleet/mr'
    vocal_directory = './audio/infer_file_spleet/vocal'
    
    # 출력 디렉토리
    output_mr_directory = './audio/pitch_change/mr'
    output_vocal_directory = './audio/pitch_change/vocal'

    # MR과 보컬 파일에 대해 피치 조정
    process_directory(mr_directory, output_mr_directory)
    process_directory(vocal_directory, output_vocal_directory)
