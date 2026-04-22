import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import os

LOG_FILE = "keystrokes.log"


class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keystroke Logger (In-App Only)")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.is_logging = False

        # Title
        title = tk.Label(root, text="Keystroke Logger", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Status
        self.status_label = tk.Label(root, text="Status: OFF", fg="red")
        self.status_label.pack()

        # Input field
        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Log display
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=10)
        self.log_area.pack(pady=10)
        self.log_area.config(state='disabled')

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.start_btn = tk.Button(btn_frame, text="Start", width=10, command=self.start_logging)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=10, command=self.stop_logging)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear", width=10, command=self.clear_log)
        self.clear_btn.grid(row=0, column=2, padx=5)

        self.save_btn = tk.Button(btn_frame, text="Save Log", width=10, command=self.show_path)
        self.save_btn.grid(row=0, column=3, padx=5)

        # Bind keys
        root.bind("<Key>", self.log_key)

    def log_key(self, event):
        if not self.is_logging:
            return

        key = event.keysym
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {key}"

        # Write to file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

        # Show in UI
        self.log_area.config(state='normal')
        self.log_area.insert(tk.END, log_entry + "\n")
        self.log_area.config(state='disabled')
        self.log_area.yview(tk.END)

    def start_logging(self):
        self.is_logging = True
        self.status_label.config(text="Status: ON", fg="green")

    def stop_logging(self):
        self.is_logging = False
        self.status_label.config(text="Status: OFF", fg="red")

    def clear_log(self):
        self.log_area.config(state='normal')
        self.log_area.delete(1.0, tk.END)
        self.log_area.config(state='disabled')

    def show_path(self):
        path = os.path.abspath(LOG_FILE)
        messagebox.showinfo("Log File Location", f"Saved at:\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()