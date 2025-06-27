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
```bash
pip install pyinstaller
pyinstaller --onefile sql_formatter_gui.py
```
