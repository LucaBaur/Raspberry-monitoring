import customtkinter
import sys

class Gui:
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.assistent = None

        self.root = customtkinter.CTk()
        self.root.geometry("500x350")
        self.root.protocol("WM_DELETE_WINDOW", self.stop_gui)
        self.root.title("Smart Home")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.head_label = customtkinter.CTkLabel(master=self.frame, text="Smart Home", font=("Roboto",24))
        self.head_label.pack(pady=12, padx=20)

        self.assistent_text = customtkinter.CTkLabel(master=self.frame, text="Texthalter", font=("Roboto",24))
        self.assistent_text.pack(pady=12, padx=20)

    def set_assistent(self, assistent):
        self.assistent = assistent

    def start_gui(self):
  
        def switch_event():
            print("switch toggled, current value:", switch_var.get())
            if switch_var.get() == "an":
                self.assistent.silent_assistent()
            else: 
                self.assistent.stop_assistent()

        switch_var = customtkinter.StringVar(value="an")
        switch = customtkinter.CTkSwitch(self.root, text="Spracherkennung", command=switch_event,
                                        variable=switch_var, onvalue="an", offvalue="aus")
        switch.pack(pady=12, padx=20)

        self.root.mainloop()
    
    def update_assistent_text(self, text):
        self.assistent_text.set(text)
    


    def stop_gui(self):
        self.root.destroy()
        sys.exit()  # Beendet das gesamte Programm
