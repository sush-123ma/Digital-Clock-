from datetime import datetime
import time
from turtle import *
import tkinter as tk
def DigitalClock():
  setup()
  tu=Turtle()
  n=datetime.time(datetime.now())
  k=str(n.replace(microsecond=0))
  l=k.split(":")
  h=int(l[0])
  m=int(l[1])
  s=int(l[2])
  if h>12:
    a="PM"
  else:
    a="AM"
  while True:
    tu.clear()
    if h>12:
        h=h-12
        a="PM"
    tu.write(str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)+a,align="center",font=("arial",30,"bold"))
    s=s+1
    time.sleep(1)
    if s==60:
        s=0
        m=m+1
    if m==60:
        m=0
        h=h+1
    tu.hideturtle()
root=tk.Tk()
canvas1=tk.Canvas(root,width=200,height=200)
canvas1.pack()
button1=tk.Button(text="Click to get Time now",command=DigitalClock)
canvas1.create_window(100,50,window=button1)
root.mainloop()
