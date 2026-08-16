import sys
import csv
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from fpdf import FPDF

def addc(i):
    with open('data.csv','a+',newline='') as file:
        writer = csv.writer(file)
        current_dt_tm = datetime.now()
        i.insert(0,current_dt_tm)
        writer.writerow(i)
     
def addf(i):
    with open('fert.csv','a+',newline='') as file:
        writer = csv.writer(file)
        current_dt_tm = datetime.now()
        i.insert(0,current_dt_tm)
        writer.writerow(i)

def addl(i):
    with open('lab.csv','a+',newline='') as file:
        writer = csv.writer(file)
        current_dt_tm = datetime.now()
        i.insert(0,current_dt_tm)
        writer.writerow(i)

def view_c():
    data = []
    with open('data.csv') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    return data

def view_f():
    data = []
    with open('fert.csv') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    return data

def view_l():
    data = []
    with open('lab.csv') as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    return data

def remc(i):
    def save(j):
        with open('data.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    SeedVariety = i
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == SeedVariety:
                    new_list.remove(row)
        save(new_list)

def remf(i):
    def save(j):
        with open('fert.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    FertiliserName = i
    with open('fert.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == FertiliserName:
                    new_list.remove(row)
        save(new_list)


def reml(i):
    def save(j):
        with open('lab.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
    new_list = []
    LabourerId = i
    with open('lab.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == LabourerId:
                    new_list.remove(row)
        save(new_list)

def search(i):
    SeedVariety = i
    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == SeedVariety:
                    return True

def searcf(i):
    Fertname = i
    with open('fert.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == Fertname:
                    return True

def searcl(i):
    LabId = i
    with open('lab.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == LabId:
                    return True
              

def searchc(i):
    data = []
    SeedVariety = i
    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == SeedVariety:
                    data.append(row)
    return data

def searchf(i):
    data = []
    FertiliserName = i
    with open('fert.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == FertiliserName:
                    data.append(row)
    return data

def searchl(i):
    data = []
    LabourerId = i
    with open('lab.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == LabourerId:
                    data.append(row)
    return data

def datapdf():
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times','B',14.0) 
        col_width = page_width/5
        th = pdf.font_size
        pdf.cell(page_width, 0.0, 'Crop Information', align='C')
        pdf.ln(10)
        pdf.set_font('Courier', '', 12)
        pdf.ln(1)
        with open('data.csv', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                        pdf.cell(col_width, th, row[1], border=1)
                        pdf.cell(col_width, th, row[2], border=1)
                        pdf.cell(col_width, th, row[3], border=1)
                        pdf.cell(col_width, th, row[4], border=1)
                        pdf.cell(col_width, th, row[5], border=1)
                        pdf.ln(th)
        pdf.ln(10)
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        pdf.output('crop.pdf', 'F')
        messagebox.showinfo('information','Pdf downloaded')

def fertpdf():
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times','B',14.0) 
        col_width = page_width/5
        th = pdf.font_size
        pdf.cell(page_width, 0.0, 'Fertiliser Information', align='C')
        pdf.ln(10)
        pdf.set_font('Courier', '', 12)
        pdf.ln(1)
        with open('fert.csv', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                        pdf.cell(col_width, th, row[1], border=1)
                        pdf.cell(col_width, th, row[2], border=1)
                        pdf.cell(col_width, th, row[3], border=1)
                        pdf.cell(col_width, th, row[4], border=1)
                        pdf.ln(th)
        pdf.ln(10)
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        pdf.output('fert.pdf', 'F')
        messagebox.showinfo('information','Pdf downloaded')

def labpdf():
        pdf = FPDF()
        pdf.add_page()
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.set_font('Times','B',14.0) 
        col_width = page_width/5
        th = pdf.font_size
        pdf.cell(page_width, 0.0, 'Labourer Information', align='C')
        pdf.ln(10)
        pdf.set_font('Courier', '', 12)
        pdf.ln(1)
        with open('lab.csv', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                        pdf.cell(col_width, th, row[1], border=1)
                        pdf.cell(col_width, th, row[2], border=1)
                        pdf.cell(col_width, th, row[3], border=1)
                        pdf.cell(col_width, th, row[4], border=1)
                        pdf.cell(col_width, th, row[5], border=1)
                        pdf.ln(th)
        pdf.ln(10)
        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of report -', align='C')
        pdf.output('lab.pdf', 'F')
        messagebox.showinfo('information','Pdf downloaded')

def updatec(i):    
    new_list = []
    SeedVariety = i[0]
    global CropName, FertiliserUsed, QuantityAvail, PricePkg
    CropName = i[1]
    SeedVariety = i[2]
    FertiliserUsed = i[3]
    QuantityAvail = i[4]
    PricePkg = i[5]
    with open('data.csv','r') as file:
        reader= csv.reader(file)
        for row in reader:
                new_list.append(row)
                for element in row:
                    if element == SeedVariety:
                        CropName = i[1]
                        SeedVariety = i[2]
                        FertiliserUsed = i[3]
                        QuantityAvail = i[4]
                        PricePkg = i[5]
                data = [CropName, SeedVariety, FertiliserUsed, QuantityAvail, PricePkg]
                index = new_list.index(row)
                new_list[index]= data
    with open('data.csv','w') as file:
        writer = csv.writer(file)
        writer.writerows(new_list)




