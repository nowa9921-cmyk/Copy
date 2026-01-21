import pyperclip
from tkinter import Tk, filedialog, messagebox
import sys

# Main hidden root
root = Tk()
root.withdraw()
root.title("EREN")

# File picker
file_path = filedialog.askopenfilename(
    title="EREN - Select TXT File",
    filetypes=[("Text Files","*.txt")]
)

if not file_path:
    sys.exit()

try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pyperclip.copy(text)
    messagebox.showinfo("EREN", "Text copied to clipboard ✔️")

except Exception as e:
    messagebox.showerror("EREN", f"Error:\n{e}")
