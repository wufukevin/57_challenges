# 1. 匯入模組與類別
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

import variable as v


# 2. 定義元件之事件處理函數


def event_handler():
    mb.showinfo("Info", "Hello World!")


def do_askstring():
    str_input = sd.askstring("askstring", "請輸入姓名")
    print("{} {}".format(str_input, type(str_input)))


def do_askinteger():
    int_input = sd.askinteger("askinteger", "請輸入年齡", minvalue=0, maxvalue=120)
    print("{} {}".format(int_input, type(int_input)))


def do_askfloat():
    float_input = sd.askfloat("askfloat", "請輸入體重", initialvalue=50.0)
    print("{} {}".format(float_input, type(float_input)))


# 3. 建立最上層視窗, 設定標題與大小
def initial(title='ttk GUI'):
    v.root = tk.Tk()
    v.root.title(title)
    v.root.geometry("400x300")


def createInputWidget(question=''):
    tk.Label(v.root, text=question).pack()
    temp = tk.Entry(v.root)
    v.inputwidgetList.append(temp)
    temp.pack()


def runMainFunction(movieRecommendation):
    def _runMainFunction():
        v.inputList = []
        for widget in v.inputwidgetList:
            value = widget.get()
            v.inputList.append(value)
        if movieRecommendation is not None:
            movieRecommendation.searchRequest(*v.inputList)
            movieRecommendation.showSearchResult()
    return _runMainFunction


def loop(movieRecommendation):
    tk.Button(v.root, text='Run the program !!!', command=runMainFunction(movieRecommendation)).pack()
    v.root.mainloop()


# 4. 加入 tk/ttk 元件並指定事件處理函數
# sd.askstring('a','b')
# ttk.Button(root, text="askstring", command=do_askstring).pack()
# ttk.Button(root, text="askinteger", command=do_askinteger).pack()
# ttk.Button(root, text="askfloat", command=do_askfloat).pack()
# for i in range(3):
#     ttk.Button(root, text="OK", command=event_handler).pack()

# 5. 啟始事件迴圈顯示視窗
if __name__ == '__main__':
    initial()
    loop()
