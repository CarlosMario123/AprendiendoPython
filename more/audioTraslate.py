import speech_recognition as sr
from deep_translator import GoogleTranslator
import pyttsx3
from playsound import playsound

# Función para transcribir audio
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='es-ES')  # Reconocimiento en español
        return text

# Función para traducir texto
def translate_text(text):
    translated_text_en = GoogleTranslator(source='auto', target='en').translate(text=text)
    return translated_text_en

# Función para generar y guardar audio a partir de texto con ajustes para voz humana
def save_text_to_audio(text, output_file, rate=130, pitch=50, volume=0.9):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Ajusta la velocidad del habla
    engine.setProperty('volume', volume)  # Ajusta el volumen del habla
    # Configuración de voz (asegúrate de que la voz está disponible en tu sistema)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Cambia el índice para seleccionar la voz deseada
    engine.setProperty('pitch', pitch)  # Ajusta el tono del habla
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Nombre del archivo de audio a transcribir (debe ser un archivo WAV)
audio_file_path = 'more/Grabación.wav'

# Transcribe el audio
transcribed_text = transcribe_audio(audio_file_path)

# Traduce el texto
translated_text_en = translate_text(transcribed_text)

print('Texto Español:', transcribed_text)
print('Texto en Inglés:', translated_text_en)

# Nombre del archivo de audio generado
output_audio_file = 'translated_audio.wav'

# Generar y guardar audio en inglés con ajustes para voz humana
save_text_to_audio(translated_text_en, output_audio_file, rate=140, pitch=70, volume=0.9)  # Ajustes para voz humana

print(f'Audio guardado como: {output_audio_file}')

# Reproducir el archivo de audio generado
playsound(output_audio_file)
