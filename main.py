import whisper
# from pyannote.audio import Pipeline

def recognize_audio(audio_path):
    model = whisper.load_model("large")
    result = model.transcribe(audio_path, language="ru")
    result = result["text"]
    return result

if __name__ == "__main__":
    audio_path = "1.wav"
    text = recognize_audio(audio_path)
    print(text)