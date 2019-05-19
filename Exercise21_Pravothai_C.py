from tkinter import *

def calculateFunction(event):
   result = float(TextBoxWeight.get()) / ((float(TextBoxHeight.get())  / 100) ** 2 )

   if result >= 30:
      print('อ้วนมาก')
   elif result < 30:
      print('อ้วน')
   elif result < 25:
      print('น้ำหนักเกิน')
   elif result < 23:
      print('น้ำหนักปกติ')
   else :
      print('ผอมเกินไป')
mainWindow = Tk()
labelHeight = Label(mainWindow,text='ส่วนสูง (cm.)').grid(row=0,column=0)
TextBoxHeight = Entry(mainWindow)
TextBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow, text='น้ำหนัก (Kg.)').grid(row=1, column=0)
TextBoxWeight = Entry(mainWindow)
TextBoxWeight.grid(row=1, column=1)
calculateButton = Button(mainWindow,text='คำนวณ')
calculateButton.bind('<Button-1>',calculateFunction)
calculateButton.grid(row=2)
mainWindow.mainloop()