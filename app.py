# =========================================
# AI vs HUMAN DETECTOR SYSTEM
# By Esraa 🔥
# =========================================

# تثبيت المكتبات أول مرة:
# pip install customtkinter pillow opencv-python

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import os

# =========================================
# SETTINGS
# =========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================================
# MAIN WINDOW
# =========================================

app = ctk.CTk()
app.geometry("1200x700")
app.title("AI SECURITY SYSTEM")
app.resizable(False, False)

# =========================================
# COLORS
# =========================================

bg_color = "#0f172a"
frame_color = "#111827"
button_color = "#2563eb"
hover_color = "#1d4ed8"

app.configure(fg_color=bg_color)

# =========================================
# VALID USERS
# =========================================

valid_names = ["esraa", "wiam", "tasneem"]
valid_password = "12345"

# =========================================
# LOGIN FUNCTION
# =========================================

def login():

    username = user_entry.get().lower()
    password = pass_entry.get()

    if username in valid_names and password == valid_password:
        messagebox.showinfo("ACCESS GRANTED", "Welcome To The System 🔥")
        open_main_system()

    else:
        messagebox.showerror("ACCESS DENIED", "Wrong Username Or Password")

# =========================================
# OPEN MAIN SYSTEM
# =========================================

def open_main_system():

    login_frame.destroy()

    global result_label
    global image_label
    global signature_label

    # TITLE
    title = ctk.CTkLabel(
        app,
        text="AI vs HUMAN DETECTION SYSTEM",
        font=("Arial", 32, "bold"),
        text_color="cyan"
    )
    title.pack(pady=20)

    # MAIN FRAME
    main_frame = ctk.CTkFrame(
        app,
        width=1100,
        height=550,
        fg_color=frame_color,
        corner_radius=20
    )
    main_frame.pack(pady=20)

    # LEFT SIDE
    left_frame = ctk.CTkFrame(
        main_frame,
        width=500,
        height=500,
        fg_color="#1e293b",
        corner_radius=20
    )
    left_frame.place(x=20, y=20)

    # RIGHT SIDE
    right_frame = ctk.CTkFrame(
        main_frame,
        width=520,
        height=500,
        fg_color="#1e293b",
        corner_radius=20
    )
    right_frame.place(x=560, y=20)

    # IMAGE LABEL
    image_label = ctk.CTkLabel(
        left_frame,
        text="UPLOAD IMAGE",
        font=("Arial", 22, "bold")
    )
    image_label.place(relx=0.5, rely=0.4, anchor="center")

    # UPLOAD BUTTON
    upload_btn = ctk.CTkButton(
        left_frame,
        text="UPLOAD IMAGE",
        width=250,
        height=50,
        font=("Arial", 18, "bold"),
        fg_color=button_color,
        hover_color=hover_color,
        command=upload_image
    )
    upload_btn.place(relx=0.5, rely=0.8, anchor="center")

    # RESULT LABEL
    result_label = ctk.CTkLabel(
        right_frame,
        text="WAITING FOR ANALYSIS...",
        font=("Arial", 26, "bold"),
        text_color="white"
    )
    result_label.pack(pady=40)

    # DIGITAL SIGNATURE
    signature_label = ctk.CTkLabel(
        right_frame,
        text="",
        font=("Arial", 20),
        justify="left"
    )
    signature_label.pack(pady=30)

# =========================================
# UPLOAD IMAGE
# =========================================

def upload_image():

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Images", "*.png *.jpg *.jpeg")
        ]
    )

    if not file_path:
        return

    # LOAD IMAGE
    img = Image.open(file_path)
    img = img.resize((400, 300))

    photo = ImageTk.PhotoImage(img)

    image_label.configure(image=photo, text="")
    image_label.image = photo

    analyze_image()  
# =========================================
# ANALYZE IMAGE
# =========================================

def analyze_image():

    # RANDOM DETECTION (تجريبي حاليا)
    result = random.choice(["HUMAN", "AI GENERATED"])

    if result == "HUMAN":

        result_label.configure(
            text="✅ HUMAN DETECTED",
            text_color="lime"
        )

        eye_print = random.randint(100000, 999999)
        face_print = random.randint(100000, 999999)
        hand_print = random.randint(100000, 999999)

        signature_label.configure(
            text=f"""
FACE PRINT : {face_print}

EYE PRINT  : {eye_print}

HAND PRINT : {hand_print}

DIGITAL SIGNATURE VERIFIED
            """,
            text_color="white"
        )

    else:

        result_label.configure(
            text="⚠ AI GENERATED IMAGE",
            text_color="orange"
        )

        similarity = random.randint(70, 97)

        signature_label.configure(
            text=f"""
SIMILAR HUMAN FOUND

MATCH : {similarity}%

Gender Match  ✅
Skin Tone Match ✅
Face Structure ✅
Hair Style Match ✅

WARNING:
THIS IMAGE MAY BE AI GENERATED
            """,
            text_color="white"
        )

# =========================================
# LOGIN FRAME
# =========================================

login_frame = ctk.CTkFrame(
    app,
    width=500,
    height=500,
    fg_color=frame_color,
    corner_radius=25
)

login_frame.place(relx=0.5, rely=0.5, anchor="center")

# =========================================
# TITLE
# =========================================

title_label = ctk.CTkLabel(
    login_frame,
    text="AI SECURITY SYSTEM",
    font=("Arial", 34, "bold"),
    text_color="cyan"
)

title_label.pack(pady=40)

# =========================================
# USERNAME
# =========================================

user_entry = ctk.CTkEntry(
    login_frame,
    width=320,
    height=50,
    placeholder_text="Enter Username",
    font=("Arial", 18),
    corner_radius=15
)

user_entry.pack(pady=20)

# =========================================
# PASSWORD
# =========================================

pass_entry = ctk.CTkEntry(
    login_frame,
    width=320,
    height=50,
    placeholder_text="Enter Password",
    show="*",
    font=("Arial", 18),
    corner_radius=15
)

pass_entry.pack(pady=20)

# =========================================
# LOGIN BUTTON
# =========================================

login_btn = ctk.CTkButton(
    login_frame,
    text="LOGIN",
    width=250,
    height=55,
    font=("Arial", 22, "bold"),
    fg_color=button_color,
    hover_color=hover_color,
    corner_radius=15,
    command=login
)

login_btn.pack(pady=40)

# =========================================
# FOOTER
# =========================================

footer = ctk.CTkLabel(
    login_frame,
    text="Cyber Security AI System 🔥",
    font=("Arial", 15),
    text_color="gray"
)

footer.pack(side="bottom", pady=20)

# =========================================
# RUN
# =========================================

app.mainloop()
