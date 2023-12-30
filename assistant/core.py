# assistant/core.py

from assistant.utils import speak, get_audio
from datetime import datetime
from gtts import gTTS
import webbrowser
import os
import speech_recognition as sr
import spacy


def handle_help():

    help_message = """
    Below are the tasks X can help you with:

    Available commands:
        - Tells you the current date and time.
        - Play music from your music folder.
        - Gives you google search information.
        - vvv.

    >=> Feel free to ask for help on specific tasks or inquire about available features.
    """

    speak(help_message)


def handle_unknown_command(contex,command):
    print(f"I'm sorry, I didn't understand the command: {command}")



def greet_user(context):
    user_name = context.get_user_name()

    if user_name:
        speak(f"Hello, {user_name}! How can I help today?")
    else:
        speak("Hello! What's your name?")
        user_name = get_audio()

        if user_name:
            context.set_user_name(user_name)
            speak(f"Hello, {user_name}! How can I assist you?")
        else:
            speak("I'm sorry, I didn't catch your name. Please try again.")
            greet_user(context)


def get_part_of_day(hour):
    if 0 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    else:
        return "evening"


def handle_time(context):
    current_time = datetime.now()
    current_hour = current_time.hour

    part_of_day = get_part_of_day(current_hour)
    speak(f"The current time is {current_time.strftime('%H:%M:%S')}, and it is {part_of_day}.")


def handle_date(context):
    current_date = datetime.now().strftime("%d-%m-%Y")
    speak(f" Today's date is {current_date}.")


def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


def handle_google_search(context):
    speak("What would you like to search on Google?")
    query = get_audio()
    
    if query:
        speak(f"Searching Google for {query}.")
        search_google(query)
    else:
        speak("Sorry, I didn't catch that. Could you please repeat your query?")



def play_music():
    speak("Opening music...")
    music_folder = "C:\\Users\\MDC\\Music"
    # Get the list of music files in the folder
    songs = os.listdir(music_folder)

    if songs:
        # Select the first song
        song_to_play = os.path.join(music_folder, songs[0])

        # Open the song
        os.system(song_to_play)
    else:
        speak("No songs found in your music folder.")

def thank():
    speak("You're welcome, {user_name}")