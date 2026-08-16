from ctypes import alignment
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import left
from venv import create
from backend import *

#colors

co0 = "#4E944F"
co1 = "#83BD75"
co2 = "#B4E197"
co3 = "#E9EFC0"

#main window instance
window = Tk()
window.title("Crop Management System")
window.geometry('2000x2000')
bg = PhotoImage(file="agri.png")
lbl = Label(window,image = bg)
lbl.place(x=0,y=0)
window.resizable(width=TRUE,height=TRUE)
#header
app_name = Label(window, text="Crop Manager", height=1, font=('Verdana 25 bold'), fg=co0, justify=CENTER )
app_name.pack()
#footer
l = Label(window, text="Developed by 4CB19IS035 & 4CB19IS043", fg=co0)
l.place(x=580,y=680)

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Crop mgmt.
def crop():
    #new window popup
    root = Tk()
    root.title("Crop Management")
    root.geometry('400x300')
    root.configure(background=co3)
    root.resizable(width=TRUE,height=TRUE)

#for new crop addition
    def creat():
#new window popup
        win = Tk()
        win.title("Manage")
        win.geometry('300x300')
        win.configure(background=co3)
        win.resizable(width=FALSE,height=FALSE)
#crop name
        l_crname = Label(win, text="Crop name:", bg=co3, fg=co0)
        l_crname.place(x=10,y=30)
        l_cname=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_cname.place(x=100,y=30)
#seed varieties
        l_seed = Label(win, text="Seed Variety:", bg=co3, fg=co0)
        l_seed.place(x=10,y=50)
        l_cseed=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_cseed.place(x=100,y=50)
#fertilizer used
        l_cfert = Label(win, text="Fertilizer used:", bg=co3, fg=co0)
        l_cfert.place(x=10,y=70)
        l_fertu=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_fertu.place(x=100,y=70)
#quatity of crop available
        l_qtyavail = Label(win, text="Qty. available:", bg=co3, fg=co0)
        l_qtyavail.place(x=10,y=90)
        l_qtyav=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_qtyav.place(x=100,y=90)
#price per kg
        l_prpkg = Label(win, text="Price per quintal:", bg=co3, fg=co0)
        l_prpkg.place(x=10,y=110)
        l_prp=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_prp.place(x=100,y=110)
                #inserting in to the system
        def cinsert():
                CropName = l_cname.get()
                SeedVariety = l_cseed.get()
                FertiliserUsed = l_fertu.get()
                QtyAvail = l_qtyav.get()
                PricePkg = l_prp.get()
                data = [CropName, SeedVariety, FertiliserUsed, QtyAvail, PricePkg]
                if CropName == '' or SeedVariety == '' or FertiliserUsed == '' or QtyAvail == '' or PricePkg == '':
                        messagebox.showwarning('data','Please fill in all details')
                        win.destroy()
                else:
                        addc(data)
                        messagebox.showinfo('data', 'Data added successfully!')
                        win.destroy()

        #submit button
        l_submit=Button(win, text="Add record",command=cinsert, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3 )
        l_submit.place(x=200,y=200)
        root.destroy()
                            
    def rem():

        wind = Tk()
        wind.title("Manage")
        wind.geometry('500x500')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_delc = Label(wind, text="Enter the seed variety of the crop to be deleted:", bg=co3, fg=co0)
        l_delc.place(x=50,y=50)
        l_delt=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_delt.place(x=50,y=75)

        def del_c():
                SeedVariety = l_delt.get()
                if l_sub:
                        if search(SeedVariety)==True :
                                res = messagebox.askquestion('Confirm','Are you sure?')
                                if res == 'yes':
                                        remc(SeedVariety)
                                        messagebox.showinfo('information', 'Data deleted successfully!')
                                        wind.destroy()
                                else:
                                        messagebox.showinfo("return","Data Saved")
                                        wind.destroy()
                                                                
                        else :
                                if SeedVariety == " " or search(SeedVariety)==False:
                                        messagebox.showerror('information','Please Enter Valid Seed variety')
                                        wind.destroy()
                                
        l_sub=Button(wind, text="delete", command=del_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=50,y=100)
        root.destroy()

    def ser():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('400x400')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_serc = Label(wind, text="Enter the seed variety of the crop you want search:", bg=co3, fg=co0)
        l_serc.place(x=50,y=50)
        l_searc=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_searc.place(x=50,y=75) 

        def ser_c():
                SeedVariety = l_searc.get()
                data = searchc(SeedVariety)
                
                if data:
                        text1=Label(wind, text="Searched data Found! \n", width=75)
                        text1.place(x=10,y=250)
                        text2=Label(wind, text=searchc(SeedVariety), width=75)
                        text2.place(x=10,y=275)
                        
                else:
                        messagebox.showwarning('warning','Seed Variety not Found!!!')
                        wind.destroy()
                
        l_sub=Button(wind, text="Search", command=ser_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=100,y=100)
        root.destroy()

    def viewc():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('830x250')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        frame_table = Frame(wind, width=1100, height=500, bg=co0)
        frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
        global Tree
        listheader = ['Time of insertion','CropName', 'SeedVariety', 'FertiliserUsed', 'QtyAvail', 'PricePkg']
        tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")
        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0,sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text='Timestamp', anchor=NW)
        tree.heading(1, text='Crop Name', anchor=NW)
        tree.heading(2, text='Seed Variety', anchor=NW)
        tree.heading(3, text='Fertiliser Used', anchor=NW)
        tree.heading(4, text='Quantity Available', anchor=NW)
        tree.heading(5, text='Price per kg', anchor=NW)

        tree.column(0, width=200, anchor='nw')
        tree.column(1, width=175, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=100, anchor='nw')
        tree.column(5, width=120, anchor='nw') 

        d_list = view_c()
                
        for item in d_list:
                tree.insert('','end',values=item)
    
    def up():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('1000x1000')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        frame_table = Frame(wind, width=1100, height=500, bg=co0)
        frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
        
        listheader = ['Time of insertion','CropName', 'SeedVariety', 'FertiliserUsed', 'QtyAvail', 'PricePkg']
        tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")
        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0,sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text='Time of Insertion', anchor=NW)
        tree.heading(1, text='Crop Name', anchor=NW)
        tree.heading(2, text='Seed Variety', anchor=NW)
        tree.heading(3, text='Fertiliser Used', anchor=NW)
        tree.heading(4, text='Quantity Available', anchor=NW)
        tree.heading(5, text='Price per kg', anchor=NW)

        tree.column(0, width=200, anchor='nw')
        tree.column(1, width=175, anchor='nw')
        tree.column(2, width=120, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=100, anchor='nw')
        tree.column(5, width=120, anchor='nw') 

        d_list = view_c()
                
        for item in d_list:
                tree.insert('','end',values=item)
        
#crop name
        l_crname = Label(wind, text="Crop name:", bg=co3, fg=co0)
        l_crname.place(x=10,y=300)
        l_cname=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_cname.place(x=100,y=300)
#seed varieties
        l_seed = Label(wind, text="Seed Variety:", bg=co3, fg=co0)
        l_seed.place(x=10,y=320)
        l_cseed=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_cseed.place(x=100,y=320)
#fertilizer used
        l_cfert = Label(wind, text="Fertilizer used:", bg=co3, fg=co0)
        l_cfert.place(x=10,y=340)
        l_fertu=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_fertu.place(x=100,y=340)
#quatity of crop available
        l_qtyavail = Label(wind, text="Qty. available:", bg=co3, fg=co0)
        l_qtyavail.place(x=10,y=360)
        l_qtyav=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_qtyav.place(x=100,y=360)
#price per kg
        l_prpkg = Label(wind, text="Price per Quintal:", bg=co3, fg=co0)
        l_prpkg.place(x=10,y=380)
        l_prp=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_prp.place(x=100,y=380)
        #updating in to the system
        def up_c():
                                             
                try:
                        tree_data = tree.focus()
                        tree_dictionary = tree.item(tree_data)
                        tree_list = tree_dictionary['values']

                        CropName = str(tree_list[1])
                        SeedVariety = str(tree_list[2])
                        FertiliserUsed = str(tree_list[3])
                        QuantityAvail = str(tree_list[4])
                        PricePkg = str(tree_list[5])
                        
                        l_cname.insert(0,CropName)
                        l_cseed.insert(0,SeedVariety)
                        l_fertu.insert(0,FertiliserUsed)
                        l_qtyav.insert(0,QuantityAvail)
                        l_prp.insert(0,PricePkg)

                        SeedVariety = tree_list[2]
                        remc(SeedVariety)

                        def confirm():
                                new_crop = l_cname.get()
                                new_seed = l_cseed.get()
                                new_fert = l_fertu.get()
                                new_quant = l_qtyav.get()
                                new_price = l_prp.get()

                                list=[new_crop,new_seed,new_fert,new_quant,new_price]
                               
                                addc(list)

                                messagebox.showinfo('Success','Data updated Successfully')
                                wind.destroy()
                       
                        b_confirm=Button(wind, text="Confirm", command=confirm, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
                        b_confirm.place(x=200,y=500)
                        
                except IndexError:
                        messagebox.showerror('Error','Select one of them from the table')

        
        l_sub=Button(wind, text="Update", command=up_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=200,y=450)

#2nd interface
    l_add=Button(root, text="Add", command=creat, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_add.place(x=100,y=50)
   
    l_rem=Button(root, text="Remove", command=rem, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_rem.place(x=250,y=50)

    l_search=Button(root, text="Search", command=ser, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_search.place(x=100,y=150)

    l_view=Button(root, text="View", command=viewc, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_view.place(x=250,y=150)

    l_update=Button(root, text="Update", command=up, height=10, width=20, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_update.place(x=300,y=250)

l_crops = Button(window, text="Crop", command=crop, height=5, width=20, bg=co1, font=('Ivy 20 bold'), fg=co3)
l_crops.place(x=100,y=100)

#----------------------------------------------------------------------------------------------------------------------------------------------

def fert():
    root = Tk()
    root.title("Fertiliser Management")
    root.geometry('400x300')
    root.configure(background=co3)
    root.resizable(width=FALSE,height=FALSE)
    
    def creatf():
        win = Tk()
        win.title("Manage")
        win.geometry('300x300')
        win.configure(background=co3)
        win.resizable(width=FALSE,height=FALSE)

        l_frname = Label(win, text="Fertiliser name:", bg=co3, fg=co0)
        l_frname.place(x=10,y=30)
        l_fname=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_fname.place(x=100,y=30)

        l_expdt = Label(win, text="Expiry Date:", bg=co3, fg=co0)
        l_expdt.place(x=10,y=50)
        l_expdate=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_expdate.place(x=100,y=50)

        l_fqty = Label(win, text="Qty. available:", bg=co3, fg=co0)
        l_fqty.place(x=10,y=70)
        l_fqtyav=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_fqtyav.place(x=100,y=70)

        l_pr = Label(win, text="Price:", bg=co3, fg=co0)
        l_pr.place(x=10,y=90)
        l_price=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_price.place(x=100,y=90)

        def finsert():
                FertiliserName = l_fname.get()
                ExpiryDate = l_expdate.get()
                FertiliserQty = l_fqtyav.get()
                Price = l_price.get()
                data = [FertiliserName, ExpiryDate, FertiliserQty, Price]
                if FertiliserName == '' or ExpiryDate == '' or FertiliserQty == '' or Price == '':
                        messagebox.showwarning('data','Please fill in all details')
                else:
                        addf(data)
                        messagebox.showinfo('data', 'Data added successfully!')
                        win.destroy()

        l_submit=Button(win, text="Add record", command=finsert, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3 )
        l_submit.place(x=200,y=200)
        root.destroy()

    def rem():

        wind = Tk()
        wind.title("Manage")
        wind.geometry('500x500')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_delc = Label(wind, text="Enter the name of fertiliser to be deleted:", bg=co3, fg=co0)
        l_delc.place(x=50,y=50)
        l_delt=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_delt.place(x=50,y=75)

        def del_c():
                fertname = l_delt.get()
                if searcf(fertname)==True :
                                res = messagebox.askquestion('Confirm','Are you sure?')
                                if res == 'yes':
                                        remf(fertname)
                                        messagebox.showinfo('information', 'Data deleted successfully!')
                                        wind.destroy()
                                else:
                                        messagebox.showinfo("return","Data Saved")
                                        wind.destroy()
                                                                
                else :
                        if fertname == " " or searcf(fertname)==False:
                            messagebox.showerror('information','Please Enter Fertiliser Name')
                            wind.destroy()
                       
        l_sub=Button(wind, text="delete", command=del_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=50,y=100)
    
    def ser():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('400x400')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_serc = Label(wind, text="Enter the fertiiser name you want search:", bg=co3, fg=co0)
        l_serc.place(x=50,y=50)
        l_searc=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_searc.place(x=50,y=75) 

        def ser_c():
                FertiliserName = l_searc.get()
                data = searcf(FertiliserName)
                
                if data:
                        text1=Label(wind, text="Searched data Found! \n", width=100)
                        text1.pack()
                        text2=Label(wind, text=searchf(FertiliserName), width=100)
                        text2.pack()
                        
                else:
                        messagebox.showwarning('warning','Fertiliser not Found!!!')
                
        l_sub=Button(wind, text="Search", command=ser_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=100,y=100)

    def viewc():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('700x250')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        frame_table = Frame(wind, width=1100, height=500, bg=co0)
        frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
        global Tree
        listheader = [' ','FertiliserName','ExpiryDate', 'FertiliserQty', 'Price']
        tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")
        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0,sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text=' ', anchor=NW)
        tree.heading(1, text='Fertiliser Name', anchor=NW)
        tree.heading(2, text='ExpiryDate', anchor=NW)
        tree.heading(3, text='Fertiliser Quantity', anchor=NW)
        tree.heading(4, text='Price', anchor=NW)
        
        tree.column(0, width=200, anchor='nw')
        tree.column(1, width=175, anchor='nw')
        tree.column(2, width=100, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=100, anchor='nw')

        d_list = view_f()
                
        for item in d_list:
                tree.insert('','end',values=item)

    l_add=Button(root, text="Add", command=creatf, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_add.place(x=100,y=50)

    l_rem=Button(root, text="Remove", command=rem, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_rem.place(x=250,y=50)

    l_search=Button(root, text="Search",command=ser, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_search.place(x=100,y=150)

    l_view=Button(root, text="View", command=viewc, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_view.place(x=250,y=150)

    '''l_update=Button(root, text="Update", height=10, width=20, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_update.place(x=400,y=300)'''

l_fert = Button(window, text="Fertilizer", command=fert, height=5, width=20, bg=co1, font=('Ivy 20 bold'), fg=co3)
l_fert.place( x=900,y=100)

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Labour mgmt.
def labour():
    #new window popup
    root = Tk()
    root.title("Labour Management")
    root.geometry('400x300')
    root.configure(background=co3)
    root.resizable(width=FALSE,height=FALSE)

#for new labour addition
    def creatl():
#new window popup
        win = Tk()
        win.title("Manage")
        win.geometry('300x300')
        win.configure(background=co3)
        win.resizable(width=FALSE,height=FALSE)
#labourer id
        l_lrid = Label(win, text="Labourer Id:", bg=co3, fg=co0)
        l_lrid.place(x=10,y=30)
        l_lid=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_lid.place(x=100,y=30)
#labourer name
        l_lrname = Label(win, text="Labourer name:", bg=co3, fg=co0)
        l_lrname.place(x=10,y=50)
        l_lname=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_lname.place(x=100,y=50)
#gender
        l_gend = Label(win, text="Gender:", bg=co3, fg=co0)
        l_gend.place(x=10,y=70)
        l_gen = StringVar()
        l_gen.set("Select gender")
        drop = OptionMenu(win,l_gen,"Male","Female")
        drop.place(x=100,y=70)
#No. of days present
        l_att = Label(win, text="No. of days :", bg=co3, fg=co0)
        l_att.place(x=10,y=90)
        l_attend=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_attend.place(x=100,y=90)
#Daily Wage
        l_wage = Label(win, text="Wage:", bg=co3, fg=co0)
        l_wage.place(x=10,y=110)
        l_lwge=Entry(win, width=20, highlightthickness=1, relief='solid')
        l_lwge.place(x=100,y=110)

        def linsert():
                LabourerId = l_lid.get()
                LabourerName = l_lname.get()
                Gender = l_gen.get()
                Attendance = l_attend.get()
                Wage = l_lwge.get()
                data = [LabourerId,LabourerName,Gender,Attendance,Wage]
                if LabourerName == '' or Gender == '' or Attendance == '' or Wage == '':
                        messagebox.showwarning('data','Please fill in all details')
                        win.destroy()
                else:
                        addl(data)
                        messagebox.showinfo('data', 'Data added successfully!')
                        win.destroy()
        l_submit=Button(win, text="Add record", command=linsert, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3 )
        l_submit.place(x=200,y=200)
        root.destroy()

    def viewc():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('700x250')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        frame_table = Frame(wind, width=1100, height=500, bg=co0)
        frame_table.grid(row=2, column=0, columnspan=2, padx=0, pady=1)
        global Tree
        listheader = ['','LabourerName','Gender','Attendance','Wage']
        tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")
        vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0,sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        tree.heading(0, text=' ', anchor=NW)
        tree.heading(1, text='LabourerName', anchor=NW)
        tree.heading(2, text='Gender', anchor=NW)
        tree.heading(3, text='Attendance', anchor=NW)
        tree.heading(4, text='Wage', anchor=NW)
        
        tree.column(0, width=200, anchor='nw')
        tree.column(1, width=175, anchor='nw')
        tree.column(2, width=100, anchor='nw')
        tree.column(3, width=100, anchor='nw')
        tree.column(4, width=100, anchor='nw')
        
        d_list = view_l()
                
        for item in d_list:
                tree.insert('','end',values=item)

        
    def rem():

        wind = Tk()
        wind.title("Manage")
        wind.geometry('500x500')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_delc = Label(wind, text="Enter the name of Labourer Name to be deleted:", bg=co3, fg=co0)
        l_delc.place(x=50,y=50)
        l_delt=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_delt.place(x=50,y=75)
        def del_c():
                LabId = l_delt.get()
                if l_sub:
                        if searcl(LabId)==True :
                                res = messagebox.askquestion('Confirm','Are you sure?')
                                if res == 'yes':
                                        reml(LabId)
                                        messagebox.showinfo('information', 'Data deleted successfully!')
                                        wind.destroy()
                                else:
                                        messagebox.showinfo("return","Data Saved")
                                        wind.destroy()
                                                                
                        else :
                                if LabId == " ":
                                        messagebox.showerror('information','Please Enter Seed variety')
                                        wind.destroy()
                                else:
                                        messagebox.showerror('error','Seed variety not found')
                                        wind.destroy()


        l_sub=Button(wind, text="delete", command=del_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=50,y=100)

    def ser():
        wind = Tk()
        wind.title("Manage")
        wind.geometry('700x700')
        wind.configure(background=co3)
        wind.resizable(width=TRUE,height=TRUE)

        l_serc = Label(wind, text="Enter the name of the labourer you want search:", bg=co3, fg=co0)
        l_serc.place(x=50,y=50)
        l_searc=Entry(wind, width=20, highlightthickness=1, relief='solid')
        l_searc.place(x=50,y=75) 

        def ser_c():
                LabourerName = l_searc.get()
                data = searcl(LabourerName)
                
                if data:
                        text1=Label(wind, text="Searched data Found! \n", width=100)
                        text1.pack()
                        text2=Label(wind, text=searchl(LabourerName), width=100)
                        text2.pack()
                else:
                        messagebox.showwarning('warning','Labourer not Found!!!')
                        wind.destroy()
                
        l_sub=Button(wind, text="Search", command=ser_c, height=5, width=10, bg=co1, font=('Ivy 5 bold'), fg=co3)
        l_sub.place(x=100,y=100)

#2nd interface
    l_add=Button(root, text="Add", command=creatl, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_add.place(x=100,y=50)

    l_rem=Button(root, text="Remove",command=rem, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_rem.place(x=250,y=50)

    l_search=Button(root, text="Search", command=ser, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_search.place(x=100,y=150)

    l_view=Button(root, text="View", command=viewc, height=5, width=10, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_view.place(x=250,y=150)

   
''' l_update=Button(root, text="Update", height=10, width=20, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_update.place(x=400,y=300)'''

l_labour = Button(window, text="Labour", command=labour, height=5, width=20, bg=co1, font=('Ivy 20 bold'), fg=co3)
l_labour.place(x=100,y=400)

#----------------------------------------------------------------------------------------------------------------------------------------------

def summary():
    #new window popup
    root = Tk()
    root.title("Download Info")
    root.geometry('400x300')
    root.configure(background=co3)
    root.resizable(width=FALSE,height=FALSE)

    c = Label(root, text="Download crop information ->", fg=co0)
    c.place(x=10,y=50)
    l_c=Button(root, text="pdf", command=datapdf, height=1, width=2, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_c.place(x=250,y=50)
    f = Label(root, text="Download fertiliser information ->", fg=co0)
    f.place(x=10,y=90)
    l_f=Button(root, text="pdf", command=fertpdf, height=1, width=2, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_f.place(x=250,y=90)
    l = Label(root, text="Download labourer information ->", fg=co0)
    l.place(x=10,y=130)
    l_l=Button(root, text="pdf",command=labpdf, height=1, width=2, bg=co1, font=('Ivy 10 bold'), fg=co3 )
    l_l.place(x=250,y=130)

l_summary = Button(window, text="Summary", command=summary, height=5, width=20, bg=co1, font=('Ivy 20 bold'), fg=co3)
l_summary.place(x=900,y=400)

window.mainloop()

