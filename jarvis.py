import speech_recognition as sr
import webbrowser
import datetime
import pyttsx3
import sys
import subprocess
import tkinter as tk
from tkinter import Scrollbar, Text, Button, PhotoImage, Label

engine = pyttsx3.init()

chatStr = ""

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        try:
            print("Listening...")  # Print "Listening..." when Jarvis is listening
            say("Listening...")    # Inform the user that Jarvis is listening
            query = r.listen(source)
            print("Recognizing...")  # Print "Recognizing..." when Jarvis is recognizing
            say("Recognizing...")    # Inform the user that Jarvis is recognizing
            query = r.recognize_google(query, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            say("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            say(f"Sorry, I encountered an error: {e}")
        return ""

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to open applications on a Windows system
def open_application(application_name):
    try:
        subprocess.Popen(application_name, shell=True)
        print(f"Opening {application_name}...")
    except Exception as e:
        print(f"Error opening {application_name}: {str(e)}")

def on_button_click():
    user_input = user_input_text.get("1.0", tk.END).strip()
    user_input_text.delete("1.0", tk.END)
    if user_input:
        process_user_input(user_input)

def process_user_input(user_input):
    response = None  # Initialize the response variable
    if "say" in user_input:
        say_command_index = user_input.index("say")
        message_to_say = user_input[say_command_index + 1:]
        say(message_to_say)
        response = message_to_say  # Set the response to the spoken message
    else:
        # Add your command processing logic here
        if "open notepad" in user_input:
            open_application("notepad.exe")  # Open Notepad
            response = "Opening Notepad"
        elif "open chrome" in user_input:
            open_application("chrome.exe")   # Open Chrome
            response = "Opening Chrome"
        elif "the time" in user_input:
            now = datetime.datetime.now()
            hour = now.strftime("%H")
            minute = now.strftime("%M")
            response = f"Sir, the time is {hour} o'clock and {minute} minutes"
            say(response)  # Speak the response
        elif "exit" in user_input:
            response = "Goodbye, sir!"
            say(response)
            sys.exit()  # Use sys.exit() to properly exit the script
        else:
            # Add conversation commands here
            if "how are you" in user_input:
                response = "I'm just a computer program, but I'm here to help you Sir!"
                say(response)
            elif "tell me a joke" in user_input:
             joke = "you"
             say(joke)
            elif "tell me another joke" in user_input:
             joke = "Parallel lines have so much in common. It's a shame they'll never meet!"
             say(joke)
            elif "chat with me" in user_input:
              response = "Sure, I'd love to chat with you! What's on your mind?"
              say(response)
            elif "who is your creator" in user_input:
              response = "I was created by a team of developers at OpenAI."
              say(response)
            else:
                sites = [
                  ["youtube", "https://www.youtube.com"],
                  ["wikipedia", "https://www.wikipedia.com"],
                  ["google", "https://www.google.com"],
                  ["chat", "https://chat.openai.com/"],
                  ["example2", "https://www.example2.com"],
                  ["example2", "https://www.example2.com"],
                  ["github", "https://www.github.com"],
                  ["facebook", "https://www.facebook.com"],
                  ["twitter", "https://www.twitter.com"],
                  ["linkedin", "https://www.linkedin.com"],
                  ["reddit", "https://www.reddit.com"],
                  ["amazon", "https://www.amazon.com"],
                  ["ebay", "https://www.ebay.com"],
                  ["stackoverflow", "https://www.stackoverflow.com"],
                  ["instagram", "https://www.instagram.com"],
                  ["pinterest", "https://www.pinterest.com"],
                  ["netflix", "https://www.netflix.com"],
                  ["hulu", "https://www.hulu.com"],
                  ["yahoo", "https://www.yahoo.com"],
                  ["bing", "https://www.bing.com"],
                  ["spotify", "https://www.spotify.com"],
                ]
                
                for site in sites:
                    if f"open {site[0]}".lower() in user_input:
                        say(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])
                        response = f"Opening {site[0]}"
                        break  # Exit the loop after opening the website
            
            if response is None:
                response = "Command not recognized."

    # Insert the response into the GUI
    user_input_text.insert(tk.END, response + "\n")

def process_speech_input():
    query = takeCommand()
    if query:
        user_input_text.insert(tk.END, query)

# Create the GUI window
root = tk.Tk()
root.title("Jarvis AI")
root.geometry("400x400")

# Create a text area for user input
user_input_text = Text(root, height=4, width=40)
user_input_text.pack(pady=10)

# Create a "Submit" button
submit_button = Button(root, text="Submit", command=on_button_click)
submit_button.pack()

# Create a "Speech Input" button
speech_input_button = Button(root, text="Speech Input", command=process_speech_input)
speech_input_button.pack()

# Start the GUI main loop
root.mainloop()
