import sqlite3
import tkinter as tk
import hashlib
from tkinter import messagebox

import os

thisfloder = os.path.dirname(__file__)


def init_db():
    conn = sqlite3.connect(os.path.join(thisfloder, "users.db"))
    c = conn.cursor()

    # 建立 users 資料表
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# 註冊使用者
def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        conn = sqlite3.connect(os.path.join(thisfloder, "users.db"))
        c = conn.cursor()

        c.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed_password),
        )

        conn.commit()
        conn.close()
        return True, "註冊成功！"

    except sqlite3.IntegrityError:
        return False, "該使用者名稱已存在！"
    except Exception as e:
        return False, f"註冊失敗：{str(e)}"


def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        conn = sqlite3.connect(os.path.join(thisfloder, "users.db"))
        c = conn.cursor()

        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = c.fetchone()

        conn.close()

        if user and user[0] == hashed_password:
            return True, "登入成功！"
        else:
            return False, "使用者名稱或密碼錯誤！"

    except Exception as e:
        return False, f"登入失敗：{str(e)}"


# 初始化資料庫
init_db()

# 建立 Tkinter 介面
root = tk.Tk()
root.title("會員管理系統")

# 使用者名稱輸入框
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

tk.Label(root, text="使用者名稱：").grid(row=0, column=0, padx=10, pady=5)
entry_username.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="密碼：").grid(row=1, column=0, padx=10, pady=5)
entry_password.grid(row=1, column=1, padx=10, pady=5)


# 顯示/隱藏密碼按鈕
def toggle_password_visibility():
    entry_password.config(show="" if entry_password.cget("show") == "*" else "*")


tk.Button(root, text="顯示/隱藏密碼", command=toggle_password_visibility).grid(
    row=1, column=2, padx=10, pady=5
)


# 註冊功能
def register():
    username, password = entry_username.get(), entry_password.get()
    if not username or not password:
        messagebox.showwarning("警告", "請輸入使用者名稱和密碼！")
        return
    success, message = register_user(username, password)
    messagebox.showinfo("成功", message) if success else messagebox.showerror(
        "錯誤", message
    )
    if success:
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)


# 登入功能
def login():
    username, password = entry_username.get(), entry_password.get()
    if not username or not password:
        messagebox.showwarning("警告", "請輸入使用者名稱和密碼！")
        return
    success, message = login_user(username, password)
    label_result.config(text=message, fg="green" if success else "red")


# 註冊和登入按鈕
tk.Button(root, text="註冊", command=register).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="登入", command=login).grid(row=2, column=1, padx=10, pady=10)

# 登入結果標籤
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# 啟動介面
root.mainloop()
