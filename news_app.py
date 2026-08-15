import requests
import io
import webbrowser
from tkinter import *
from urllib.request import Request, urlopen
from PIL import Image,ImageTk


class NewsApp:

    def __init__(self):

       #fetch data
       self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b1af6b06c49c48b7921b5d372144aaff').json()
       
       #initial gui load
       self.load_gui()
       

       #load the 1st news item

       self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('400x700')
        self.root.resizable(0,0)
        self.root.title('News App')
        self.root.configure(bg = 'black')

    #clear the screen for the next news item
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        #clear the screen for the new news item
        self.clear()

        #image
        try:
            # 1. Get the URL from the JSON data first
            img_url = self.data['articles'][index]['urlToImage']
    
            # 2. Build and execute the request with headers
            req = Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            raw_data = urlopen(req).read()
    
            img = Image.open(io.BytesIO(raw_data)).resize((350, 250))
    
            # 3. Store reference in self.photo to prevent garbage collection
            self.photo = ImageTk.PhotoImage(img)

        except Exception as e:
            # Fallback to your image when urlopen, JSON extraction, or decoding fails
            fallback_url = "https://png.pngtree.com/png-vector/20221125/ourmid/pngtree-no-image-available-icon-flatvector-illustration-thumbnail-graphic-illustration-vector-png-image_40966590.jpg"
    
            try:
                req = Request(fallback_url, headers={'User-Agent': 'Mozilla/5.0'})
                raw_data = urlopen(req).read()
                img = Image.open(io.BytesIO(raw_data)).resize((350, 250))
                self.photo = ImageTk.PhotoImage(img)
            except Exception as fallback_error:
                print(f"Completely failed to load any image: {fallback_error}")

        label = Label(self.root, image=self.photo)
        label.pack(pady=(30,50))


        heading = Label(self.root, text = self.data['articles'][index]['title'], bg = 'black', fg = 'white', wraplength = 350, justify = 'center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana', 15))

        details = Label(self.root, text = self.data['articles'][index]['description'], bg = 'black', fg = 'white', wraplength = 350, justify = 'center')
        details.pack(pady=(2,20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        #For the first item there cannot be a previous one, so we need to disable it
        if index == 0:
            prev = Button(frame, text ='Prev', width = 18, height = 3, state=DISABLED)
            prev.pack(side=LEFT)
        else:
            prev = Button(frame, text ='Prev', width = 18, height = 3, command = lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        read = Button(frame, text ='Read More', width = 18, height = 3, command = lambda: webbrowser.open(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        #For the last news item, there cannot be next news item, so we disable it
        if index == len(self.data['articles']) - 1:
            next= Button(frame, text ='Next', width = 18, height = 3, state=DISABLED)
            next.pack(side=LEFT)
        else:
            next= Button(frame, text ='Next', width = 18, height = 3, command = lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        

        self.root.mainloop()

obj = NewsApp()