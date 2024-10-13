import whisper
import speech_recognition as sr
import os
from pydub import AudioSegment
import ffmpeg

# Specify the input and output files
method = 'whisper'  # 'google' or 'whisper'
content = 'video'   # 'audio' or 'video'
name = 'test'       # base name of the file

input_file = name + '.mp4'
filename = name + '.wav'

if content == 'video':
    # Extract the audio
    if (os.path.exists(filename) == False): 
        try:
            ffmpeg.input(input_file).output(name + '.m4a').run(quiet=False, overwrite_output=True)
        except ffmpeg.Error as e:
            print('Error:', e)

## Conversion from m4a to wav 
audio = AudioSegment.from_file(name + '.m4a', format='m4a')
audio.export(filename, format='wav')

if method == 'whisper':
    model = whisper.load_model('turbo')
    result = model.transcribe(filename)
    text = str(result["text"])
    
elif method == 'google': 
    ### GOOGLE ###
    # Initialize the recognizer
    r = sr.Recognizer()

    # Open the file
    with sr.AudioFile(filename) as source:
        # Listen for the data (load audio to memory)
        audio_data = r.record(source)
        # Recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='fr-FR')
    
def write_text_with_line_breaks(text, filename, line_length=100):
    words = text.split()  # Split the text into words
    current_line = ""

    with open(name + '.txt', 'w', encoding='utf-8') as f:
        for word in words:
            # Check if adding the word exceeds the line length
            if len(current_line) + len(word) + 1 <= line_length:
                if current_line:  # Add a space if the line is not empty
                    current_line += " "
                current_line += word
            else:
                # Write the current line and reset for the new line
                f.write(current_line + '\n')
                current_line = word  # Start a new line with the current word

        # Write the last line if it's not empty
        if current_line:
            f.write(current_line + '\n')

write_text_with_line_breaks(text, filename)
