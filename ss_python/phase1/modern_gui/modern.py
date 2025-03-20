import customtkinter as ctk 

# BASIC SETTINGS
ctk.set_appearance_mode("dark") #dark/sys/light
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

def login():
    print("Test")

#root element
frame = ctk.CTkFrame(master = root)
# we can also use grad but we'll use pack here
# vert padding is 20, horz is 60
frame.pack(pady = 20, padx = 60, fill=both, expand=True)

# add button and checkbox 
# adding to the frame not the root directly
label = ctk.CTkLabel(master = frame, text_font = ("Roboto", 240))
label.pack(pady = 12, padx = 10)

# username and password entries
#username entry
name_entry = ctk.CTkEntry(master = frame, placeholder_text = "Username")
#username appearance
name_entry.pack(pady = 12, padx = 10)

#password entry
pw_entry = ctk.CTKEntry(master = frame, placeholder_text = "Password", show = "*")
#password appearance
pw_entry.pack(pady = 12, padx = 10)

#login button
#connects to function "login"
login_btn = ctk.CTkButton(master = frame, text="Login", command=login)
#login button appearance
login_btn.pack(pady = 12, padx = 10)

#checkbox
btn_check = ctk.CTkCheckBox(master = frame, text="Remember Me")
#checkbox appearance

