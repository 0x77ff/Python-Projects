import tkinter as tk
from pygame import mixer
import shelve
import random
mixer.init()
d = shelve.open('score.txt')
window = tk.Tk()
Moleimg= tk.PhotoImage(file='E:\PythonProjects\Projects\Whack-A-Mole\Mole.png')
Evilmoleimg= tk.PhotoImage(file='E:\PythonProjects\Projects\Whack-A-Mole\EvilMole.png')
window.title("Whack-A-Mole")
window.resizable(0,0)
window.geometry("500x500")
evmon=False
hs=0
ahs=0
def begin():
    wel.pack_forget()
    stt.pack_forget()
    randx=random.randint(1,450)
    randy=random.randint(1,450)
    mole.place(x=randx,y=randy)
def moleclked1():
    global hs
    global evmon
    badm=random.randint(1,4)
    if evmon == False:
     if badm==1:
        moleminusspawn()
        print(str(badm))
        randx=random.randint(1,450)
        randy=random.randint(1,450)
        mole.place(x=randx,y=randy)
        hs=hs+1
        hsc.config(text="Score: "+str(hs))
     else:
      print(str(badm))
      randx=random.randint(1,450)
      randy=random.randint(1,450)
      mole.place(x=randx,y=randy)
      hs=hs+1
      hsc.config(text="Score: "+str(hs))
    else:
        randx=random.randint(1,450)
        randy=random.randint(1,450)
        mole.place(x=randx,y=randy)
        hs=hs+1
        hsc.config(text="Score: "+str(hs))  
def moleminusspawn():
    global evmon
    evmon=True
    randx=random.randint(1,450)
    randy=random.randint(1,450)
    evilmole.place(x=randx,y=randy)
    wait = window.after(2500,unmap)
def moleminus():
    global evmon
    global hs
    hs=hs-2
    evmon=False
    hsc.config(text="Score: "+str(hs))
    evilmole.place_forget()
    randx=random.randint(1,450)
    randy=random.randint(1,450)
    mole.place(x=randx,y=randy)
def unmap():
    global evmon
    evmon=False
    evilmole.place_forget()    
#Main Menu Widgets
stt=tk.Button(text="Begin?",font=('Times', 14),bg="green",height=5,width=25,command=begin)
wel=tk.Label(text="Whack-A-Mole",font=('Bold',24))
hsc=tk.Label(text="Score: 0")
ahsc=tk.Label(text="All-time Highscore: 0")
#Game Widgets
mole=tk.Button(image=Moleimg,command=moleclked1)
evilmole=tk.Button(image=Evilmoleimg,command=moleminus)
mixer.music.load('E:/Pythonprojects/Projects/Whack-A-Mole/Stage_Select_-_Mario_vs_Donkey_Kon_(getmp3.pro).mp3')
mixer.music.play(100)
ahsc.pack()
hsc.pack()
wel.pack(padx=5,pady=40)
stt.pack(padx=5,pady= 70)
window.mainloop()