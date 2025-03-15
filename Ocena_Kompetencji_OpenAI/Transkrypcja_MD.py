# DO zainstalowania
# pip install moviepy transformers torch


from moviepy.editor import VideoFileClip
from transformers import pipeline

# Ścieżka do pliku MP4
video_path = "sciezka/do/pliku.mp4"

# 1. Konwersja MP4 na audio (WAV)
video = VideoFileClip(video_path)
audio_path = "audio.wav"
video.audio.write_audiofile(audio_path, codec='pcm_s16le')  # codec 'pcm_s16le' jest wymagany dla formatu WAV

# 2. Transkrypcja audio na tekst przy użyciu modelu Whisper
# Ładowanie pipeline dla transkrypcji
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")

# Wczytanie i transkrypcja audio
with open(audio_path, "rb") as audio_file:
    transcription = transcriber(audio_file)["text"]

# 3. Zapis transkrypcji do pliku tekstowego
with open("transkrypcja.txt", "w") as f:
    f.write(transcription)

print("Transkrypcja została zapisana do pliku transkrypcja.txt")
