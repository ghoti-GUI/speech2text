import os

audio_name = "atelier.MP3"

audio_folder = "resource"
audio_folder_path = os.path.join(os.path.curdir, audio_folder)
audio_path = os.path.join(audio_folder_path, audio_name)

result_folder = "result"
result_path = os.path.join(os.path.curdir, result_folder)

if __name__ == "__main__":
    print(audio_path)
    print(result_path)