from tkinter import *
import math

def leftClickButton(event):
    hightValue = math.pow(float(textBoxHight.get()) / 100, 2)
    weightValue = float(textBoxWeight.get())
    bmiValue = weightValue / hightValue
    labelBMI.configure(text="BMI = " + str('%.1f' % bmiValue))
    if bmiValue <= 18.50:
        bmiResult = "อยู่ในเกณฑ์ 'ผอมเกินไป'"
    elif bmiValue <= 22.90:
        bmiResult = "อยู่ในเกณฑ์ 'น้ำหนักปกติ'"
    elif bmiValue <= 24.90:
        bmiResult = "อยู่ในเกณฑ์ 'น้ำหนักเกิน'"
    elif bmiValue <= 29.90:
        bmiResult = "อยู่ในเกณฑ์ 'อ้วน'"
    elif bmiValue > 29.90:
        bmiResult = "อยู่ในเกณฑ์ 'อ้วนมาก'"
    labelResult.configure(text=bmiResult)

MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2)
labelBMI = Label(MainWindow,text="ผลลัพธ์")
labelBMI.grid(row=3,column=1)
labelResult = Label(MainWindow,text="เกณฑ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()