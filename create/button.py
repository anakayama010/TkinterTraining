import tkinter

# Tkクラス生成
root = tkinter.Tk()
# 画面サイズ
root.geometry('400x200')
# 画面タイトル
root.title('ボタン')

# ボタン
btn = tkinter.Button(root, text='btn')
btn.place(x=30, y=50)

# ボタンの背景色を設定
btn1 = tkinter.Button(root, text="bg='#f0e68c'", bg='#f0e68c')

# ボタンの文字色を設定
btn2 = tkinter.Button(root, text="fg='#ff0000'", fg='#ff0000')

# ボタンの横幅サイズを設定
btn3 = tkinter.Button(root, text="width=20", width=40)

# ボタンの背景色を設定
btn4 = tkinter.Button(root, text="bg='#f0e68c', fg='#ff0000', width=20", bg='#f0e68c', fg='#ff0000', width=40)

#ボタンの配置
btn1.place(x=80, y=30)
btn2.place(x=80, y=60)
btn3.place(x=80, y=90)
btn4.place(x=80, y=120)


# 閉じるボタン（閉じるボタンはオプション引数に「command=画面.destroy」を指定します。）
btn5 = tkinter.Button(root, text='閉じる', command=root.destroy)
btn5.place(x=140, y=170)

root.mainloop()