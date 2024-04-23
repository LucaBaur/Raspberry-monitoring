import pyaudio
from vosk import Model, KaldiRecognizer
import json

def recognize_speech():
    model = Model("C:/Users/lb307/Documents/python-workspace/Raspberry-monitoring/vosk-model-small-de-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    # Konfiguration des PyAudio
    audio_format = pyaudio.paInt16
    channels = 1
    sample_rate = 16000
    chunk = 1024

    audio = pyaudio.PyAudio()
    stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

    print("Spreche etwas...")
    stream.start_stream()

    buffer = b''
    while True:
        data = stream.read(chunk)
        buffer += data
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            print(result_dict["text"])  # Drucke nur den erkannten Text
            if "stopp" in result_dict["text"]:
                break  # Beende die Schleife, wenn "stopp" erkannt wurde
        else:
            pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == "__main__":
    recognize_speech()