def Mr_Spleet():
    from spleeter.separator import Separator
    from spleeter.audio.adapter import AudioAdapter
    import os

    def spleet_file(audio_adapter, separator, file_path, base_output_directory):
        waveform, rate = audio_adapter.load(file_path)
        prediction = separator.separate(waveform)
        
        # 각 트랙 별로 저장할 디렉토리 설정
        output_directories = {
            'vocals': os.path.join(base_output_directory, 'vocal'),
            'accompaniment': os.path.join(base_output_directory, 'mr')
        }

        # 필요한 경우 디렉토리 생성
        for dir in output_directories.values():
            if not os.path.exists(dir):
                os.makedirs(dir)

        for key in ['vocals', 'accompaniment']:
            if key in prediction:
                value = prediction[key]
                output_path = os.path.join(output_directories[key], os.path.splitext(os.path.basename(file_path))[0] + f"_{key}.wav")
                audio_adapter.save(output_path, value, rate, 'wav')

    audio_adapter = AudioAdapter.default()
    separator = Separator('spleeter:2stems')

    input_directory = './audio/infer_file_wav'
    base_output_directory = './audio/infer_file_spleet'

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if os.path.isfile(file_path):
            spleet_file(audio_adapter, separator, file_path, base_output_directory)
