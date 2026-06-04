from tkinter import *
from tkinter import ttk, messagebox, filedialog
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import speech_recognition as sr
import threading
import datetime
import os

DARK_BG = "#211A2E"
DARK_INPUT = "#37163E"
DARK_HISTORY = "#0F3460"
ACCENT = "#E94560"

LIGHT_BG = "#F5F5F5"
LIGHT_INPUT = "#FFFFFF"

dark_mode = True

languages = {
    "English":"en",
    "Hindi":"hi",
    "Telugu":"te",
    "Tamil":"ta",
    "Kannada":"kn",
    "Malayalam":"ml",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Japanese":"ja",
    "Korean":"ko",
    "Chinese (Simplified)":"zh-cn",
    "Russian":"ru",
    "Arabic":"ar",
    "Italian":"it",
    "Portuguese":"pt",
    "Urdu":"ur",
    "Turkish":"tr",
    "Dutch":"nl"
}

history = []

root = Tk()
root.title("AI Language Translator")
root.geometry("1200x850")
root.configure(bg=DARK_BG)
root.minsize(1000,750)

def update_status(msg):
    status.config(text=msg)

def filter_languages(event, combo):
    value = combo.get().lower()

    combo["values"] = [
        item for item in languages.keys()
        if value in item.lower()
    ]

def update_count(event=None):
    txt = input_text.get("1.0",END).strip()
    counter.config(text=f"Characters: {len(txt)}")

def translate_text():

    try:

        text = input_text.get("1.0",END).strip()

        if not text:
            messagebox.showerror("Error","Please enter text")
            return

        update_status("Detecting language...")

        translated = GoogleTranslator(
            source=languages[source_combo.get()],
            target=languages[target_combo.get()]
        ).translate(text)

        output_text.delete("1.0",END)
        output_text.insert(END,translated)

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        item = (
            f"[{timestamp}] "
            f"Auto ➜ {target_combo.get()} : "
            f"{translated}"
        )

        history.append(item)

        history_box.delete(0,END)

        for h in history[-50:]:
            history_box.insert(END,h)

        update_status("Translation Completed")

    except Exception as e:
        messagebox.showerror("Translation Error",str(e))


def voice_input_worker():
    try:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            update_status("Listening...")

            r.adjust_for_ambient_noise(source, duration=1)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        text = r.recognize_google(audio)

        input_text.delete("1.0", END)
        input_text.insert(END, text)

        update_status("Voice Captured")

    except sr.UnknownValueError:
        messagebox.showerror(
            "Voice Error",
            "Could not understand audio.\nPlease speak clearly."
        )

    except sr.RequestError:
        messagebox.showerror(
            "Voice Error",
            "No internet connection."
        )

    except Exception as e:
        messagebox.showerror(
            "Voice Error",
            str(e)
        )


def voice_input():
    threading.Thread(
        target=voice_input_worker,
        daemon=True
    ).start()
def speak_worker():

    try:

        text = output_text.get(
            "1.0",
            END
        ).strip()

        if not text:
            return

        filename = "voice.mp3"

        tts = gTTS(
            text=text,
            lang=languages[target_combo.get()]
        )

        tts.save(filename)

        os.system(f'start "" "{filename}"')

        update_status("Playing Audio")

    except Exception as e:

        messagebox.showerror(
            "Speech Error",
            str(e)
        )

def speak_text():

    threading.Thread(
        target=speak_worker,
        daemon=True
    ).start()

def copy_text():

    text = output_text.get(
        "1.0",
        END
    ).strip()

    if text:

        pyperclip.copy(text)

        update_status(
            "Copied"
        )

def clear_text():

    input_text.delete(
        "1.0",
        END
    )

    output_text.delete(
        "1.0",
        END
    )

    update_count()

    update_status(
        "Cleared"
    )

def save_translation():

    text = output_text.get(
        "1.0",
        END
    ).strip()

    if not text:
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File","*.txt")]
    )

    if file:

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(text)

        update_status("Saved")

def swap_languages():

    src = target_combo.get()

    target_combo.set(
        source_combo.get()
    )

    source_combo.set(src)

def clear_history():

    history.clear()

    history_box.delete(
        0,
        END
    )

def toggle_theme():

    global dark_mode

    if dark_mode:

        root.configure(bg=LIGHT_BG)

        input_text.config(
            bg=LIGHT_INPUT,
            fg="black",
            insertbackground="black"
        )

        output_text.config(
            bg=LIGHT_INPUT,
            fg="black",
            insertbackground="black"
        )

        history_box.config(
            bg="white",
            fg="black"
        )

        counter.config(
            bg=LIGHT_BG,
            fg="black"
        )

        status.config(
            bg="#DDDDDD",
            fg="black"
        )

        dark_mode = False

        update_status(
            "Light Mode"
        )

    else:

        root.configure(bg=DARK_BG)

        input_text.config(
            bg=DARK_INPUT,
            fg="white",
            insertbackground="white"
        )

        output_text.config(
            bg=DARK_INPUT,
            fg="white",
            insertbackground="white"
        )

        history_box.config(
            bg=DARK_HISTORY,
            fg="white"
        )

        counter.config(
            bg=DARK_BG,
            fg="white"
        )

        status.config(
            bg="#111827",
            fg="white"
        )

        dark_mode = True

        update_status(
            "Dark Mode"
        )

Label(
    root,
    text="AI LANGUAGE TRANSLATOR",
    font=("Segoe UI",28,"bold"),
    bg=DARK_BG,
    fg=ACCENT
).pack(pady=15)

input_text = Text(
    root,
    height=8,
    bg=DARK_INPUT,
    fg="white",
    font=("Arial",13)
)

input_text.pack(
    fill=BOTH,
    padx=20
)

input_text.bind(
    "<KeyRelease>",
    update_count
)

counter = Label(
    root,
    text="Characters: 0",
    bg=DARK_BG,
    fg="white"
)

counter.pack(pady=5)

lang_frame = Frame(
    root,
    bg=DARK_BG
)

lang_frame.pack(pady=10)

source_combo = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    width=25
)

source_combo.set("English")
source_combo.grid(row=0,column=0,padx=5)

source_combo.bind(
    "<KeyRelease>",
    lambda e: filter_languages(
        e,
        source_combo
    )
)

Button(
    lang_frame,
    text="⇄",
    command=swap_languages
).grid(row=0,column=1,padx=5)

target_combo = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    width=25
)

target_combo.set("Telugu")
target_combo.grid(row=0,column=2,padx=5)

target_combo.bind(
    "<KeyRelease>",
    lambda e: filter_languages(
        e,
        target_combo
    )
)

button_frame = Frame(
    root,
    bg=DARK_BG
)

button_frame.pack(pady=15)

buttons = [
    ("Translate",translate_text),
    ("Voice Input",voice_input),
    ("Speak",speak_text),
    ("Theme",toggle_theme),
    ("Copy",copy_text),
    ("Save",save_translation),
    ("Clear",clear_text)
]

for txt,cmd in buttons:

    Button(
        button_frame,
        text=txt,
        command=cmd,
        width=12
    ).pack(
        side=LEFT,
        padx=4
    )

output_text = Text(
    root,
    height=8,
    bg=DARK_INPUT,
    fg="white",
    font=("Arial",13)
)

output_text.pack(
    fill=BOTH,
    padx=20,
    pady=10
)

Label(
    root,
    text="Translation History",
    bg=DARK_BG,
    fg="white",
    font=("Segoe UI",12,"bold")
).pack()

history_box = Listbox(
    root,
    bg=DARK_HISTORY,
    fg="white"
)

history_box.pack(
    fill=BOTH,
    expand=True,
    padx=20,
    pady=10
)

Button(
    root,
    text="Clear History",
    command=clear_history
).pack()

status = Label(
    root,
    text="Ready",
    anchor=W,
    bg="#111827",
    fg="white"
)

status.pack(
    side=BOTTOM,
    fill=X
)

root.mainloop()
