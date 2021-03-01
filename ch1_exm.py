import sys
import tkinter as tk

window = tk.Tk()
window.title('Tip APP')

header_label = tk.Label(window, text='Tip Calculator')
header_label.pack()


def getNumber():
    bill_get = bill_entry.get()
    if bill_get.isdigit():
        bill = float(bill_get)
        bill_warning.configure(text='')
    else:
        bill_warning.configure(text='Please enter a valid number')

    tipRate_get = tip_entry.get()
    if tipRate_get.isdigit():
        tipRate = float(tipRate_get)
        tip_warning.configure(text='')
    else:
        tip_warning.configure(text='Please enter a valid number')
    
    if bill_get.isdigit() and tipRate_get.isdigit():
        tip = bill*tipRate/100
        allBill = tip+bill
        # 將計算結果更新到 result_label 文字內容
        tipResult_label_2.configure(text=tip)
        total_label_2.configure(text=allBill)

    window.after(1000, getNumber)



# 將元件分為 bill/tip 兩群並加入主視窗
bill_frame = tk.Frame(window)
bill_frame.pack(side=tk.TOP)
bill_label = tk.Label(bill_frame, text='What is the bill ? ')
bill_label.pack(side=tk.LEFT)
bill_entry = tk.Entry(bill_frame)
bill_entry.pack(side=tk.LEFT)
bill_warning = tk.Label(bill_frame)
bill_warning.pack(side=tk.LEFT)

tip_frame = tk.Frame(window)
tip_frame.pack(side=tk.TOP)
tip_label = tk.Label(tip_frame, text='What is the tip percentage ? ')
tip_label.pack(side=tk.LEFT)
tip_entry = tk.Entry(tip_frame)
tip_entry.pack(side=tk.LEFT)
tip_warning = tk.Label(tip_frame)
tip_warning.pack(side=tk.LEFT)

tipResult_frame = tk.Frame(window)
tipResult_frame.pack(side=tk.TOP)
tipResult_label_1 = tk.Label(tipResult_frame, text='The tip is $')
tipResult_label_1.pack(side=tk.LEFT)
tipResult_label_2 = tk.Label(tipResult_frame)
tipResult_label_2.pack(side=tk.LEFT)

total_frame = tk.Frame(window)
total_frame.pack(side=tk.TOP)
total_label_1 = tk.Label(total_frame, text='The total is $')
total_label_1.pack(side=tk.LEFT)
total_label_2 = tk.Label(total_frame)
total_label_2.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text='馬上計算', command=getNumber)
calculate_btn.pack()

getNumber()
window.mainloop()


"""
notrepeat = 1
while True:
    notrepeat = 1
    bill_input = input('What is the bill ? $')
    if bill_input.isdigit():
        bill = float(bill_input)
    else:
        print('Please enter a valid number for the bill amount.')
        notrepeat = 0
    if notrepeat:
        break

while True:
    notrepeat = 1
    tipRate_input = input('What is the tip percentage ? ')
    if tipRate_input.isdigit():
        tipRate = float(tipRate_input)
    else:
        print('Please enter a valid number for the tip rate.')
        notrepeat = 0
    if notrepeat:
        break
def tipFunc(bill, tiprate):
    ans = bill*tiprate/100
    return ans
tip = tipFunc(bill, tipRate)
# '%.2f': 控制小數位 , sep : 控制 print 結尾  
print('The tip is $', '%.2f'%tip, sep="")
print('The total is $', '%.2f'%(bill+tip), sep="")
"""