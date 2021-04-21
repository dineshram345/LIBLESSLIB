from tkinter import *
import time
from tkinter import messagebox
from playsound import playsound
import cv2
from bs4 import BeautifulSoup
import csv
from PIL import ImageTk,Image
import numpy as np
import smtplib 
from pyzbar.pyzbar import decode
root = Tk()
root.geometry('1000x800')
root.resizable(0,0)
root.config(bg ='lightblue')
root.title(' PSNA COLLEGE OF ENGINEERING AND TECHNOLOGY ')
Label(root, text = '# LIB LESS LIB  !!' , font = 'arial 20 bold',  bg ='yellow').pack()
Label(root, font ='arial 15 bold', text = 'TIME NOW :', bg = 'violet').place(x = 40 ,y = 70)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')
def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
Label(root, font ='arial 15 bold', text = 'LIBRARY OPENS AT 9AM ',   bg ='gold').place(x = 20 ,y = 150)
Button(root, text='STEPS :', bd ='5', command = countdown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=190)
def bar():
    def decoder(image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)

        for obj in barcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data " + str(barcodeData)
            
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Barcode: "+barcodeData )
            if(barcodeData =='18EC47'):
                      messagebox.showinfo("LIB ID MATCH ", "--- MATCH SUCCESSFUL --- ")
                      messagebox.showinfo("LIB LESS LIB", "!!!WELCOME DINESH RAM  C!!! ")
            elif(barcodeData =='18EC75'):
                      messagebox.showinfo("LIB ID MATCH ", "--- MATCH SUCCESSFUL --- ")
                      messagebox.showinfo("LIB LESS LIB", "!!!WELCOME JACQULINE JEMIMAH S!!! ")
                      #like this all the students data will be checked along with their photo from the library website (there data is taken using beautifulsoup)
            else:
                messagebox.showinfo("LIB LESS LIB", "*** ACCESS DENIED *** ")

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
def photo():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) 
            print(frame)
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")# This image is checked with the image dataset and result is shown by library database
            
                break
            elif key == ord('q'):
                webcam.release()
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            webcam.release()
            print("Program ended.")
            cv2.destroyAllWindows()
            break

def ajk():
    ren=getrenewaldate()#gets the date from lib database
    def sendmail():
        email = smtplib.SMTP('smtp.gmail.com', 587) 
        email.ehlo()
        email.starttls() 
        email.login("liblesslib@gmail.com", "liblesslib@908") 
        message = "RENEWAL DATE IS ",ren,"2021"
        email.sendmail("liblesslib@gmail.com", "ramcdinesh@gmail.com", message) 
        email.quit()
    sendmail()
    messagebox.showinfo("REMINDER ", "--- RENEWAL DATE HAS BEEN SENT TO MAIL  ---", date )# mail is sent to the pesron 
    

photo = PhotoImage(file = r"C:/Users/DELL/Desktop/LIBLESSLIB/lib.jpg")
Button(root, text='2. SCAN CODE ', bd ='5', command = bar, bg = 'white', font = 'arial 10 bold').place(x=150, y=300)
Button(root, text='1. FACIAL SCAN ', bd ='5', command = photo, bg = 'orange', font = 'arial 10 bold').place(x=150, y=250)
Button(root, text='3. RENEWAL  ', bd ='5', command = ajk, bg = 'lightgreen', font = 'arial 10 bold').place(x=150, y=350)
Label( text = "BEAUTIFUL SOUP #ICONIC  ",bg = 'pink', font = 'arial 15 bold').place(x = 10,y = 20)
Button(root,text='exit',command=root.quit)
Button(root, text='--EXIT-- ', bd ='5', command = root.destroy, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=400)
root.mainloop()
