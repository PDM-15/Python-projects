tree_data = tree.focus()
                        tree_dictionary = tree.item(tree_data)
                        tree_list = tree_dictionary['values']

                        CropName = str(tree_list[1])
                        SeedVariety = str(tree_list[2])
                        FertiliserUsed = str(tree_list[3])
                        QtyAvail = str(tree_list[4])
                        PricePkg = str(tree_list[5])

                        l_cname.insert(0,CropName)
                        l_cseed.insert(0,SeedVariety)
                        l_fertu.insert(0,FertiliserUsed)
                        l_qtyav.insert(0,QtyAvail)
                        l_prp.insert(0,PricePkg)

                        def updc():

                                CropName = l_cname.get()
                                SeedVariety = l_cseed.get()
                                FertiliserUsed = l_fertu.get()
                                QtyAvail = l_qtyav.get()
                                PricePkg = l_prp.get()
                                list = [CropName, SeedVariety, FertiliserUsed, QtyAvail, PricePkg]
                                remove(list)
                                if CropName == '' or SeedVariety == '' or FertiliserUsed == '' or QtyAvail == '' or PricePkg == '':
                                        messagebox.showwarning('data','Please fill in all details')
                                        
                                else:
                                        addc(list)
                                        messagebox.showinfo('data', 'Data added successfully!')
                                        

                        '''current_dt_tm = str(tree_list[0])
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

                        def confirm():
                                new_dt_tm = datetime.now()
                                new_crop = l_cname.get()
                                new_seed = l_cseed.get()
                                new_fert = l_fertu.get()
                                new_quant = l_qtyav.get()
                                new_price = l_prp.get()

                                list=[new_dt_tm,new_crop,new_seed,new_fert,new_quant,new_price]
                               
                                updatec(list)

                                messagebox.showinfo('Success','Data updated Successfully')
                                
                                current_dt_tm.delete(0,'end')
                                l_cname.delete(0, 'end')
                                l_cseed.delete(0, 'end')
                                l_fertu.delete(0, 'end')
                                l_qtyav.delete(0, 'end')
                                l_prp.delete(0, 'end')'''






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