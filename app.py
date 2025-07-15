import tkinter as tk
from tkinter import messagebox
import random

def generate_numbers():
    # Generowanie 6 losowych liczb od 1 do 9
    generated_numbers = [random.randint(0, 9) for _ in range(6)]

    # Wyświetlanie wygenerowanych liczb bez przecinków obok siebie
    result_label.config(text="".join(map(str, generated_numbers)))

    # Zapisanie wygenerowanego ciągu liczb do zmiennej globalnej
    global generated_numbers_text
    generated_numbers_text = "".join(map(str, generated_numbers))


def copy_to_clipboard():
    # Kopiowanie wygenerowanego ciągu liczb do schowka
    window.clipboard_clear()
    window.clipboard_append(generated_numbers_text)
    window.update()

    # Wyświetlenie komunikatu o skopiowaniu
    messagebox.showinfo("Skopiowano", "Wygenerowane liczby zostały skopiowane do schowka.")


# Tworzenie głównego okna
window = tk.Tk()
window.geometry("300x200")
window.title("Generator i Kopiowanie Liczb")

# Przycisk do generowania liczb
generate_button = tk.Button(window, text="Generuj liczby", command=generate_numbers)
generate_button.pack(pady=10)

# Przycisk do kopiowania liczb do schowka
copy_button = tk.Button(window, text="Skopiuj do schowka", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Etykieta do wyświetlania wygenerowanych liczb
result_label = tk.Label(window, text="")
result_label.pack()

# Zmienna przechowująca wygenerowany ciąg liczb
generated_numbers_text = ""

# Uruchomienie pętli głównej
window.mainloop()