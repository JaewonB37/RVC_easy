def Mr_Combine():
    from pydub import AudioSegment
    
    def combine_tracks(vocals_path, accompaniment_path, output_path):
        # 보컬과 MR 트랙 로드
        vocals = AudioSegment.from_file(vocals_path)
        accompaniment = AudioSegment.from_file(accompaniment_path)
    
        # 오디오 트랙 합치기
        combined = vocals.overlay(accompaniment)
    
        # 결과 저장
        combined.export(output_path, format='wav')
    
    # 파일 경로 설정
    vocals_path = 'path/to/vocals.wav'
    accompaniment_path = 'path/to/accompaniment.wav'
    output_path = 'path/to/output/combined.wav'
    
    # 트랙 합치기
    combine_tracks(vocals_path, accompaniment_path, output_path)