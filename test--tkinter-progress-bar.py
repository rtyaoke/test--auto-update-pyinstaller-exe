import tkinter
from tkinter import ttk

# ボタンクリック時に実行する関数


def count_up():
    if var.get() < 100:
        var.set(var.get()+10)  # 値を＋10


root = tkinter.Tk()
var = tkinter.IntVar(root)  # 現在値格納用変数

# プログレスバー(確定的)
pb = ttk.Progressbar(
    root,
    maximum=100,  # 最大値
    mode="determinate",  # 確定的モード
    variable=var,  # 変数を設定
)
pb.pack()

# カウントアップボタン
b = tkinter.Button(
    root,
    text="count up",
    command=count_up,  # クリック時に実行する関数
)
b.pack()

root.mainloop()
