# pip install gTTS playsound pyttsx3

import gtts  
from playsound import playsound

def speak(text):
    # tld="com.au"
    tld="ca"
    audio = gtts.gTTS(text=text, lang='en', slow=False, tld=tld)
    # https://gtts.readthedocs.io/en/latest/module.html#localized-accents
    #voice="en-AU-Standard-C"

    filepath="data/audio-out.mp3"
    audio.save(filepath)
    playsound(filepath)

speak("This is your chat bot speaking")
