import tkinter as tk
from tkinter import messagebox
from ai_engine import get_ai_move
from utils import is_complete_word, is_valid_fragment
import random

# Baca file kamus
with open("kamus.txt") as f:
    WORD_LIST = [w.strip() for w in f if len(w.strip()) >= 4]

class GhostWordGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Ghost Word Game")
        self.master.geometry("400x500")  # Set window size to 2x the original
        self.master.configure(bg="#D8F3B5")  # Set background color to bottle green

        self.fragment = ""
        self.turn = random.choice(["user", "ai"])

        self.label_fragment = tk.Label(master, text=f"Masukan kata! '{self.fragment}'", bg="#D8F3B5", font=("Times new roman", 24))
        self.label_fragment.pack(pady=20)

        self.entry_letter = tk.Entry(master, font=("Arial", 24))
        self.entry_letter.pack(pady=20)

        self.button_submit = tk.Button(master, text="Submit", command=self.submit_letter, font=("Arial", 24))
        self.button_submit.pack(pady=20)

        self.label_turn = tk.Label(master, text=f"Giliran: {self.turn.upper()}", bg="#D8F3B5", font=("Arial", 24))
        self.label_turn.pack(pady=20)

        self.message = tk.Label(master, text="", bg="#D8F3B5", font=("Arial", 24))
        self.message.pack(pady=20)

    def submit_letter(self):
        letter = self.entry_letter.get().lower()
        self.entry_letter.delete(0, tk.END)

        if not (letter.isalpha() and len(letter) == 1):
            self.message.config(text="Masukan hanya satu huruf a-z!")
            return

        self.fragment += letter

        # Cek apakah USER kalah
        if is_complete_word(self.fragment, WORD_LIST) and len(self.fragment) >= 4:
            self.end_game(f"'{self.fragment}' adalah kata lengkap. USER kalah!")
            return
        if not is_valid_fragment(self.fragment, WORD_LIST):
            self.end_game(f"'{self.fragment}' tidak bisa membentuk kata valid. USER kalah!")
            return

        self.turn = "ai"
        self.ai_turn()

    def ai_turn(self):
        letter = get_ai_move(self.fragment, WORD_LIST)
        self.fragment += letter
        self.label_fragment.config(text=f"Fragment sekarang: '{self.fragment}'")

        # Cek apakah AI kalah
        if is_complete_word(self.fragment, WORD_LIST) and len(self.fragment) >= 4:
            self.end_game(f"'{self.fragment}' adalah kata lengkap. AI kalah!")
            return
        if not is_valid_fragment(self.fragment, WORD_LIST):
            self.end_game(f"'{self.fragment}' tidak bisa membentuk kata valid. AI kalah!")
            return

        self.turn = "user"
        self.label_turn.config(text=f"Giliran: {self.turn.upper()}")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.fragment = ""
        self.turn = random.choice(["user", "ai"])
        self.label_fragment.config(text=f"Fragment sekarang: '{self.fragment}'")
        self.label_turn.config(text=f"Giliran: {self.turn.upper()}")
        self.message.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GhostWordGame(root)
    root.mainloop()
