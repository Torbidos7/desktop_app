import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Custom Tkinter")
root.geometry("500x500")

def login():
    print("Login")


frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Loggati", font=("Arial", 20))
label.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(frame, placeholder_text="username")
entry1.pack(pady=10, padx=10)

entry2 = customtkinter.CTkEntry(frame, placeholder_text="password", show="*")
entry2.pack(pady=10, padx=10)

button = customtkinter.CTkButton(frame, text="Login", command=login)
button.pack(pady=10, padx=10)

checkbox = customtkinter.CTkCheckBox(frame, text="Remember me")
checkbox.pack(pady=10, padx=10)

root.mainloop()