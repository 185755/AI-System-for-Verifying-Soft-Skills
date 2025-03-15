from moviepy.editor import VideoFileClip

# Ścieżka do pliku wideo
video_path = 'D:\projekt_badawczy\pierwszy.mp4'

# Wczytanie wideo
video_clip = VideoFileClip(video_path)

# Wyodrębnienie audio
audio_clip = video_clip.audio

# Zapisanie audio do pliku WAV
audio_path = 'D:\projekt_badawczy\pierwszy.wav'
audio_clip.write_audiofile(audio_path)
