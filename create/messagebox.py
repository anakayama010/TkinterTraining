'''
# 1.メッセージボックス（情報） 
messagebox.showinfo(タイトル, メッセージ内容)

# 2.メッセージボックス（警告） 
messagebox.showwarning(タイトル, メッセージ内容)

# 3.メッセージボックス（エラー） 
messagebox.showerror(タイトル, メッセージ内容)
'''
# showinfo、showwarning、showerrorの戻り値
	# OKボタン・・・ok


'''
# 4.メッセージボックス（はい・いいえ） 
messagebox.askyesno(タイトル, メッセージ内容)
'''
# askyesno の戻り値
	# はいボタン・・・True
	# いいえボタン・・・False


'''
# 5.メッセージボックス（はい・いいえ） 
messagebox.askquestion(タイトル, メッセージ内容)
'''
# askquestion の戻り値
	# はいボタン・・・yes
	# いいえボタン・・・no


'''
# 6.メッセージボックス（OK・キャンセル） 
messagebox.askokcancel(タイトル, メッセージ内容)
'''
# askokcancel の戻り値
	# OKボタン・・・True
	# キャンセルボタン・・・False


'''
# メッセージボックス（再試行・キャンセル） 
messagebox.askretrycancel(タイトル, メッセージ内容)
'''
# askretrycancel の戻り値
	# 再試行ボタン・・・True
	# キャンセルボタン・・・False


import sys
from tkinter import messagebox

# メッセージボックス（情報） 
messagebox.showinfo('確認', 'もうすぐ誕生日です')

# メッセージボックス（エラー） 
messagebox.showerror('エラー', 'メールアドレスが入力されていません')

# メッセージボックス（はい・いいえ） 
ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
if ret == True:
    sys.exit()
else:
    messagebox.showinfo('確認', 'いいえが押されました')
    
    


	





