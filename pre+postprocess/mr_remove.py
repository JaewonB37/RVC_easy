def Mr_Remove():
    from spleeter.separator import Separator
    from spleeter.audio.adapter import AudioAdapter
    import os
    
    def spleet_vocals_only(audio_adapter, separator, file_path, output_directory):
        # 오디오 파일 로드
        waveform, rate = audio_adapter.load(file_path)
    
        # 오디오 분리
        prediction = separator.separate(waveform)
    
        # 분리된 보컬 트랙만 저장
        vocals = prediction.get('vocals')
        if vocals is not None:
            output_path = os.path.join(output_directory, os.path.splitext(os.path.basename(file_path))[0] + "_vocals.wav")
            audio_adapter.save(output_path, vocals, rate, 'wav')
            print(f"보컬 트랙 저장됨: {output_path}")
    
    def main():
        audio_adapter = AudioAdapter.default()
        separator = Separator('spleeter:2stems')
    
        input_directory = './audio/train_file_wav'
        output_directory = './audio/train_file_removemr'
    
        # 출력 디렉토리 확인 및 생성
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    
        # 입력 디렉토리의 모든 파일에 대해 보컬만 spleet 실행
        for filename in os.listdir(input_directory):
            file_path = os.path.join(input_directory, filename)
            if os.path.isfile(file_path):
                spleet_vocals_only(audio_adapter, separator, file_path, output_directory)
    
    if __name__ == '__main__':
        main()