import tkinter as tk
from tkinter import messagebox
from login_logic import check_credentials

def on_login(event=None):
    user = entry_username.get().strip()
    pwd = entry_password.get()
    ok, reason = check_credentials(user, pwd)
    if ok:
        messagebox.showinfo("Login", "✅ Login Successful!")
    else:
        if reason == "empty_fields":
            messagebox.showwarning("Login", "Παρακαλώ συμπλήρωσε όλα τα πεδία.")
        else:
            messagebox.showerror("Login", "❌ Invalid credentials")

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_motion(event):
    dx = event.x - root.x
    dy = event.y - root.y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")

# Δημιουργία παραθύρου
root = tk.Tk()
root.overrideredirect(True)
root.geometry("320x220")
root.configure(bg="#39FF14")  # neon green

# Custom title bar
title_bar = tk.Frame(root, bg="#00FF00", relief="raised", bd=0, height=30)
title_bar.pack(fill=tk.X)
title_bar.bind("<Button-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_motion)

title_label = tk.Label(title_bar, text="Login Form", bg="#00FF00", fg="black")
title_label.pack(side=tk.LEFT, padx=5)

close_btn = tk.Button(title_bar, text="X", bg="#FF0000", fg="white", command=root.destroy, bd=0)
close_btn.pack(side=tk.RIGHT, padx=5)

# Hover effect για το X κουμπί
def on_close_enter(e):
    close_btn['bg'] = "#FF5555"
def on_close_leave(e):
    close_btn['bg'] = "#FF0000"

close_btn.bind("<Enter>", on_close_enter)
close_btn.bind("<Leave>", on_close_leave)

# Username / Password
tk.Label(root, text="Username:", bg="#39FF14", fg="black").pack(pady=(40,0))
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", bg="#39FF14", fg="black").pack(pady=(10,0))
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login button με hover effect
btn_login = tk.Button(root, text="Login", command=on_login, bg="#FFD700")
btn_login.pack(pady=15)

def on_login_enter(e):
    btn_login['bg'] = "#FFFF00"
def on_login_leave(e):
    btn_login['bg'] = "#FFD700"

btn_login.bind("<Enter>", on_login_enter)
btn_login.bind("<Leave>", on_login_leave)

# Enter key για login
root.bind('<Return>', on_login)

# Esc key για κλείσιμο
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()