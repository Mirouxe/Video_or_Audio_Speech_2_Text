# Video_or_Audio_Speech_2_Text
Transcription Audio-Video avec Whisper et Google Speech Recognition

Ce projet permet d'extraire l'audio d'un fichier vidéo et de le transcrire en texte à l'aide des modèles de reconnaissance vocale Whisper ou Google Speech Recognition. Les transcriptions sont enregistrées dans un fichier texte avec des sauts de ligne pour une meilleure lisibilité.

## Fonctionnalités

- Extraction de l'audio à partir de fichiers vidéo au format MP4.
- Conversion de l'audio au format M4A vers WAV.
- Transcription audio en texte à l'aide de deux méthodes :
  - Whisper (modèle open-source d'OpenAI)
  - Google Speech Recognition
- Enregistrement du texte transcrit dans un fichier texte avec gestion des sauts de ligne.

## Prérequis

Avant d'exécuter le code, assurez-vous d'avoir installé les dépendances nécessaires :

- Python 3.6 ou supérieur
- whisper
- speech_recognition
- pydub
- ffmpeg

Vous pouvez installer les dépendances via pip :
```bash
pip install git+https://github.com/openai/whisper.git
pip install SpeechRecognition
pip install pydub
