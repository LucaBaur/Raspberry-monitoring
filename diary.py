import os
import json
from datetime import date

def write_diary_entry(entry):
    # Bestimme den Pfad zum Diary-Ordner
    diary_dir = os.path.join(os.path.dirname(__file__), "diary")

    # Erstelle den Ordner "diary", wenn er noch nicht existiert
    if not os.path.exists(diary_dir):
        os.makedirs(diary_dir)

    # Bestimme den Dateinamen mit dem heutigen Datum
    today = date.today()
    filename = os.path.join(diary_dir, f"{today}.txt")

    # Schreibe den Tagebucheintrag in die Textdatei
    with open(filename, "w") as file:
        file.write(f"Tagebucheintrag {today}\n")  # Erste Zeile mit "Tagebucheintrag" und Datum
        file.write(entry)

    print(f"Tagebucheintrag wurde unter '{filename}' gespeichert.")


def create_diary_entry(recognizer, stream, chunk):
    print("Spreche deinen Tagebucheintrag...")
    diary_entry = ""
    while True:
        data = stream.read(chunk)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            print(result_dict["text"])  # Drucke den erkannten Text
            if "tagebucheintrag beenden" in result_dict["text"]:
                break  # Beende die Schleife, wenn "tagebucheintrag beenden" erkannt wurde
            else:
                diary_entry += result_dict["text"] + " "
        else:
            pass
    print("TAGEBUCHEINTRAG WIRD ERSTELLT:")
    print(diary_entry )
    write_diary_entry(entry=diary_entry)

    
#if __name__ == "__main__":
#    write_diary_entry(get_diary_input())