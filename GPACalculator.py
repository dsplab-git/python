import tkinter

def click_btnRun():
    grade = 0
    grade1 = float(entryLec1.get())
    grade2 = float(entryLec2.get())
    grade3 = float(entryLec3.get())
    
    grade += 3*grade1
    grade += 2*grade2
    grade += 1*grade3
    grade = grade / 6

    str1 = "평균 학점 : "+str(grade)
    
    label3 = tkinter.Label(root, text=str1, font=("맑은 고딕",10))
    label3.place(x=110,y=100)

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y    
    labelMouse["text"]=str(x)+","+str(y)

root = tkinter.Tk()
root.title("성적 계산기")
root.geometry("250x150")

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕",10))
labelMouse.place(x=0,y=130)

label1 = tkinter.Label(root, text="과목(이수학점)", font=("맑은 고딕",10))
label2 = tkinter.Label(root, text="성적", font=("맑은 고딕",10))

labelLectur1 = tkinter.Label(root, text="파이썬(3)", font=("맑은 고딕",10))
labelLectur2 = tkinter.Label(root, text="모바일(2)", font=("맑은 고딕",10))
labelLectur3 = tkinter.Label(root, text="엑셀(1)", font=("맑은 고딕",10))

label1.place(x=10,y=10)
label2.place(x=140,y=10)

labelLectur1.place(x=10,y=35)
labelLectur2.place(x=10,y=55)
labelLectur3.place(x=10,y=75)

entryLec1 = tkinter.Entry(width=4)
entryLec2 = tkinter.Entry(width=4)
entryLec3 = tkinter.Entry(width=4)

entryLec1.insert(0,"3.0")
entryLec2.insert(0,"3.0")
entryLec3.insert(0,"3.0")

entryLec1.place(x=140,y=35)
entryLec2.place(x=140,y=55)
entryLec3.place(x=140,y=75)

btnRun = tkinter.Button(root, text="계산", font=("Times New Roma",10),command=click_btnRun)
btnRun.place(x=10, y=100,width=70,height=20)

root.mainloop()