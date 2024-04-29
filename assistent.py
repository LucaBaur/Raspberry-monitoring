import pyaudio
from vosk import Model, KaldiRecognizer
import json
import diary
import gui
import threading, logging
import sys


class Assistent:
    def __init__(self, gui) -> None:
        self.gui = gui
        self.model =  Model("C:/Users/lb307/Documents/python-workspace/Raspberry-monitoring/vosk-model-small-de-0.15")
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 16000
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.audio_format, channels=self.channels, rate=self.sample_rate, input=True, frames_per_buffer=self.chunk)
        self.running = True


    def stop_assistent(self):
        self.running = False
        print("Spracherkennung beendet.")
        
    
    def silent_assistent(self):
        print("silent_assistent gestartet.")
        self.gui.head_label.configure(text_color="red")
        self.stream.start_stream()

        buffer = b''
        while True:
            data = self.stream.read(self.chunk)
            buffer += data
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                result_dict = json.loads(result)
                if "modrig" in result_dict["text"]:
                    print("silent_assistent beendet.")
                    self.loud_assistent()
                    break

            else:
                pass
        self
    def loud_assistent(self):
        print("loud_assistent gestartet.")
        self.gui.head_label.configure(text_color="green") 
        self.stream.start_stream()
        buffer = b''
        
        while True:
            data = self.stream.read(self.chunk)
            buffer += data
            if self.recognizer.AcceptWaveform(data):
                result = self.recognizer.Result()
                result_dict = json.loads(result)
               
                if "beenden" in result_dict["text"]:
                    print("loud_assistent beendet.")
                    self.silent_assistent()
                    break
                    
                elif "schließen" in result_dict["text"]:
                    self.gui.head_label.configure(text_color="white") 
                    self.stop_assistent()  # Rufe die Methode zum Schließen der Instanz auf
                elif "erstelle tagebucheintrag" in result_dict["text"]:
                    print("TAGEBUCHEINTRAG WIRD ERSTELLT:")
                    diary.create_diary_entry(self.recognizer, self.stream, self.chunk)
                self.gui.assistent_text.configure(text=result_dict["text"])
                print(result_dict["text"])
            else:
                pass

    def start_assistent(self):
        while self.running:
            print("Spracherkennung gestartet.")
            self.silent_assistent()
        
