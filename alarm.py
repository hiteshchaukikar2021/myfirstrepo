#adding alarm feature 

import tkinter as tk
from datetime import datetime
import threading
import time
import winsound  # works on Windows; for Linux/Mac, use `playsound`

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock with Alarm")
        self.resizable(False, False)
        self.configure(bg="#111")

        self.is_24h = True
        self.alarm_time = None
        self.alarm_set = False

        # Clock label
        self.time_label = tk.Label(self, font=("Consolas", 48, "bold"),
                                   fg="#00ff88", bg="#111")
        self.time_label.pack(padx=20, pady=(20, 5))

        # Date label
        self.date_label = tk.Label(self, font=("Consolas", 16),
                                   fg="#b0b0b0", bg="#111")
        self.date_label.pack(padx=20, pady=(0, 10))

        # Alarm input
        alarm_frame = tk.Frame(self, bg="#111")
        alarm_frame.pack(pady=(0, 10))
        tk.Label(alarm_frame, text="Set Alarm (HH:MM):", fg="#fff", bg="#111").pack(side=tk.LEFT)
        self.alarm_entry = tk.Entry(alarm_frame, width=8)
        self.alarm_entry.pack(side=tk.LEFT, padx=5)

        # Buttons
        btn_frame = tk.Frame(self, bg="#111")
        btn_frame.pack(pady=(0, 20))

        tk.Button(btn_frame, text="Set Alarm", command=self.set_alarm).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear Alarm", command=self.clear_alarm).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Switch Format", command=self.toggle_format).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Quit", command=self.destroy).pack(side=tk.LEFT, padx=5)

        # Start clock update
        self.update_clock()

    def toggle_format(self):
        self.is_24h = not self.is_24h

    def set_alarm(self):
        self.alarm_time = self.alarm_entry.get().strip()
        if self.alarm_time:
            self.alarm_set = True
            print(f"Alarm set for {self.alarm_time}")

    def clear_alarm(self):
        self.alarm_set = False
        self.alarm_time = None
        print("Alarm cleared.")

    def update_clock(self):
        now = datetime.now()
        fmt = "%H:%M:%S" if self.is_24h else "%I:%M:%S %p"
        current_time = now.strftime(fmt).lstrip("0")
        self.time_label.config(text=current_time)
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))

        # Check alarm
        if self.alarm_set:
            current_hm = now.strftime("%H:%M")
            if current_hm == self.alarm_time:
                self.alarm_set = False
                threading.Thread(target=self.play_alarm, daemon=True).start()

        self.after(500, self.update_clock)

    def play_alarm(self):
        for _ in range(5):  # play 5 times
            winsound.Beep(1000, 500)  # frequency, duration
            time.sleep(0.5)

if __name__ == "__main__":
    AlarmClock().mainloop()

