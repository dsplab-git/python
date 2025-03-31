import tkinter

# 버튼 클릭하면 실행하는 함수
def click_btnRun():
    # 값 입력 (글자여서 숫자로 바꿔야 함)
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    # 라벨에 넣을 문자열
    str1 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    str2 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지은 "+str(num1%num2)+"입니다."

    # 라벨 만들기 (결과가 담긴 문자열 1,2)
    label3 = tkinter.Label(root, text=str1, font=("맑은 고딕",10))
    label3.place(x=25,y=125)

    label3 = tkinter.Label(root, text=str2, font=("맑은 고딕",10))
    label3.place(x=25,y=152)

# tkinter 기본문 시작
root = tkinter.Tk()
root.title("산술 연산자")
root.geometry("400x300")

# 라벨 만들기 (설명이 담긴 문자열 1,2)
label1 = tkinter.Label(root, text="나눠 지는 수", font=("맑은 고딕",10))
label1.place(x=25,y=25)

label2 = tkinter.Label(root, text="나누는 수", font=("맑은 고딕",10))
label2.place(x=35,y=77)

# 사용자가 값을 입력하는 란
entry1 = tkinter.Entry(width=10)
entry1.place(x=130,y=26)

entry2 = tkinter.Entry(width=10)
entry2.place(x=130,y=78)

# 계산 버튼
btnRun = tkinter.Button(root, text="계산", font=("Times New Roma",10),command=click_btnRun)
btnRun.place(x=234, y=25,width=70,height=70)

# tkinter 기본문 끝
root.mainloop()