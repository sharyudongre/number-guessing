import tkinter as tk
import random
from tkinter import font
tries=0
comp_guess=random.randint(1,10)
def check():
    #get user guess
    global tries

    user_guess=int(txt_guess.get())

    if user_guess>comp_guess:
        tries=tries+1
        msg="the number is lower than "+str(user_guess)
    elif user_guess<comp_guess:
        tries =tries + 1
        msg="the number is higher than "+str(user_guess)
    elif user_guess==comp_guess:
        tries = tries + 1
        msg="CONGRATS!!! your guess is correct!"
    else:
        msg="something is wrong"

    lbl_result["text"]=msg
    lbl_tri["text"] = "number of tries:" + str(int(tries))


def reset():

    global comp_guess, tries
    tries=0
    comp_guess = random.randint(1, 10)
    lbl_tri["text"] = "number of tries:" + str(int(tries))

    lbl_result["text"]="The game is reset try again"

root=tk.Tk()
root.title("Guessing Game")

root.configure(bg="violet")

root.geometry("450x225")

#widgets
myFont = font.Font(size=12)

lbl_title=tk.Label(root,text="Welcome to the guessing game\n",bg="violet")
lbl_title.pack()
lbl_title['font']=myFont


lbl_result=tk.Label(root,text="Good Luck!\n",bg="violet")
lbl_result.pack()
lbl_result['font']=myFont



lbl_tri=tk.Label(root,text="number of tries:"+str(tries),bg="violet")
lbl_tri.pack()
lbl_tri['font']=myFont
lbl_tri.place(relx=0.09,rely=0.8)


btn_check=tk.Button(root,text="check",width=5,height=3,bg="green",fg="black",command=check)
btn_check.pack(side="left")
btn_check['font']=myFont
btn_check.place(relx=0.1,rely=0.4)

btn_reset=tk.Button(root,text="reset",width=5,height=3,fg="black",bg="blue",command=reset)
btn_reset.pack(side="right")
btn_reset['font']=myFont
btn_reset.place(relx=0.78,rely=0.4)


txt_guess=tk.Entry(root,width=7)
txt_guess.pack()
txt_guess.place(height=50,width=70,relx=0.42,rely=0.4)
txt_guess['font']=myFont


lbl_term=tk.Label(root,text="your guess\n",bg="violet")
lbl_term.pack()
lbl_term['font']=myFont
lbl_term.place(relx=0.497,rely=0.74,anchor="center")


root.mainloop()
root.destroy()

