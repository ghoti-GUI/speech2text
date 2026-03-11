import os
import whisper
from pathlib import Path

from config import audio_folder_path, result_path


class WhisperModel():
    def __init__(self, model_name:str="base"):
        self.model = whisper.load_model("base") # could be 


    def convert(self, audio_path:str, language:str="fr")->str:
        result = self.model.transcribe(audio_path, language=language)
        return result


if __name__ == "__main__":
    model = WhisperModel("base")

    test_audio_path = os.path.join(audio_folder_path, "test-fr.wav")
    print("wav: ", model.convert(test_audio_path, "fr"), "\n\n")

    test_audio_path = os.path.join(audio_folder_path, "test-fr.mp3") 
    print("mp3: ", model.convert(test_audio_path, "fr"), "\n\n")