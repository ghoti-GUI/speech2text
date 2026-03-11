import os
from pathlib import Path

from config import result_path, audio_folder_path
from model import WhisperModel

def convert(audio_path:str, txt_name:str=None):
    audio_file = Path(audio_path)
    if not audio_file.exists():
        raise FileNotFoundError(f"找不到文件: {audio_file}")

    if txt_name is None:
        txt_name = audio_file.with_suffix(".txt").name
    
    txt_path = os.path.join(result_path, txt_name)

    
    model = WhisperModel()
    result = model.convert(audio_path, "fr")
    text = result["text"].strip()

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    test_audio_path = os.path.join(audio_folder_path, "test-fr.wav")
    convert(test_audio_path, "test-fr-wav.txt")

    test_audio_path = os.path.join(audio_folder_path, "test-fr.mp3")
    convert(test_audio_path, "test-fr-mp3.txt")