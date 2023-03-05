import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('チェックボタン簡易作成')

# チェックボタン簡易作成
chk = tkinter.Checkbutton(root, text='Pythonを使用する')
chk.place(x=50, y=70)

root.mainloop()




# Tkクラス生成
root2 = tkinter.Tk()
# 画面サイズ
root2.geometry('300x200')
# 画面タイトル
root2.title('チェックボタン基本編')

# チェックONにする
bln = tkinter.BooleanVar()
bln.set(True)

# チェックボタン基本編
chk = tkinter.Checkbutton(root2, variable=bln, text='Pythonを使用する')
chk.place(x=50, y=70)

root2.mainloop()




import tkinter

# Tkクラス生成
tki = tkinter.Tk()
# 画面サイズ
tki.geometry('300x200')
# 画面タイトル
tki.title('チェックボタン応用編')

# チェックボタンのラベルをリスト化する
chk_txt = ['Pythonを使用する','Javaを使用する','C#を使用する']
# チェックボックスON/OFFの状態
chk_bln = {}

# チェックボタンを動的に作成して配置
for i in range(len(chk_txt)):
    chk_bln[i] = tkinter.BooleanVar()
    chk = tkinter.Checkbutton(tki, variable=chk_bln[i], text=chk_txt[i]) 
    chk.place(x=50, y=30 + (i * 24))

# ボタンクリックイベント(チェック有無をセット)
def btn_click(bln):
    for i in range(len(chk_bln)):
        chk_bln[i].set(bln)

# ボタン作成 
btn = tkinter.Button(tki, text='ONにする', command=lambda:btn_click(True)) 
btn.place(x=80, y=170) 
btn = tkinter.Button(tki, text='OFFにする', command=lambda:btn_click(False)) 
btn.place(x=150, y=170)

tki.mainloop()