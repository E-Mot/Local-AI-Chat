import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import threading
from app_logic import user_prompt_stream

# --------------------------------------------------------------------------------------------------------#
# ------------------------------------------UI-Specific Logic------------------------------------------#
# --------------------------------------------------------------------------------------------------------#

logo_icon = None
chat_icon_path = None
chat_icon_img = None
user_icon_path = None
user_icon_img = None
placeholder = "Type a question"
bubble_labels = []
bubble_frames = []

def resource_path(filename):
    """Get absolute path to resource (works in dev + PyInstaller onefile)."""
    if hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base, filename)

def load_assets():
    global logo_icon, chat_icon_path, chat_icon_img, user_icon_path, user_icon_img

    logo_icon = resource_path("logo.ico")
    chat_icon_path = resource_path("logo.png")
    user_icon_path = resource_path("user.png")

    img1 = Image.open(chat_icon_path).resize((30, 30), Image.LANCZOS)
    chat_icon_img = ImageTk.PhotoImage(img1)

    img2 = Image.open(user_icon_path).resize((25, 25), Image.LANCZOS)
    user_icon_img = ImageTk.PhotoImage(img2)

def append_to_label(label, text):
    label.config(text=label.cget("text") + text)
    chat_box.see(tk.END)

def stream_ai_into_label(prompt, label):
    for piece in user_prompt_stream(prompt):
        root_window.after(0, append_to_label, label, piece)

def on_chat_resize(event=None):
    available = chat_box.winfo_width() - 200

    for lbl in bubble_labels:
        lbl.config(wraplength=available)

def on_mousewheel(event):
    chat_box.yview_scroll(int(-1 * (event.delta / 120)), "units")
    return "break"

def insert_newline(event):
    user_prompt.insert("insert", "\n")
    return "break"

def clear_placeholder(event=None):
    current = user_prompt.get("1.0", "end-1c")
    if current == placeholder:
        user_prompt.delete("1.0", tk.END)
        user_prompt.config(fg="black")

def restore_placeholder(event=None):
    current = user_prompt.get("1.0", "end-1c")
    if not current.strip():
        user_prompt.insert("1.0", placeholder)
        user_prompt.config(fg="gray")

def erase_chat():
    chat_box.config(state="normal")
    chat_box.delete("1.0", tk.END)
    chat_box.config(state="disabled")

def ai_output(event=None):
    global user_icon_img, chat_icon_img

    prompt = user_prompt.get("1.0", "end-1c")

    if not prompt.strip() or prompt == placeholder:
        if event is not None:
            return "break"
        return

    chat_box.config(state="normal")

    chat_box.insert(tk.END, "\n")
    chat_box.insert(tk.END, " ")
    user_bubble = tk.Frame(chat_box, bg = "#eeeeee", pady=10)
    bubble_frames.append(user_bubble)
    user_image = tk.Label(user_bubble, image=user_icon_img, bg = "#eeeeee")
    user_image.pack(side=tk.LEFT, anchor=tk.NW, padx=(10,10))
    user_bubble.bind("<MouseWheel>", on_mousewheel)
    user_image.bind("<MouseWheel>", on_mousewheel)
    user_prefix = tk.Label(user_bubble, text="You said:", bg="#eeeeee", font=("Courier", 12, "bold"))
    user_prefix.pack(side=tk.LEFT, anchor="nw", pady=0)
    user_label = tk.Label(user_bubble, text=prompt, justify="left", wraplength=360, bg="#eeeeee",font=("Courier", 12))
    user_label.pack(side=tk.LEFT, anchor="nw", fill="x", pady=0, padx=(0,10))
    bubble_labels.append(user_label)
    user_label.bind("<MouseWheel>", on_mousewheel)
    chat_box.window_create(tk.END, window=user_bubble)

    chat_box.insert(tk.END, "\n\n")

    chat_box.insert(tk.END, " ")
    ai_bubble = tk.Frame(chat_box, bg = "#f1f7ff", pady=10)
    bubble_frames.append(ai_bubble)
    ai_image = tk.Label(ai_bubble, image=chat_icon_img, bg = "#f1f7ff")
    ai_image.pack(side=tk.LEFT, anchor=tk.NW, padx=(10,10))
    ai_bubble.bind("<MouseWheel>", on_mousewheel)
    ai_image.bind("<MouseWheel>", on_mousewheel)
    ai_prefix = tk.Label(ai_bubble, text="Desky said:", bg="#f1f7ff", font=("Courier", 12, "bold"))
    ai_prefix.pack(side=tk.LEFT, anchor="nw", pady=0)
    ai_label = tk.Label(ai_bubble, text="", justify="left", compound="left", wraplength=360, bg = "#f1f7ff", font=("Courier", 12))
    ai_label.pack(side=tk.LEFT, anchor="nw", fill="x", pady=0, padx=(0,10))
    bubble_labels.append(ai_label)
    ai_label.bind("<MouseWheel>", on_mousewheel)
    chat_box.window_create(tk.END, window=ai_bubble)
    chat_box.insert(tk.END, "\n")

    on_chat_resize()

    threading.Thread(target=stream_ai_into_label, args=(prompt, ai_label), daemon=True).start()

    chat_box.config(state="disabled")

    user_prompt.delete("1.0", tk.END)
    user_prompt.mark_set("insert", "1.0")
    user_prompt.see("1.0")
    user_prompt.focus_set()   

    chat_box.update_idletasks()
    chat_box.see(tk.END)

    if event is not None:
        return "break"

# --------------------------------------------------------------------------------------------------------#
# ----------------------------------------------Program UI------------------------------------------------#
# --------------------------------------------------------------------------------------------------------#

root_window = tk.Tk()
load_assets()
window_width = 500
window_height = 400
root_window.title("Desktop AI")
app_icon = tk.PhotoImage(file=chat_icon_path)
root_window.iconphoto(True, app_icon)
screen_width = root_window.winfo_screenwidth()
screen_height = root_window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
root_window.minsize(450,400)
root_window.maxsize(screen_width // 2,screen_height)
root_window.grid_rowconfigure(0, weight=1)
root_window.grid_rowconfigure(1, weight=1)
root_window.grid_rowconfigure(2, weight=1)
root_window.grid_rowconfigure(3, weight=5)
root_window.grid_columnconfigure(0, weight=1)

top_label = tk.Label(root_window, text="Your Local Desktop AI", fg="#2d2d2d", font=("Nyla", 15, "bold"))
top_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20,20))

user_prompt = tk.Text(root_window,height=2,relief="flat",wrap="word",font=("Courier", 12), highlightthickness=1, highlightbackground="#c7c7c7", highlightcolor="#c7c7c7")
user_prompt.grid(row=1, column=0, sticky="nsew", padx=20, pady=0)
user_prompt.bind("<Return>", ai_output)
user_prompt.bind("<Shift-Return>", insert_newline)
user_prompt.insert("1.0", placeholder)
user_prompt.config(fg="gray")
user_prompt.bind("<FocusIn>", clear_placeholder)
user_prompt.bind("<FocusOut>", restore_placeholder)

buttons_frame=tk.Frame(root_window)
buttons_frame.grid(row=2, column=0, pady=(10,10))

submit_button = tk.Button(buttons_frame, command=ai_output, width=20, height=2, text="Submit", font=("Nyla", 10, "bold"), relief="flat", bg="#a9a9a9", fg="#ffffff", bd=0)
submit_button.configure(activebackground="#c8c8c8", activeforeground="#ffffff")
submit_button.grid(row=0, column=0, padx=(0,30), pady=(10,10))
submit_button.grid_propagate(False)

erase_convo = tk.Button(buttons_frame, command=erase_chat, width=20, height=2, text="Reset Conversation", font=("Nyla", 10, "bold"), relief="flat", bg="#a9a9a9", fg="#ffffff", bd=0)
erase_convo.configure(activebackground="#c8c8c8", activeforeground="#ffffff")
erase_convo.grid(row=0, column=1, padx=(30,0), pady=(10,10))
erase_convo.grid_propagate(False)

chat_frame = tk.Frame(root_window, highlightthickness=1, highlightbackground="#c7c7c7", highlightcolor="#c7c7c7")
chat_frame.grid(row=3, column=0, sticky="nsew", padx=20, pady=(0,20))
chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)

chat_box = tk.Text(chat_frame, relief="flat", wrap="word", height=8)
chat_box.grid(row=0, column=0, sticky="nsew", padx=0)
chat_box.config(state="disabled")
chat_box.bind("<Configure>", on_chat_resize)

scrollbar = tk.Scrollbar(chat_frame, orient="vertical", command=chat_box.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
chat_box.config(yscrollcommand=scrollbar.set)


if __name__ == "__main__":
    root_window.mainloop()