def Train_File_To_Wav():
    import os
    from pydub import AudioSegment
    
    def convert_to_wav(input_directory, output_directory):
        # 출력 디렉토리가 없으면 생성
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
    
        for filename in os.listdir(input_directory):
            if not filename.endswith(".wav"):
                input_file_path = os.path.join(input_directory, filename)
                # 파일 확장자 추출
                file_extension = os.path.splitext(filename)[1][1:]
    
                try:
                    # 오디오 파일 로드
                    audio = AudioSegment.from_file(input_file_path, format=file_extension)
                    # wav 파일로 저장
                    output_file_path = os.path.join(output_directory, os.path.splitext(filename)[0] + ".wav")
                    audio.export(output_file_path, format="wav")
                    print(f"{input_file_path}를 {output_file_path}로 변환 완료")
                except Exception as e:
                    print(f"변환 실패: {input_file_path}, 오류: {e}")
    
    # 원본 및 출력 디렉토리 경로
    input_directory = "./audio/train_file"
    output_directory = "./audio/train_file_wav"
    
    # 변환 실행
    convert_to_wav(input_directory, output_directory)