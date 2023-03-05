import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('Rabelの作成')


# ラベル作成
lbl = tkinter.Label(text='Rabel ラベル')
lbl.place(x=30, y=70)


# 表示
root.mainloop()