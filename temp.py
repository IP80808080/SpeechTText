import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import playsound

# Set up the recognition object
r = sr.Recognizer()

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Speech to Text")

# Create a label and a text entry box
label = tk.Label(root, text="Enter text:")
text_box = tk.Entry(root)
label.pack()
text_box.pack()

# Create a "Speak" button
def speak():
    # Get the text from the entry box
    text = text_box.get()

    # Use the text-to-speech API to convert the text to speech
    tts = gTTS(text=text)
    tts.save("speech.mp3")
    playsound("speech.mp3")

speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack()

# Start the GUI event loop
root.mainloop()
