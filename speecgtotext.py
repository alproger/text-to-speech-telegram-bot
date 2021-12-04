import speech_recognition as sr

# obtain path to "Three.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "Three.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile('Three.wav') as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "NVz5l9PuSMLBpNdLT0lljw=="  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "TySyat4A5MlRA35ozS2ZaGRF7x0ZAiynXCgM2CTG5o9LaCiVPMbmN5WCLk0pVA0sxyAAWG_RwuNAchnhesGqEw=="  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))