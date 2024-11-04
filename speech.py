from deep_translator import GoogleTranslator
from gtts import gTTS    
import os

def translate_text(text):
    t = GoogleTranslator(source='en', target='ml')
    return t.translate(text)

def text_to_speech(text, file_name='speech.mp3'):
    tts = gTTS(text=text, lang='ml')
    tts.save(file_name)
    os.system('start ' + file_name)  # added a space after 'start'

text = input('Enter the input: ')

translated = translate_text(text)

print('Original:', text)
print('Translated:', translated)

text_to_speech(translated)
