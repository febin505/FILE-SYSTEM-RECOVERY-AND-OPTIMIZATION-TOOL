import tkinter as tk
from tkinter import messagebox, filedialog
import os
import shutil

PATH = "test_directory"
TRASH = "test_directory/.trash"
RECOVERED = "recovered_files"

os.makedirs(TRASH, exist_ok=True)
os.makedirs(RECOVERED, exist_ok=True)

def delete_file():
    file_path = filedialog.askopenfilename(initialdir=PATH)
    if file_path:
        shutil.move(file_path, TRASH)
        messagebox.showinfo("Delete", "File moved to trash")

def recover_files():

    
    files = os.listdir(TRASH)
    if not files:
        messagebox.showinfo("Recover", "No files to recover")
        return

    for f in files:
        shutil.move(os.path.join(TRASH, f), os.path.join(RECOVERED, f))

    messagebox.showinfo("Recover", "Files recovered successfully")

def list_deleted_files():
    win = tk.Toplevel()
    win.title("Deleted Files")
    win.geometry("300x250")

    tk.Label(win, text="Deleted Files (Trash)", font=("Arial", 12)).pack(pady=10)

    listbox = tk.Listbox(win, width=40)
    listbox.pack(padx=10, pady=10)

    files = os.listdir(TRASH)
    if not files:
        listbox.insert(tk.END, "No deleted files")
    else:
        for f in files:
            listbox.insert(tk.END, f)

def list_recovered_files():
    win = tk.Toplevel()
    win.title("Recovered Files")
    win.geometry("300x250")

    tk.Label(win, text="Recovered Files", font=("Arial", 12)).pack(pady=10)

    listbox = tk.Listbox(win, width=40)
    listbox.pack(padx=10, pady=10)

    files = os.listdir(RECOVERED)
    if not files:
        listbox.insert(tk.END, "No recovered files")
    else:
        for f in files:
            listbox.insert(tk.END, f)

root = tk.Tk()
root.title("File System Recovery & Optimization Tool")
root.geometry("440x380")

tk.Label(root, text="File System Tool", font=("Arial", 16)).pack(pady=15)

tk.Button(root, text="Delete File", width=30, command=delete_file).pack(pady=5)
tk.Button(root, text="Recover Files", width=30, command=recover_files).pack(pady=5)
tk.Button(root, text="List Deleted Files", width=30, command=list_deleted_files).pack(pady=5)
tk.Button(root, text="List Recovered Files", width=30, command=list_recovered_files).pack(pady=5)
tk.Button(root, text="Optimize File System", width=30).pack(pady=5)
tk.Button(root, text="Analyze File System", width=30).pack(pady=5)

root.mainloop()
