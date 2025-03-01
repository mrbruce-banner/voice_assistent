import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import wikipedia
import requests
import pyautogui
import time

# Text-to-Speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice
engine.setProperty('rate', 180)  # Speech speed

# Your chatbot API key (replace with Gemini or OpenAI key)
CHATBOT_API_KEY = "your-gemini-or-openai-api-key"
CHATBOT_API_URL = "https://api.openai.com/v1/chat/completions"  # Adjust for Gemini API if needed

def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=None, phrase_time_limit=None)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        # speak("Sorry sir, I couldn't understand anything please say again...")
        return "none"
    query = query.lower()
    return query

def chatbot_response(message):
    """Get a response from the chatbot."""
    headers = {
        "Authorization": f"Bearer {CHATBOT_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",  # Replace with Gemini model name if using Gemini API
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7,
    }
    response = requests.post(CHATBOT_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code}"



def execute_command(command):
    """Execute tasks based on voice commands."""
    if 'open youtube' in command:
        speak("code accept Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak(" code accept Opening Google.")
        webbrowser.open("https://www.google.com")

    elif 'play song on youtube' in command:
        song = command.replace('play song on youtube', '').strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}.")


    elif 'open notepad' in command:
        speak("code accept Opening Notepad.")
        os.system("notepad")

    elif "you can sleep" in command or "sleep command" in command or "go to sleep mode" in command or "go to sleep" in command:
        speak("okay sir, i am going to sleep you call me anytime sir.")
        while True:
            permission = listen_command()
            if "hey bruce" in permission or "wake up" in permission:
                speak("Welcome back sir, please tell me how may i help you sir?")
                bruce()

    elif 'control panel' in command:
        speak("code accept Opening control panel.")
        os.system("control panel ")

    elif 'open command prompt' in command or "open CMD" in command:
        speak("code accept Opening Command Prompt.")
        os.system("start cmd")

    elif "open free fire" in command:
        pyautogui.hotkey('win')
        time.sleep(0.5)
        pyautogui.write('free fire')
        pyautogui.press('enter')

    elif "open desktop" in command:
        pyautogui.hotkey('win')
        time.sleep(0.5)
        pyautogui.write('desktop')
        pyautogui.press('enter')

    elif "open run prompt" in command or "open run bar" in command or "open run dialog box" in command:
        pyautogui.hotkey('win', 'r')

    elif "print" in command:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('notepad')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.write('iam karthi sir assistent you all welcome my assistent this name for redhook')

        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')

    elif 'goodbye' in command or 'block screen' in command:
        speak("thank you bruce banner.")
        exit()


def bruce():
    """Main function for the J.A.R.V.I.S. assistant."""
    speak("Hello, I am bruce, your personal assistant. any help  karthi sir?")
    while True:
        command = listen_command()
        if command:
            execute_command(command)

if __name__ == "__main__":
    speak("Voice Activation Required")
    while True:
        permission = listen_command()
        if "i am batman" in permission:
            speak("access granted")
            speak("bruce Activated")
            bruce()

        else:
            speak("Access Denied")

