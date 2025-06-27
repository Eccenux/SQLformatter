Program napisany w Pythonie z okienkiem GUI do wklejenia SQL i jego formatowania, używający `tkinter` oraz `sqlparse`.

## Jak uruchomić:

1. Zainstaluj/sprawdź `sqlparse`:

   ```bash
   python3 -m pip install sqlparse
   ```

2. Uruchom:

   ```bash
   python3 sql_formatter_gui.py
   ```

## Tworzenie wersji exe:

Jeśli chcesz wersję `.exe`:
```powershell
# raz (instalacja)
python3 -m pip install pyinstaller
# nowy exe
pyinstaller --onefile --noconsole sql_formatter_gui.py
```
