import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('300x200')
# 画面タイトル
root.title('テキストボックス')


# テキストボックス作成
txt = tkinter.Entry(width=20)
txt.place(x=90, y=70)


# 表示
root.mainloop()