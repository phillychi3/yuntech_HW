import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# 連接或創建資料庫
# 使用 'with' 語句確保在程式結束時資料庫會自動關閉
with sqlite3.connect('todo.db') as db:
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT '未完成'
        )
    ''')
    db.commit()

# 新增待辦事項
# 此函式從使用者介面獲取標題和描述並新增到資料庫
# 如果標題為空則顯示警告

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    if title:
        with sqlite3.connect('todo.db') as db:
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO tasks (title, description, status)
                VALUES (?, ?, ?)
            ''', (title, description, '未完成'))
            db.commit()
        entry_title.delete(0, tk.END)  # 清空輸入框
        entry_description.delete(0, tk.END)
        update_task_list()  # 更新顯示
    else:
        messagebox.showwarning("警告", "標題不能為空！")

# 刪除待辦事項
# 此函式刪除使用者選取的任務

def delete_task():
    selected_task = tree_tasks.selection()
    if selected_task:
        task_id = tree_tasks.item(selected_task)['values'][0]
        with sqlite3.connect('todo.db') as db:
            cursor = db.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            db.commit()
        update_task_list()
    else:
        messagebox.showwarning("警告", "請選擇要刪除的待辦事項！")

# 編輯待辦事項
# 此函式讓使用者編輯選取的任務

def edit_task():
    selected_task = tree_tasks.selection()  # 獲取使用者選取的任務
    if selected_task:
        task_values = tree_tasks.item(selected_task)['values']  # 獲取選取任務的所有值
        # 創建編輯視窗，供使用者更改選取的任務
        edit_window = tk.Toplevel(root)  # 創建新窗口作為編輯窗口
        edit_window.title("編輯待辦事項")
        # 新標題輸入框
        entry_edit_title = tk.Entry(edit_window, width=30)
        entry_edit_title.grid(row=0, column=1, padx=5, pady=5)
        entry_edit_title.insert(0, task_values[1])  # 將原標題填入輸入框，方便編輯
        # 新描述輸入框
        entry_edit_description = tk.Entry(edit_window, width=30)
        entry_edit_description.grid(row=1, column=1, padx=5, pady=5)
        entry_edit_description.insert(0, task_values[2])  # 將原描述填入輸入框
        # 狀態選擇框，允許更改狀態
        status_var = tk.StringVar(value=task_values[3])  # 設定初始值為原任務狀態
        status_options = ttk.Combobox(edit_window, textvariable=status_var, values=["未完成", "已完成"])
        status_options.grid(row=2, column=1, padx=5, pady=5)

        # 保存編輯後的任務
        def save_edit():
            new_title = entry_edit_title.get()
            new_description = entry_edit_description.get()
            new_status = status_var.get()
            if new_title:
                with sqlite3.connect('todo.db') as db:
                    cursor = db.cursor()
                    cursor.execute('''
                        UPDATE tasks
                        SET title = ?, description = ?, status = ?
                        WHERE id = ?
                    ''', (new_title, new_description, new_status, task_values[0]))
                    db.commit()
                update_task_list()
                edit_window.destroy()
            else:
                messagebox.showwarning("警告", "標題不能為空！")

        # 編輯視窗中的保存按鈕，按下後保存更改
        tk.Button(edit_window, text="保存", command=save_edit).grid(row=3, column=1, pady=10)
    else:
        # 如果未選擇任務，顯示警告訊息
        messagebox.showwarning("警告", "請選擇要編輯的待辦事項！")

# 更新待辦事項清單
# 此函式從資料庫中讀取所有任務並顯示在樹狀檢視表中

def update_task_list():
    tree_tasks.delete(*tree_tasks.get_children())
    with sqlite3.connect('todo.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM tasks')
        for task in cursor.fetchall():
            tree_tasks.insert('', 'end', values=task)

# 建立介面
root = tk.Tk()  # 創建主視窗
root.title("Todo List")
frame_main = tk.Frame(root)  # 創建主框架以容納輸入區域和按鈕
frame_main.pack(padx=10, pady=10)

# 標題輸入框
entry_title = tk.Entry(frame_main, width=30)  # 創建標題輸入框
entry_title.grid(row=0, column=1, padx=5, pady=5)  # 設定輸入框位置
# 描述輸入框
entry_description = tk.Entry(frame_main, width=30)  # 創建描述輸入框
entry_description.grid(row=1, column=1, padx=5, pady=5)  # 設定描述輸入框位置

# 標題和描述的標籤
# 這些標籤用來提示使用者輸入的內容
tk.Label(frame_main, text="標題:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_main, text="描述:").grid(row=1, column=0, padx=5, pady=5)

# 新增、刪除和編輯按鈕
# 新增任務按鈕，按下後會呼叫 add_task 函式
tk.Button(frame_main, text="新增", command=add_task).grid(row=2, column=0, pady=10)
# 刪除任務按鈕，按下後會呼叫 delete_task 函式
tk.Button(frame_main, text="刪除", command=delete_task).grid(row=2, column=1, pady=10)
# 編輯任務按鈕，按下後會呼叫 edit_task 函式
tk.Button(frame_main, text="編輯", command=edit_task).grid(row=2, column=2, pady=10)

# 建立樹狀檢視表以顯示任務
columns = ('ID', '標題', '描述', '狀態')  # 定義樹狀檢視表的列名
# 創建樹狀檢視表以顯示所有任務
tree_tasks = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree_tasks.heading(col, text=col)  # 設定每列的標題
    tree_tasks.column(col, width=100)  # 設定每列的寬度

# 顯示樹狀檢視表
tree_tasks.pack(padx=10, pady=10)

# 初次更新任務清單顯示，從資料庫中讀取並顯示任務
update_task_list()
root.mainloop()  # 啟動主視窗事件循環，使介面保持運行狀態
