#ITWS project - Live Speech-to-Speech Translator

import tkinter as tk
from tkinter import ttk, messagebox
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator
import os

# Dictionary of supported languages and their codes
languages = {
    "English": ("en-IN", "en"),
    "Hindi": ("hi-IN", "hi"),
    "Punjabi": ("pa-IN", "pa"),
    "Spanish": ("es-ES", "es"),
    "French": ("fr-FR", "fr")
}

# ---------- Function: Record audio ----------
def record_audio(filename):
    import sounddevice as sd
    import scipy.io.wavfile as wav
    duration = 5
    fs = 44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, recording)

# ---------- Function: Speech to Text ----------
def speech_to_text(filename, lang_code):
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=lang_code)
        return text
    except:
        return "Could not understand."

# ---------- Function: Translate text ----------
def translate_text(text, target_lang):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# ---------- Function: Speak text ----------
def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")

# ---------- Function: Handle Text Input ----------
def handle_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter text or use the microphone.")
        return
    try:
        output_lang_ui = output_lang.get()
        _, output_code = languages[output_lang_ui]

        translated = translate_text(input_text, output_code)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, translated)
        speak(translated, output_code)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# ---------- Function: Handle Mic Input ----------
def handle_mic():
    try:
        input_lang_ui = input_lang.get()
        output_lang_ui = output_lang.get()
        if not input_lang_ui or not output_lang_ui:
            messagebox.showerror("Error", "Please select both input and output languages.")
            return

        input_code, _ = languages[input_lang_ui]
        _, output_code = languages[output_lang_ui]

        filename = "input.wav"
        record_audio(filename)
        text = speech_to_text(filename, input_code)
        os.remove(filename)

        if "Could not understand" in text:
            messagebox.showwarning("Try Again", "Speech not recognized.")
            return

        translated = translate_text(text, output_code)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, translated)
        speak(translated, output_code)
    except Exception as e:
        messagebox.showerror("Mic Input Error", str(e))

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Live Speech-to-Speech Translator")
root.geometry("500x500")

# Input Language Dropdown
tk.Label(root, text="Select Input Language").pack(pady=5)
input_lang = ttk.Combobox(root, values=list(languages.keys()))
input_lang.pack()

# Output Language Dropdown
tk.Label(root, text="Select Output Language").pack(pady=5)
output_lang = ttk.Combobox(root, values=list(languages.keys()))
output_lang.pack()

# Text Input Box
tk.Label(root, text="Enter Text (Optional)").pack(pady=5)
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# Buttons
tk.Button(root, text="Translate Text", command=handle_text).pack(pady=10)
tk.Button(root, text="Use Microphone", command=handle_mic).pack(pady=5)

# Output Display Box
tk.Label(root, text="Translated Output").pack(pady=5)
output_display = tk.Text(root, height=5, width=50)
output_display.pack()

root.mainloop()