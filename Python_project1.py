from tkinter import *
import os
from PIL import Image,ImageTk

def rotate_img():
    global counter
    img_label.config(image=img_array[counter%len(img_array)]) #counter%len(img_array) is used so that when counter value increase and index goes out of bound, we need to loop the image back to the first one
    counter = counter+1

counter = 1
root = Tk() #root is the main class of tkinter which is used to create the main window of the application

root.title('Wallpaper viewer')  # used to set the title of the window - titlebar

#root.iconbitmap('favicon.ico')  -> used to set the icon of the window - titlebar
#root.minsize(100,100)  # used to set the minimum size of the window

root.geometry('250x400')  # used to set the size of the window
root.configure(background='black')  # used to set the background color of the window

files = os.listdir('Wallpapers')

#for displaying images in the gui, we need to create an array of photoimage object
img_array = []
for file in files:
    img = Image.open(os.path.join('Wallpapers',file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image = img_array[0])  # used to create a label widget to display the image
img_label.pack(pady=(20,10))  # used for spacing the image from top and bottom

#creating a button to change the image
next_btn = Button(root, text='Next', bg = 'white', fg = 'black', width=28, height = 2, command =rotate_img)
next_btn.pack()

root.mainloop() #used to run the application and wait for user interaction