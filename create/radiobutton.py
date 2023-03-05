import tkinter, tkinter.messagebox

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('ラジオボタン簡易作成')

# ラジオボタン簡易作成
rdo1 = tkinter.Radiobutton(root, text='Apple')
rdo1.place(x=70, y=40)

rdo2 = tkinter.Radiobutton(root, text='Amazon')
rdo2.place(x=70, y=70)

rdo3 = tkinter.Radiobutton(root, text='Google')
rdo3.place(x=70, y=100)

root.mainloop()


# Tkクラス生成
root2 = tkinter.Tk()
# 画面サイズ
root2.geometry('300x200')
# 画面タイトル
root2.title('ラジオボタン基本編')

# チェック有無変数
var = tkinter.IntVar()
# value=2のラジオボタンにチェックを入れる
var.set(2)

# ラジオボタン基本作成
rdo1 = tkinter.Radiobutton(root2, value=0, variable=var, text='Apple')
rdo1.place(x=70, y=40)

rdo2 = tkinter.Radiobutton(root2, value=1, variable=var, text='Amazon')
rdo2.place(x=70, y=70)

rdo3 = tkinter.Radiobutton(root2, value=2, variable=var, text='Google')
rdo3.place(x=70, y=100)

root2.mainloop()



# Tkクラス生成
tki = tkinter.Tk()
# 画面サイズ
tki.geometry('300x200')
# 画面タイトル
tki.title('ラジオボタン応用編')


# ラジオボタンのラベルをリスト化する
rdo_txt = ['Python','Java','C#']
# ラジオボタンの状態
rdo_var = tkinter.IntVar()

# ラジオボタンを動的に作成して配置
for i in range(len(rdo_txt)):
    rdo = tkinter.Radiobutton(tki, value=i, variable=rdo_var, text=rdo_txt[i]) 
    rdo.place(x=50, y=30 + (i * 24))

# ボタンクリックイベント
def btn_click():
    num = rdo_var.get()
    tkinter.messagebox.showinfo('チェックされた項目', rdo_txt[num])

# ボタン作成 
btn = tkinter.Button(tki, text='ラジオボタン取得', command=btn_click)
btn.place(x=100, y=170) 

tki.mainloop()