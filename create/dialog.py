#（１）メッセージボックス（messagebox.py #1）

import tkinter as tk
import tkinter.messagebox as messagebox

tk.Tk().withdraw()
messagebox.showinfo('メッセージ', '処理が完了しました。')



#（２）選択ダイアログ（messagebox.py #6）

import tkinter as tk
import tkinter.messagebox as messagebox

tk.Tk().withdraw()
messagebox.askokcancel('質問', '処理を続行しますか？')



#（３）入力ダイアログ

import tkinter as tk
import tkinter.simpledialog as simpledialog

tk.Tk().withdraw()
password = simpledialog.askstring('パスワード入力', 'パスワードを入力してください')



#（４）ファイル選択ダイアログ（filedialog.py）

import tkinter as tk
import tkinter.filedialog as filedialog

tk.Tk().withdraw()
filepath = filedialog.askopenfilename()