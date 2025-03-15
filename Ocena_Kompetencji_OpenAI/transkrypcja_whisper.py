import whisper

# Ścieżka do pliku audio
audio_path = 'pierwszy.wav'

# Wczytanie modelu
model = whisper.load_model('base')  # Dostępne modele: 'tiny', 'base', 'small', 'medium', 'large'

# Transkrypcja audio
result = model.transcribe(audio_path, language='pl')

# Zapis transkrypcji do pliku
with open('transkrypcja_whisper.txt', 'w', encoding='utf-8') as f:
    f.write(result['text'])
