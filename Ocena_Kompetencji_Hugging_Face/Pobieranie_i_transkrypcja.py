from __future__ import print_function
import os.path
import io
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

import whisper

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def main():
    """Pobiera pliki mp4 z folderu na Dysku Google i dokonuje transkrypcji."""
    creds = None
    # Autoryzacja i uzyskanie poświadczeń
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    folder_id = '1lmm3e5s3LAyvFGVsq9y5VrVU5UktMweq'

    # Pobierz listę plików mp4 w folderze
    query = f"'{folder_id}' in parents and mimeType='video/mp4'"
    results = service.files().list(
        q=query,
        pageSize=1000,
        fields="nextPageToken, files(id, name)"
    ).execute()
    items = results.get('files', [])

    if not items:
        print('Brak plików mp4 w podanym folderze.')
        return

    print(f"Znaleziono {len(items)} plików mp4 w folderze.")

    # Wczytanie modelu Whisper
    model = whisper.load_model('base')

    # Iteracja przez pliki
    for item in items:
        file_id = item['id']
        file_name = item['name']
        transcription_file = f"{os.path.splitext(file_name)[0]}_transkrypcja.txt"

        # Sprawdzenie, czy transkrypcja już istnieje
        if os.path.exists(transcription_file):
            print(f"Plik '{file_name}' został już przetworzony, pomijam.")
            continue

        print(f"\nPobieranie pliku: {file_name}")

        # Pobieranie pliku mp4
        with io.FileIO(file_name, 'wb') as fh:
            request = service.files().get_media(fileId=file_id)
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Pobieranie {file_name}: {int(status.progress() * 100)}%.")

        # Transkrypcja pliku mp4 przy użyciu Whisper
        print(f"Transkrypcja pliku: {file_name}")
        result = model.transcribe(file_name, language='pl')
        transcription = result['text']

        # Zapis transkrypcji do pliku tekstowego
        with open(transcription_file, 'w', encoding='utf-8') as f:
            f.write(transcription)

        print(f"Transkrypcja została zapisana do pliku '{transcription_file}'.")

        # Usunięcie oryginalnego pliku mp4 po transkrypcji
        try:
            os.remove(file_name)
            print(f"Plik '{file_name}' został usuniety, aby zaoszczedzic miejsce.")
        except OSError as e:
            print(f"Wystapil blad podczas usuwania pliku '{file_name}': {e}")

    print("\nPrzetwarzanie zakonczone.")

#if __name__ == '__main__':
#    main()

#Wywołanie Funckji
main()




