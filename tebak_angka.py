import tkinter as tk
from tkinter import messagebox
import random

BG_COLOR = "#1a1a2e"
CARD_COLOR = "#16213e"
ACCENT_COLOR = "#0f3460"
BTN_COLOR = "#e94560"
BTN_HOVER = "#e7637e"
SUCCESS_COLOR = "#21e6c1"
TEXT_COLOR = "#f5f6fa"
ATTEMPT_COLOR = "#fddb3a"
WARNING_COLOR = "#f5f6fa"

class TebakAngka:
    def __init__(self, master):
        self.master = master
        master.title("Permainan Tebak Angka")
        master.attributes("-fullscreen", True)
        master.configure(bg=BG_COLOR)
        master.resizable(False, False)
        master.bind("<Escape>", self.keluar_fullscreen)
        self.card = tk.Frame(master, bg=CARD_COLOR, bd=0, highlightthickness=0)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=370, height=340)
        self.title_label = tk.Label(
            self.card, text="🎲 Permainan Tebak Angka 🎲",
            font=("Segoe UI", 19, "bold"), bg=CARD_COLOR, fg=SUCCESS_COLOR
        )
        self.title_label.pack(pady=(28, 6))
        self.sep1 = tk.Frame(self.card, height=2, bg=ACCENT_COLOR)
        self.sep1.pack(fill="x", padx=18, pady=(0, 12))
        self.instruction_label = tk.Label(
            self.card, text="Tebak angka antara 1 hingga 100:",
            font=("Segoe UI", 13), bg=CARD_COLOR, fg=TEXT_COLOR
        )
        self.instruction_label.pack(pady=(0, 7))
        row = tk.Frame(self.card, bg=CARD_COLOR)
        row.pack(pady=(0, 10))
        self.entry = tk.Entry(
            row, font=("Segoe UI", 15), width=8, justify="center", bd=2, relief="groove"
        )
        self.entry.pack(side="left", padx=(0, 10))
        self.entry.focus_set()
        self.entry.bind("<Return>", lambda e: self.cek_tebakan())
        self.guess_button = tk.Button(
            row, text="Tebak", font=("Segoe UI", 13, "bold"),
            bg=BTN_COLOR, fg="white", activebackground=BTN_HOVER, activeforeground="white",
            width=8, bd=0, cursor="hand2", command=self.cek_tebakan
        )
        self.guess_button.pack(side="left")
        self.guess_button.bind("<Enter>", lambda e: self.guess_button.config(bg=BTN_HOVER))
        self.guess_button.bind("<Leave>", lambda e: self.guess_button.config(bg=BTN_COLOR))
        self.result_label = tk.Label(
            self.card, text="", font=("Segoe UI", 14, "bold"),
            bg=CARD_COLOR, fg=BTN_COLOR
        )
        self.result_label.pack(pady=(6, 0))
        self.attempts_label = tk.Label(
            self.card, text="Percobaan: 0", font=("Segoe UI", 12, "bold"),
            bg=CARD_COLOR, fg=ATTEMPT_COLOR
        )
        self.attempts_label.pack(pady=(5, 0))
        self.sep2 = tk.Frame(self.card, height=1, bg=ACCENT_COLOR)
        self.sep2.pack(fill="x", padx=20, pady=(17, 10))
        self.reset_button = tk.Button(
            self.card, text="Ulang Permainan", font=("Segoe UI", 11, "bold"),
            bg=ACCENT_COLOR, fg="white", activebackground=BTN_COLOR, activeforeground="white",
            width=16, bd=0, cursor="hand2", command=self.ulang_permainan
        )
        self.reset_button.pack(pady=(0, 0))
        self.reset_button.bind("<Enter>", lambda e: self.reset_button.config(bg=BTN_COLOR))
        self.reset_button.bind("<Leave>", lambda e: self.reset_button.config(bg=ACCENT_COLOR))
        self.footer = tk.Label(
            self.card, text="oleh ryanazryan", font=("Segoe UI", 9), bg=CARD_COLOR, fg="#888"
        )
        self.footer.pack(side="bottom", pady=(10, 0))
        self.ulang_permainan()

    def keluar_fullscreen(self, event=None):
        self.master.attributes("-fullscreen", False)

    def cek_tebakan(self):
        try:
            tebakan = int(self.entry.get())
            if not (1 <= tebakan <= 100):
                self.result_label.config(text="Isi 1-100", fg=WARNING_COLOR, bg=CARD_COLOR)
                return
            self.attempts += 1
            self.attempts_label.config(text=f"Percobaan: {self.attempts}")
            if tebakan < self.angka_rahasia:
                self.result_label.config(text="Terlalu kecil", fg=BTN_COLOR)
            elif tebakan > self.angka_rahasia:
                self.result_label.config(text="Terlalu besar", fg=BTN_COLOR)
            else:
                self.result_label.config(text="", fg=SUCCESS_COLOR)
                self.tampil_dialog_menang()
        except ValueError:
            self.result_label.config(text="Isi angka", fg=WARNING_COLOR, bg=CARD_COLOR)
        finally:
            self.entry.delete(0, tk.END)
            self.entry.focus_set()

    def tampil_dialog_menang(self):
        msg = f"🎉 Benar!\nKamu menebak angka dalam {self.attempts} percobaan."
        messagebox.showinfo("Selamat!", msg)
        self.ulang_permainan()

    def ulang_permainan(self):
        self.angka_rahasia = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg=BTN_COLOR)
        self.attempts_label.config(text="Percobaan: 0")
        self.entry.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = TebakAngka(root)
    root.mainloop()