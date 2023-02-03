# Principal 

import speech_recognition as sr 

    #Cria um reconhecedor
r = sr.Recognizer()


#Abrir dispositivo de audio

with sr.Microphone() as source:
  while True:
      audio = r.listen(source) #Define microfone como fonte de áudio

      print(r.recognize_google(audio, language='pt'))