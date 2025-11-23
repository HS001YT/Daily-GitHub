import tkinter as tk
from tkinter import ttk, messagebox
from gtts import gTTS
from playsound import playsound
import os
import threading
import speech_recognition as sr
from deep_translator import GoogleTranslator

# -----------------------------
# Languages
# -----------------------------
languages = {
    "English": ("en-IN", "en"),
    "Hindi": ("hi-IN", "hi"),
    "Punjabi": ("pa-IN", "pa"),
    "Spanish": ("es-ES", "es"),
    "French": ("fr-FR", "fr")
}

continuous_mode = False  # Flag for live translation

# -----------------------------
# Text-to-Speech
# -----------------------------
def speak(text, lang_code='en'):
    try:
        tts = gTTS(text=text, lang=lang_code)
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        print("TTS Error:", e)

# -----------------------------
# Translation
# -----------------------------
def translate_text_func(text, target_lang):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# -----------------------------
# Manual Mic Input
# -----------------------------
def handle_mic():
    input_lang_ui = input_lang.get()
    if not input_lang_ui:
        messagebox.showerror("Error", "Please select input language.")
        return

    input_code, _ = languages[input_lang_ui]
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 400
    recognizer.pause_threshold = 1.0

    try:
        with sr.Microphone() as source:
            status_label.config(text="🎤 Listening...")
            root.update()
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        status_label.config(text="🧠 Recognizing...")
        root.update()
        text = recognizer.recognize_google(audio, language=input_code)

        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, text)
        status_label.config(text="✅ Speech recognized. Ready to translate.")

    except sr.UnknownValueError:
        status_label.config(text="⚠ Could not understand.")
        messagebox.showwarning("Try Again", "Could not understand speech.")
    except Exception as e:
        messagebox.showerror("Mic Input Error", str(e))
        status_label.config(text="❌ Mic Error")

# -----------------------------
# Manual Translate
# -----------------------------
def handle_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter or record text first.")
        return

    output_lang_ui = output_lang.get()
    if not output_lang_ui:
        messagebox.showerror("Error", "Please select output language.")
        return

    _, output_code = languages[output_lang_ui]

    try:
        status_label.config(text="🧠 Translating...")
        root.update()
        translated = translate_text_func(input_text, output_code)
        output_display.delete("1.0", tk.END)
        output_display.insert(tk.END, translated)
        status_label.config(text="✅ Translation done.")
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))
        status_label.config(text="❌ Translation Error")

# -----------------------------
# Speak Translated Text
# -----------------------------
def speak_translated():
    translated_text = output_display.get("1.0", tk.END).strip()
    if not translated_text:
        messagebox.showerror("Error", "Please translate text first.")
        return

    output_lang_ui = output_lang.get()
    if not output_lang_ui:
        messagebox.showerror("Error", "Please select output language.")
        return
    _, output_code = languages[output_lang_ui]

    status_label.config(text="🔊 Speaking...")
    root.update()
    speak(translated_text, output_code)
    status_label.config(text="✅ Done speaking.")

# -----------------------------
# Continuous Translation Thread
# -----------------------------
def continuous_translation_thread():
    global continuous_mode
    continuous_mode = True

    input_lang_ui = input_lang.get()
    output_lang_ui = output_lang.get()

    if not input_lang_ui or not output_lang_ui:
        messagebox.showerror("Error", "Please select both languages.")
        continuous_mode = False
        return

    input_code, _ = languages[input_lang_ui]
    _, output_code = languages[output_lang_ui]

    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 400
    recognizer.pause_threshold = 1.0

    status_label.config(text="🎙️ Live Translation Active")
    root.update()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while continuous_mode:
            try:
                status_label.config(text="🎧 Listening...")
                root.update()
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

                status_label.config(text="🧠 Recognizing...")
                root.update()
                text = recognizer.recognize_google(audio, language=input_code)
                text_input.delete("1.0", tk.END)
                text_input.insert(tk.END, text)

                status_label.config(text="🌐 Translating...")
                root.update()
                translated = translate_text_func(text, output_code)
                output_display.delete("1.0", tk.END)
                output_display.insert(tk.END, translated)

                status_label.config(text="🔊 Speaking...")
                root.update()
                speak(translated, output_code)

                status_label.config(text="✅ Waiting for next speech...")
                root.update()
            except sr.UnknownValueError:
                status_label.config(text="⚠ Could not understand. Speak again.")
                root.update()
            except Exception as e:
                print("Error:", e)
                status_label.config(text=f"❌ Error: {e}")
                root.update()
    status_label.config(text="🛑 Live Translation Stopped")

def start_continuous_mode():
    threading.Thread(target=continuous_translation_thread, daemon=True).start()

def stop_continuous_mode():
    global continuous_mode
    continuous_mode = False
    status_label.config(text="🛑 Live Translation Stopped")

# -----------------------------
# Copy Functions
# -----------------------------
def copy_input():
    root.clipboard_clear()
    root.clipboard_append(text_input.get("1.0", tk.END).strip())

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_display.get("1.0", tk.END).strip())

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Live Speech-to-Speech Translator")
root.geometry("750x700")

# Top: Languages Selection
tk.Label(root, text="Select Languages", font=("Arial", 14)).pack(pady=5)

lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)
tk.Label(lang_frame, text="From:").grid(row=0, column=0, padx=5)
input_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), width=15)
input_lang.grid(row=0, column=1, padx=5)
tk.Label(lang_frame, text="To:").grid(row=0, column=2, padx=5)
output_lang = ttk.Combobox(lang_frame, values=list(languages.keys()), width=15)
output_lang.grid(row=0, column=3, padx=5)

# Live Translation Button
tk.Button(root, text="🎙️ Live Translation", command=start_continuous_mode, width=25, bg="#d0ffd0").pack(pady=5)

# Input Text Area
tk.Label(root, text="Enter or Record Text").pack(pady=5)
text_input = tk.Text(root, height=5, width=80)
text_input.pack(pady=5)

# Mic + Copy Input buttons
btn_frame_input = tk.Frame(root)
btn_frame_input.pack(pady=5)
tk.Button(btn_frame_input, text="🎤 Mic Input", command=handle_mic, width=15).grid(row=0, column=0, padx=5)
tk.Button(btn_frame_input, text="📋 Copy Input", command=copy_input, width=15).grid(row=0, column=1, padx=5)

# Translate Button
tk.Button(root, text="🌐 Translate", command=handle_text, width=25).pack(pady=5)

# Output Text Area
tk.Label(root, text="Translated Output").pack(pady=5)
output_display = tk.Text(root, height=5, width=80)
output_display.pack(pady=5)

# Speak + Copy Output buttons
btn_frame_output = tk.Frame(root)
btn_frame_output.pack(pady=5)
tk.Button(btn_frame_output, text="🔊 Speak Translation", command=speak_translated, width=20).grid(row=0, column=0, padx=5)
tk.Button(btn_frame_output, text="📋 Copy Output", command=copy_output, width=20).grid(row=0, column=1, padx=5)

# Clear All Button
tk.Button(root, text="🧹 Clear All", command=lambda: [text_input.delete("1.0", tk.END),
                                                      output_display.delete("1.0", tk.END)], width=25).pack(pady=5)

# Stop Continuous Mode Button
tk.Button(root, text="⏹ Stop Live Translation", command=stop_continuous_mode, width=25, bg="#ffcccc").pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=5)

# Keyboard Shortcuts
root.bind('<Return>', lambda e: handle_text())
root.bind('<Control-m>', lambda e: handle_mic())

root.mainloop()
