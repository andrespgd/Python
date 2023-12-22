import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('\nSay something!\n')
    audio = r.listen(source)

try:
    print('Google Speech Recognition thinks you said: \n\n' + r.recognize_google(audio))
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print('Could not request results from Google Speech Recognition service; {0}'.format(e))
