# import os
# from pydub import AudioSegment

# def convert_m4a_to_wav(input_path, output_path):
#     # m4a 파일 로드
#     audio = AudioSegment.from_file(input_path, format="mp4")

#     # wav 파일로 저장
#     audio.export(output_path, format="wav")
#     print(f"{input_path}를 {output_path}로 변환 완료")

# # 주어진 파일에 대한 변환 예시
# input_file_path = r"C:\Users\qowod\s1.mp4"
# output_file_path = r"C:\Users\qowod\s1.wav"
# convert_m4a_to_wav(input_file_path, output_file_path)


import os
from pydub import AudioSegment

def convert_to_wav(directory):
    for filename in os.listdir(directory):
        if not filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            # 파일 확장자 추출
            file_extension = os.path.splitext(filename)[1][1:]

            try:
                # 오디오 파일 로드
                audio = AudioSegment.from_file(file_path, format=file_extension)
                # wav 파일로 저장
                output_path = os.path.splitext(file_path)[0] + ".wav"
                audio.export(output_path, format="wav")
                print(f"{file_path}를 {output_path}로 변환 완료")
            except Exception as e:
                print(f"변환 실패: {file_path}, 오류: {e}")

# 변환할 디렉토리 경로
directory_path = r"C:\Downloads\\1"
convert_to_wav(directory_path)
