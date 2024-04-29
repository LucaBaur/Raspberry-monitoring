import threading
import gui
import assistent

gui_instance = gui.Gui()  # Create an instance of the Gui class
assistent_instance = assistent.Assistent(gui=gui_instance)  # Create
gui_instance.set_assistent(assistent_instance)  # Set the assistant instance in the GUI

def start_gui_instance():
    gui_instance.start_gui() # Start the GUI

def start_assistant_instance():
    assistent_instance.start_assistent() # Start the assistant

if __name__ == "__main__":
    # Create a new thread for the assistant
    assistant_thread = threading.Thread(target=start_assistant_instance)
    assistant_thread.daemon = True
    assistant_thread.start()

    start_gui_instance()  # Start the GUI  

    
