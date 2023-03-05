# 参考URL
# https://pg-chain.com/python-filedialog

from tkinter import filedialog

#テキストファイルを選択するファイルダイアログを表示する
typ = [('テキストファイル','*.txt')] 
#初期表示するパス
dir = 'C:\\pg'
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 

print(fle)
#[結果] C:/pg/python/LICENSE.txt


from tkinter import filedialog

typ = [('', '*')]
dir = 'C:\\pg'
fle = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 

for f in fle:
    print(f)
#[結果] C:/pg/data1.xlsx
#[結果] C:/pg/data2.xlsx
#[結果] C:/pg/data3.xlsx


# すべてのファイル
typ=[('', '*')]
# テキストファイルのみ
typ=[('テキストファイル', '*.txt')]
# テキストファイルとCSVファイル
typ = [('テキストファイル', '*.txt'), ('CSVファイル', '*.csv')]