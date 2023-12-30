# Main
from assistant.context import Context
from assistant.utils import get_audio, speak
from assistant.core import greet_user, handle_help, handle_unknown_command, handle_time,  handle_date, handle_google_search, play_music


# Starting 
def main():
    context = Context()

    greet_user(context)

    while True:
        command = get_audio()

        if "goodbye" in command or "see you" in command:
            speak("Sure, see you next time!\n")
            break
        elif "time" in command:
            handle_time(context)
        elif "day" in command or "date" in command:
            handle_date(context)
        elif "search" in command or "google" in command:
            handle_google_search(context)
        elif "audio" in command or "music" in command:
            play_music()
        elif "help me" in command or "need support" in command:
            handle_help()
        else:
            handle_unknown_command(context, command)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("\n @-> The program has been interrupted by the user.")
