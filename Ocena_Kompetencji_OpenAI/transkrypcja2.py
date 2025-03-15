import speech_recognition as sr

# Ścieżka do pliku audio
audio_path = 'D:\projekt_badawczy\pierwszy.wav'

# Inicjalizacja rozpoznawania mowy
r = sr.Recognizer()

with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)

# Transkrypcja audio (język polski)
try:
    text = r.recognize_google(audio_data, language='pl-PL')
    print(text)

    # Zapisywanie transkrypcji do pliku tekstowego
    with open('tekst.txt', 'w', encoding='utf-8') as f:
        f.write(text)

    print("Transkrypcja została zapisana do pliku 'transkrypcja.txt'.")

except sr.UnknownValueError:
    print("Nie udało się rozpoznać mowy.")
except sr.RequestError as e:
    print(f"Błąd połączenia z usługą rozpoznawania mowy; {e}")
