# 1. 학습할 파일 
# 1) 사용자가 학습하고 싶은 파일이 있는 디렉터리를 선택하면 해당 디렉터리 내에 있는 모든 파일을 .wav로 확장자 변경
# 2) 학습할 파일 mr 제거
# 3) 학습

# 2. 추론할 파일 선택
# 1) 사용자가 추론하고 싶은 파일 선택
# 2) 사용자가 학습한 목소리의 pitch에 맞춰 추론할 파일 pitch 조정
# 3) 추론할 파일 mr 분리
# 4) 추론
# 5) mr과 추론한 파일 다시 합치기

# 3. 결과물 저장할 디렉터리 선택
# 1) 사용자가 선택한 디렉터리에 결과물 저장


from infer_file_to_wav import Infer_File_To_Wav
from train_file_to_wav import Train_File_To_Wav
from mr_spleet import Mr_Spleet
from mr_remove import Mr_Remove
from pitch_extraction import Pitch_Extraction
from pitch_control import Pitch_Control
from mr_combine import Mr_Combine

def main():
    #Infer_File_To_Wav()
    #Train_File_To_Wav()
    #Mr_Spleet()
    #Mr_Remove()
    
    ## 추론 및 학습 진행
    
    # 피치 추출 함수 실행 및 반환 값 저장
    target_pitch, origin_pitch = Pitch_Extraction()

    # 반환된 피치 값으로 피치 조절 함수 실행
    Pitch_Control(target_pitch, origin_pitch)

    #Mr_Combine()

if __name__ == '__main__':
    main()
