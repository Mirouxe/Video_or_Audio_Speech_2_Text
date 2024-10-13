import whisper
import speech_recognition as sr
import os
from pydub import AudioSegment
import ffmpeg

# Spécifier le fichier d'entrée et de sortie
methode = 'whisper' # google ou whisper 
contenu = 'texte'  # texte ou video
nom = 'PT4'
input_file = nom + '.mp4'
filename = nom + '.wav'

if contenu == 'video':
    # Extraire l'audio
    if (os.path.exists(filename)==False) : 
        try:
            ffmpeg.input(input_file).output(nom + '.m4a').run(quiet=False, overwrite_output=True)
        except ffmpeg.Error as e:
            print('Error:', e)

## Conversion m4a --> wav 
audio = AudioSegment.from_file(nom + '.m4a', format='m4a')
audio.export(filename, format='wav')

if methode == 'whisper':
    model = whisper.load_model('turbo')
    result = model.transcribe(filename)
    text = str(result["text"])
    
elif methode == 'google': 
    ### GOOGLE ###
    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='fr-FR')
    
def write_text_with_line_breaks(text, filename, line_length=100):
    words = text.split()  # Séparer le texte en mots
    current_line = ""

    with open(nom + '.txt', 'w', encoding='utf-8') as f:
        for word in words:
            # Vérifier si ajouter le mot dépasse la longueur de ligne
            if len(current_line) + len(word) + 1 <= line_length:
                if current_line:  # Ajouter un espace si la ligne n'est pas vide
                    current_line += " "
                current_line += word
            else:
                # Écrire la ligne actuelle et réinitialiser pour la nouvelle ligne
                f.write(current_line + '\n')
                current_line = word  # Commencer une nouvelle ligne avec le mot actuel

        # Écrire la dernière ligne si elle n'est pas vide
        if current_line:
            f.write(current_line + '\n')

write_text_with_line_breaks(text, filename)