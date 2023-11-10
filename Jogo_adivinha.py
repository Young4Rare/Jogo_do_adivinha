import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Adivinhação")
        self.master.geometry("300x150")

        self.numero_secreto = random.randint(1, 10000)
        self.tentativas = 0
        self.max_tentativas = 10

        self.label = tk.Label(self.master, text="Tente adivinhar o número entre 1 e 10000.")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.master, text="Enviar Tentativa", command=self.fazer_tentativa)
        self.button.pack(pady=10)

        self.remaining_attempts_label = tk.Label(self.master, text=f"Tentativas restantes: {self.max_tentativas}")
        self.remaining_attempts_label.pack()

    def fazer_tentativa(self):
        try:
            tentativa = int(self.entry.get())
            self.tentativas += 1

            if tentativa == self.numero_secreto:
                messagebox.showinfo("Parabéns!", f"Você acertou em {self.tentativas} tentativa(s).")
                self.master.destroy()
            elif tentativa < self.numero_secreto:
                messagebox.showinfo("Tente Novamente", "Tente um número maior.")
            else:
                messagebox.showinfo("Tente Novamente", "Tente um número menor.")

            remaining_attempts = self.max_tentativas - self.tentativas
            self.remaining_attempts_label.config(text=f"Tentativas restantes: {max(0, remaining_attempts)}")

            if self.tentativas == self.max_tentativas:
                messagebox.showinfo("Fim de Jogo", f"Você atingiu o número máximo de tentativas. O número secreto era {self.numero_secreto}.")
                self.master.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
