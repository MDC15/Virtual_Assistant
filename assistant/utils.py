
import os
import playsound
from gtts import gTTS
import speech_recognition as sr
import keyboard


def speak(text):
    print("\nVirtual Assistant:", text)
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("output.mp3")
    playsound.playsound("output.mp3", True)
    os.remove("output.mp3")


def get_audio():
    recognizer = sr.Recognizer()
    audio = None

    with sr.Microphone() as source:
        print(" >>> Listening... ")
        try:
            audio = recognizer.listen(source, timeout=6)
        except sr.WaitTimeoutError:
            print("\n-->> Timeout. Press any key to continue...")
            keyboard.read_key()  

    try:
        if audio:
            print("--- Processing audio... ")
            text = recognizer.recognize_google(audio, language="en-US")
            print(f" \n You: {text}")
            return text.lower()
        else:
            return ""
    except sr.UnknownValueError:
        print("Virtual Assistant: I couldn't understand you.")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return ""
