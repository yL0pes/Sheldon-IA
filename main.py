#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyttsx3
import core

#Síntese de Fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
     engine.say(text)
     engine.runAndWait()
     

if not os.path.exists("model"):
     print ("Please download the model from https://alphacephei.com/vask/models and unpack as 'model' in the current folder.")
     exit (1)
 
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()  

while True:
    data = stream.read(3000, exception_on_overflow=False)
    if len(data) == 0:
         break
    if rec.AcceptWaveform(data):
         result = rec.Result()
         result = json.loads(result)
         
         if result is not None:
              text = result['text']
              
              print(text)
              
              if text == 'que horas são' or text == 'me diga as horas':
                   speak(core.SystemInfo.get_time())