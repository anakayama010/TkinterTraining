import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('Rabelの作成')


# ラベル作成
lbl1 = tkinter.Label(text='Rabel ラベル')


# 文字色・・・foreground、fg
# 背景色・・・background、bg

# ラベルの文字色
lbl2 = tkinter.Label(text="foreground='#faf0e6', background='#778899'", foreground='#faf0e6', background='#778899')

# ラベルの背景色（文字色名）
lbl3 = tkinter.Label(text="foreground='pink', background='blue'", foreground='pink', background='blue') 

lbl1.place(x=30, y=50)
lbl2.place(x=30, y=80)
lbl3.place(x=30, y=110)

# 表示
root.mainloop()