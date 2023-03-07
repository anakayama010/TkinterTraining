import tkinter

# メニューから呼び出される関数
def open_file():
    pass


def close_disp():
    pass

# 画面作成
tki = tkinter.Tk()

# メニューバー作成
men = tkinter.Menu(tki)

# メニューバーを画面にセット
tki.config(menu=men)

# メニューに親メニュー（ファイル）を作成する
menu_file = tkinter.Menu(tki)
men.add_cascade(label='ファイル', menu=menu_file)

# 親メニューに子メニュー（開く・閉じる）を追加する
menu_file.add_command(label='開く', command=open_file)
menu_file.add_separator()
menu_file.add_command(label='閉じる', command=close_disp)

tki.mainloop()