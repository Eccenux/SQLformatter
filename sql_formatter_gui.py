import tkinter as tk
from tkinter import scrolledtext, messagebox
import sqlparse

# Funkcja formatująca SQL
def format_sql():
	try:
		raw_sql = input_text.get("1.0", tk.END)
		formatted = sqlparse.format(raw_sql, reindent=True, keyword_case='upper')
		output_text.delete("1.0", tk.END)
		output_text.insert(tk.END, formatted)
	except Exception as e:
		messagebox.showerror("Błąd", str(e))

# Główne okno
root = tk.Tk()
root.title("SQL Formatter")

# Pole do wklejenia SQL
input_label = tk.Label(root, text="Wklej SQL:")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
input_text.pack(fill=tk.BOTH, expand=True)

# Przycisk formatowania
format_button = tk.Button(root, text="Formatuj SQL", command=format_sql)
format_button.pack(pady=10)

# Pole na wynik
output_label = tk.Label(root, text="Sformatowany SQL:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
output_text.pack(fill=tk.BOTH, expand=True)

# Uruchomienie GUI
root.geometry("800x800")
root.mainloop()
