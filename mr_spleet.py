from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
import os

def main():
    audio_adapter = AudioAdapter.default()
    separator = Separator('spleeter:5stems')

    # 오디오 파일 로드
    waveform, rate = audio_adapter.load('./audio/바람이불어오는곳-김광석.wav')

    # 오디오 분리
    prediction = separator.separate(waveform)

    # 출력 디렉토리 설정
    output_directory = './audio/output'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 분리된 오디오 저장
    for key, value in prediction.items():
        output_path = os.path.join(output_directory, f"{key}.wav")
        audio_adapter.save(output_path, value, rate, 'wav')

if __name__ == '__main__':
    main()
