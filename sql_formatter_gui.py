import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
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

def save_to_file():
	data = output_text.get("1.0", tk.END)
	file_path = filedialog.asksaveasfilename(defaultextension=".sql")
	if file_path:
		with open(file_path, "w", encoding="utf-8") as f:
			f.write(data)

def copy_to_clipboard():
	root.clipboard_clear()
	root.clipboard_append(output_text.get("1.0", tk.END))
	messagebox.showinfo("Schowek", "Sformatowany SQL skopiowany!")

# Główne okno
root = tk.Tk()
root.title("SQL Formatter")

# Pole do wklejenia SQL
input_label = tk.Label(root, text="Wklej SQL:")
input_label.pack()
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=5)
input_text.pack(fill=tk.BOTH, expand=True)

# Przycisk formatowania
format_button = tk.Button(root, text="Formatuj SQL", command=format_sql)
format_button.pack(pady=5)

# Pole na wynik
output_label = tk.Label(root, text="Sformatowany SQL:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
output_text.pack(fill=tk.BOTH, expand=True)

# Dodatkowe przyciski
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Zapisz do pliku", command=save_to_file).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Kopiuj do schowka", command=copy_to_clipboard).pack(side=tk.LEFT, padx=5)

# Uruchomienie GUI
root.geometry("800x600")

root.update_idletasks()  # aktualizacja wymiarów okna
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)  # centrowanie w poziomie
y = 0  # góra ekranu
root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
