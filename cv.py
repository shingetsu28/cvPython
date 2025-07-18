import customtkinter as ctk
from PIL import Image
import webbrowser

# Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("720x480")
app.title("CV")

# Load images for icons (adjust file paths accordingly)
icon_size = (24, 24)  # size of your icons

icon_codeberg = ctk.CTkImage(Image.open("codeberg.png").resize(icon_size))
icon_github = ctk.CTkImage(Image.open("github.png").resize(icon_size))
icon_linkedin = ctk.CTkImage(Image.open("linkedin.png").resize(icon_size))
icon_about = ctk.CTkImage(Image.open("aboutme.png").resize(icon_size))
icon_home = ctk.CTkImage(Image.open("home.png").resize(icon_size))

# Frame switching function
def show_frame(frame):
    for f in pages:
        f.grid_forget()
    frame.grid(row=0, column=1, sticky="nsew")

# Sidebar frame
sidebar = ctk.CTkFrame(app, width=150)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)

# Buttons with icons
btn_codeberg = ctk.CTkButton(sidebar, text="Codeberg", image=icon_codeberg, compound="left",
                             command=lambda: webbrowser.open("https://codeberg.org/shingetsu28"))
btn_codeberg.pack(pady=(20, 10), fill="x", padx=10)

btn_github = ctk.CTkButton(sidebar, text="GitHub", image=icon_github, compound="left",
                           command=lambda: webbrowser.open("https://github.com/shingetsu28"))
btn_github.pack(pady=10, fill="x", padx=10)

btn_linkedin = ctk.CTkButton(sidebar, text="LinkedIn", image=icon_linkedin, compound="left",
                             command=lambda: webbrowser.open("https://linkedin.com/in/baran-arslan-902868374"))
btn_linkedin.pack(pady=10, fill="x", padx=10)

btn_about = ctk.CTkButton(sidebar, text="About Me", image=icon_about, compound="left",
                          command=lambda: show_frame(about_page))
btn_about.pack(pady=(30, 10), fill="x", padx=10)

btn_home = ctk.CTkButton(sidebar, text="Home", image=icon_home, compound="left",
                         command=lambda: show_frame(main_page))
btn_home.pack(pady=(10, 10), fill="x", padx=10)

# Pages
main_page = ctk.CTkFrame(app)
about_page = ctk.CTkFrame(app)

pages = [main_page, about_page]

# Main Page Content
label_main = ctk.CTkLabel(main_page, text="Azmi Baran ARSLAN \n2025 \nCV", font=("Arial", 22))
label_main.pack(pady=40)

# About Me Page Content
label_about = ctk.CTkLabel(about_page, text="Hello, I'm Baran. I made my cv into a python application." \
"Don't ask me why. I guess I was just bored." \
"I know no one would genuinely trust someone with an .exe but honestly it's a cool trick." \
"Maybe I'll turn this into a website someday.", font=("Arial", 18), wraplength=400)
label_about.pack(pady=40)

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

show_frame(main_page)

app.mainloop()
