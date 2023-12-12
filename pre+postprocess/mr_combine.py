from pydub import AudioSegment
import os

def combine_tracks(vocals_path, accompaniment_path, output_path):
    vocals = AudioSegment.from_file(vocals_path)
    accompaniment = AudioSegment.from_file(accompaniment_path)

    # 보컬과 반주의 볼륨 차이 계산
    diff = accompaniment.dBFS - vocals.dBFS

    # 보컬 볼륨 조절
    adjusted_vocals = vocals + diff

    # 조절된 볼륨으로 트랙 결합
    combined = adjusted_vocals.overlay(accompaniment)

    combined.export(output_path, format='wav')

def find_first_wav(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.wav'):
            return os.path.join(directory, filename)
    return None

def Mr_Combine():
    vocals_directory = './audio/pitch_change/vocal'
    accompaniment_directory = './audio/pitch_change/mr'
    output_directory = './audio/output'

    vocals_path = find_first_wav(vocals_directory)
    accompaniment_path = find_first_wav(accompaniment_directory)

    if not vocals_path or not accompaniment_path:
        print("Vocals or accompaniment file not found.")
        return

    output_path = os.path.join(output_directory, 'combined_track.wav')
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    combine_tracks(vocals_path, accompaniment_path, output_path)

Mr_Combine()
