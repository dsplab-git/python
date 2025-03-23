import tkinter

def click_btnRun():
    total = 0
    total -= int(entry1B.get())*500
    total -= int(entry2B.get())*900
    total -= int(entry3B.get())*800
    total -= int(entry4B.get())*3500
    total -= int(entry5B.get())*700
    total -= int(entry6B.get())*1000

    total += int(entry1S.get())*1800
    total += int(entry2S.get())*1400
    total += int(entry3S.get())*1800
    total += int(entry4S.get())*4000
    total += int(entry5S.get())*1500
    total += int(entry6S.get())*2000

    str1 = "오늘 총 매출액은 "+str(total)+"원 입니다."
    
    labelResult = tkinter.Label(root, text=str1, font=("맑은 고딕",10))
    labelResult.place(x=50,y=250)

root = tkinter.Tk()
root.title("CU")
root.geometry("700x300")

label1 = tkinter.Label(root, text="캔 커피", font=("맑은 고딕",10))
label2 = tkinter.Label(root, text="삼각김밥", font=("맑은 고딕",10))
label3 = tkinter.Label(root, text="바나나 우유", font=("맑은 고딕",10))
label4 = tkinter.Label(root, text="도시락", font=("맑은 고딕",10))
label5 = tkinter.Label(root, text="콜라", font=("맑은 고딕",10))
label6 = tkinter.Label(root, text="새우깡", font=("맑은 고딕",10))
labelBuy  = tkinter.Label(root, text="판매 수량", font=("맑은 고딕",10))
labelSell = tkinter.Label(root, text="구매 수량", font=("맑은 고딕",10))

labelX = 25
gapX = 40
label1.place(x= 50,y=50,width=100)
label2.place(x=150,y=50,width=100)
label3.place(x=250,y=50,width=100)
label4.place(x=350,y=50,width=100)
label5.place(x=450,y=50,width=100)
label6.place(x=550,y=50,width=100)
labelBuy.place(x=5,y=100)
labelSell.place(x=5,y=150)

entry1S = tkinter.Entry(width=4)
entry2S = tkinter.Entry(width=4)
entry3S = tkinter.Entry(width=4)
entry4S = tkinter.Entry(width=4)
entry5S = tkinter.Entry(width=4)
entry6S = tkinter.Entry(width=4)
entry1B = tkinter.Entry(width=4)
entry2B = tkinter.Entry(width=4)
entry3B = tkinter.Entry(width=4)
entry4B = tkinter.Entry(width=4)
entry5B = tkinter.Entry(width=4)
entry6B = tkinter.Entry(width=4)

entry1B.insert(0,"0")
entry1S.insert(0,"0")
entry2B.insert(0,"0")
entry2S.insert(0,"0")
entry3B.insert(0,"0")
entry3S.insert(0,"0")
entry4B.insert(0,"0")
entry4S.insert(0,"0")
entry5B.insert(0,"0")
entry5S.insert(0,"0")
entry6B.insert(0,"0")
entry6S.insert(0,"0")

entry1S.place(x=100-15,y=100)
entry2S.place(x=200-15,y=100)
entry3S.place(x=300-15,y=100)
entry4S.place(x=400-15,y=100)
entry5S.place(x=500-15,y=100)
entry6S.place(x=600-15,y=100)

entry1B.place(x=100-15,y=150)
entry2B.place(x=200-15,y=150)
entry3B.place(x=300-15,y=150)
entry4B.place(x=400-15,y=150)
entry5B.place(x=500-15,y=150)
entry6B.place(x=600-15,y=150)

btnRun = tkinter.Button(root, text="계산", font=("Times New Roma",10),command=click_btnRun)
btnRun.place(x=50, y=200,width=600,height=30)

root.mainloop()