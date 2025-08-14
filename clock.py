import tkinter as tk
from datetime import datetime

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.resizable(False, False)
        self.configure(bg="#111")

        self.is_24h = True

        self.time_label = tk.Label(self, font=("Consolas", 48, "bold"),
                                   fg="#00ff88", bg="#111")
        self.time_label.pack(padx=20, pady=(20, 5))

        self.date_label = tk.Label(self, font=("Consolas", 16),
                                   fg="#b0b0b0", bg="#111")
        self.date_label.pack(padx=20, pady=(0, 10))

        btn_frame = tk.Frame(self, bg="#111")
        btn_frame.pack(pady=(0, 20))

        self.toggle_btn = tk.Button(btn_frame, text="Switch to 12-hour",
                                    command=self.toggle_format, width=18)
        self.toggle_btn.pack(side=tk.LEFT, padx=5)

        self.quit_btn = tk.Button(btn_frame, text="Quit", command=self.destroy, width=10)
        self.quit_btn.pack(side=tk.LEFT, padx=5)

        self.update_clock()

    def toggle_format(self):
        self.is_24h = not self.is_24h
        self.toggle_btn.config(text="Switch to 24-hour" if not self.is_24h else "Switch to 12-hour")

    def update_clock(self):
        now = datetime.now()
        fmt = "%H:%M:%S" if self.is_24h else "%I:%M:%S %p"
        self.time_label.config(text=now.strftime(fmt).lstrip("0"))
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))
        self.after(200, self.update_clock)  # refresh ~5 times/sec for smoothness

if __name__ == "__main__":
    DigitalClock().mainloop()
