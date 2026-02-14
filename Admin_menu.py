from datetime import datetime
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Addtional_features import mycombobox,myentry


class Books:

    def __init__(self,mainw):
        self.mainw=mainw

    # ADD MAIN MENU TO WINDOW, ALL FRAMES AND ADD IMAGE BUTTONS
    def main_menu(self,a,b):
         self.mainframe = LabelFrame(self.mainw, width=1100, height=145, bg="light blue")
         self.mainframe.place(x=200, y=100)
        
         mi = PhotoImage(file="logout.png")
         mi = mi.subsample(a,b)
         self.logout = Button(self.mainframe, text="Quit", bd=5, font="roboto 11 bold", image=mi, compound=TOP, border=4)
         self.logout.image = mi
         self.logout.place(x=980, y=27)
         
         mi = PhotoImage(file="member.png")
         mi = mi.subsample(a,b)
         self.members = Button(self.mainframe, text="Members",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addMembers, border=4)
         self.members.image = mi
         self.members.place(x=40, y=27)
         
         mi = PhotoImage(file="book.png")
         mi = mi.subsample(a,b)
         self.books = Button(self.mainframe, text="Books",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addBooks)
         self.books.image = mi
         self.books.place(x=220, y=27)

          
         mi = PhotoImage(file="borrow.png")
         mi = mi.subsample(a,b)
         self.borrowbook = Button(self.mainframe, text="Borrow Books",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addBorrowBooks)
         self.borrowbook.image = mi
         self.borrowbook.place(x=380, y=27)

         mi = PhotoImage(file="return.png")
         mi = mi.subsample(a,b)
         self.returnbook = Button(self.mainframe, text="Return Books",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addReturnBooks)
         self.returnbook.image = mi
         self.returnbook.place(x=570, y=27)

         mi = PhotoImage(file="book_details.png")
         mi = mi.subsample(a,b)
         self.stocks = Button(self.mainframe, text="Book Details",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.build_book_details)
         self.stocks.image = mi
         self.stocks.place(x=760, y=27)

        
	   
         self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
         self.formframe.place(x=100, y=315)
         self.formframeinfo = self.formframe.place_info()
         self.tableframe1 = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe1.place(x=1200, y=315, anchor=NE)
         self.tableframe1info = self.tableframe1.place_info()
         self.tableframe = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe.place(x=1300, y=315, anchor=NE)
         self.tableframeinfo=self.tableframe.place_info()
         self.itembookframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itembookframe.place(x=420, y=280, anchor=NW)
         self.itembookframeinfo=self.itembookframe.place_info()
         self.itemmemberframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itemmemberframe.place(x=420, y=280, anchor=NW)
         self.itemmemberframeinfo=self.itemmemberframe.place_info()
         self.itemborrowbookframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itemborrowbookframe.place(x=420, y=280, anchor=NW)
         self.itemborrowbookframeinfo=self.itemborrowbookframe.place_info()
         self.itemreturnbookframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itemreturnbookframe.place(x=420, y=280, anchor=NW)
         self.itemreturnbookframeinfo=self.itemreturnbookframe.place_info()
         self.formframe1 = Frame(self.mainw, width=500, height=445, bg="#FFFFFF")
         self.formframe1.place(x=100,y=275)
         self.formframe1info = self.formframe1.place_info()
         self.searchframe = Frame(self.mainw, width=720, height=70, bg="#FFFFFF")
         self.searchframe.place(x=575, y=260)
         self.searchframeinfo = self.searchframe.place_info()
         self.searchbut = Button(self.searchframe, text="Search Name", font="roboto 14", bg="#FFFFFF", bd=5, command=self.search_book_details)
         self.searchbut.place(x=0, y=20, height=40)
         self.searchvar=StringVar()
         self.searchentry = myentry(self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25, bg="#FFFFFF")
         self.searchentry.place(x=210, y=20, height=40)
         self.cur.execute("select book_name from books")
         li = self.cur.fetchall()
         a = []
         for i in range(0, len(li)):
             a.append(li[i][0])
         self.searchentry.set_completion_list(a)
         self.resetbut = Button(self.searchframe, text="Reset", font="roboto 14", bd=5, width=8, bg="#FFFFFF", command=self.reset_book_details)
         self.resetbut.place(x=510, y=18, height=40)

         self.cond=0
         self.build_book_details()

    # MAIN MENU ENDS


    # BUILD BOOK TABLE AT BOOK_DETAIL TABLE
    def build_book_details(self):
         self.searchframe.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.formframe.place(self.formframeinfo)
         self.tableframe1.place_forget()
         self.formframe1.place_forget()
         self.itembookframe.place_forget()
         self.itemmemberframe.place_forget()
         self.itemborrowbookframe.place_forget()
         self.itemreturnbookframe.place_forget()
         if(self.cond==1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
    
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Book Id", "Member Id", "Book Name", "Member Name",
         'Borrow Date', 'Return Date'), selectmode="browse", height=18,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=150)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=150)
         self.tree.column('#5', stretch=NO, minwidth=0, width=150)
         self.tree.heading('Book Id', text="Book Id", anchor=W)
         self.tree.heading('Member Id', text="Member Id", anchor=W)
         self.tree.heading('Book Name', text="Book Name", anchor=W)
         self.tree.heading('Member Name', text="Member Name", anchor=W)
         self.tree.heading('Borrow Date', text="Borrow Date", anchor=W , )
         self.tree.heading('Return Date', text="Return Date", anchor=W)

        
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.get_books_details() 
						 
         self.cond=1
         self.main_search(1)

    # SEARCH FRAME FOR BOOK_DETAIL TABLE
    def main_search(self, f):
        self.searchvar.set('')
        if (f==1):
            self.searchframe.config(width=720)
            self.searchframe.place(x=575, y=245)
            self.searchbut.config(text="Search Member Name",command=self.search_book_details)
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar,width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select member_name from members")
            self.cur.execute("select book_name from books")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
         

    # FETCH books FROM books TABLE
    def get_books(self,x=0):
         ans=''
         self.cur.execute("select * from books")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans
    
     # FETCH books FROM books TABLE
    def get_books_details(self,x=0):
         ans=''
         self.cur.execute("select * from BOOK_DETAIL")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans

    # FETCH MEMBERS FROM MEMBER TABLE
    def get_members(self,x=0):
         ans=''
         self.cur.execute("select * from members")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans
    
    # FETCH books FROM books TABLE
    def get_borrow_books(self,x=0):
         ans=''
         self.cur.execute("select * from borrow_book")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans
    
     # FETCH books FROM books TABLE
    def get_return_books(self,x=0):
         ans=''
         self.cur.execute("select * from return_book")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans


    def search_book_details(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("SELECT * FROM BOOK_DETAIL WHERE member_name = ?", (self.searchvar.get(),))
        li=self.cur.fetchall()
        for i in li:
            if(i in li):
                self.tree.insert('', 'end', values=(i))

    def reset_book_details(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.get_books_details()

    def reset_member_details(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.get_members()

    # FUNCTION FOR MEMBERS BUTTON
    def addMembers(self):
        self.itembookframe.place_forget()
        self.itemborrowbookframe.place_forget()
        self.itemreturnbookframe.place_forget()
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemmemberframe.place(self.itemmemberframeinfo)
        self.newitemmemberid = StringVar()
        self.newitemname = StringVar()
        self.newitemsurname = StringVar()
        self.newitempassword = StringVar()
        self.newitemrole  = StringVar()
        l=["Member Id","Name","Surname","Password","Role"]
        for i in range(0,len(l)):
            Label(self.itemmemberframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=15, sticky="w")
        Entry(self.itemmemberframe,width=40,textvariable=self.newitemmemberid, font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemmemberframe, width=40, textvariable=self.newitemname, font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=15, padx=10, ipady=3)
        sup=myentry(self.itemmemberframe,width=40,textvariable=self.newitemsurname, font="roboto 11",bg="#ffffff")
        sup.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemmemberframe, width=40, textvariable=self.newitempassword, font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemmemberframe, width=40, textvariable=self.newitemrole, font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=10, padx=10, ipady=3)
        self.cur.execute("select * from MEMBERS")
        li=self.cur.fetchall()
        a=[] 
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
       # sup.set_completion_list(a)
        Button(self.itemmemberframe, text="Add Member", height=3, bd=6, command=self.insert_member, bg="#FFFFFF").grid(row=5, column=1, pady=10, padx=12, sticky="w", ipadx=10)
        Button(self.itemmemberframe, text="Back", height=3, width=8, bd=6,command=self.build_book_details, bg="#FFFFFF").grid(row=5, column=1, pady=10, padx=16, sticky="e", ipadx=10)


# FUNCTION FOR books BUTTON
    def addBooks(self):
        self.itemmemberframe.place_forget()
        self.itemborrowbookframe.place_forget()
        self.itemreturnbookframe.place_forget()
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itembookframe.place(self.itembookframeinfo)
        self.newitembookid = StringVar()
        self.newitembookname = StringVar()
        self.newitemgenre = StringVar()
        self.newitemauthor = StringVar()

        l1=["Book Id","Book Name","Genre","Author"]
        for i in range(0,len(l1)):
            Label(self.itembookframe,text=l1[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=5, sticky="w")
        Entry(self.itembookframe,width=40,textvariable=self.newitembookid,font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itembookframe, width=40, textvariable=self.newitembookname,font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=10, padx=10, ipady=3)
        cus=myentry(self.itembookframe,width=40,textvariable=self.newitemgenre,font="roboto 11",bg="#ffffff")
        cus.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itembookframe, width=40, textvariable=self.newitemauthor,font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10,ipady=3)
        self.cur.execute("select * from BOOKS")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
       # cus.set_completion_list(a)
        Button(self.itembookframe, text="Add item", height=3, bd=6, command=self.insert_book, bg="#FFFFFF").grid(row=4,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.itembookframe, text="Back", height=3, width=8, bd=6, command=self.build_book_details, bg="#FFFFFF").grid(row=4, column=1, pady=10, padx=16,sticky="e",ipadx=10)


    # FUNCTION FOR Borrow Books
    def addBorrowBooks(self):
        self.itemmemberframe.place_forget()
        self.itembookframe.place_forget()
        self.itemreturnbookframe.place_forget()
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemborrowbookframe.place(self.itemborrowbookframeinfo)
        self.newitemborrowid = StringVar()
        self.newitemmemberid = StringVar()
        self.newitembookid = StringVar()
        self.newitembookname = StringVar()
        self.newitemmembername = StringVar()
        self.newitemduedate = StringVar()
        l=["Borrow Id","Member Id","Book Id","Book Name","Member Name","Due Date"]
        for i in range(0,len(l)):
            Label(self.itemborrowbookframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=15, sticky="w")
        Entry(self.itemborrowbookframe,width=40,textvariable=self.newitemborrowid,font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemborrowbookframe, width=40, textvariable=self.newitemmemberid,font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=15, padx=10, ipady=3)
        sup=myentry(self.itemborrowbookframe,width=40,textvariable=self.newitembookid,font="roboto 11",bg="#ffffff")
        sup.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemborrowbookframe, width=40, textvariable=self.newitembookname,font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemborrowbookframe, width=40, textvariable=self.newitemmembername,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemborrowbookframe, width=40, textvariable=self.newitemduedate,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=10, padx=10, ipady=3)
        self.cur.execute("select * from BORROW_BOOK")
        li=self.cur.fetchall()
       
        Button(self.itemborrowbookframe, text="Add item", height=3, bd=6, command=self.insert_borrow_book, bg="#FFFFFF").grid(row=6, column=1, pady=10, padx=12, sticky="w", ipadx=10)
        Button(self.itemborrowbookframe, text="Back", height=3, width=8, bd=6,command=self.build_book_details, bg="#FFFFFF").grid(row=6, column=1, pady=10, padx=16, sticky="e", ipadx=10)

    def addReturnBooks(self):
        self.itemborrowbookframe.place_forget()
        self.itemmemberframe.place_forget()
        self.itembookframe.place_forget()
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemreturnbookframe.place(self.itemreturnbookframeinfo)
        self.newitemreturnid = StringVar()
        self.newitemmemberid = StringVar()
        self.newitembookid = StringVar()
        self.newitembookname = StringVar()
        self.newitemduedate  = StringVar()
        l=["Return Id","Member Id","Book Id","Book Name","Due Date"]
        for i in range(0,len(l)):
            Label(self.itemreturnbookframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=15, sticky="w")
        Entry(self.itemreturnbookframe,width=40,textvariable=self.newitemreturnid,font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemreturnbookframe, width=40, textvariable=self.newitemmemberid,font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=15, padx=10, ipady=3)
        sup=myentry(self.itemreturnbookframe,width=40,textvariable=self.newitembookid,font="roboto 11",bg="#ffffff")
        sup.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemreturnbookframe, width=40, textvariable=self.newitembookname,font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemreturnbookframe, width=40, textvariable=self.newitemduedate,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=10, padx=10, ipady=3)
        self.cur.execute("select * from RETURN_BOOK")
        li=self.cur.fetchall()
       
        Button(self.itemreturnbookframe, text="Add item", height=3, bd=6, command=self.insert_return_book, bg="#FFFFFF").grid(row=5, column=1, pady=10, padx=12, sticky="w", ipadx=10)
        Button(self.itemreturnbookframe, text="Back", height=3, width=8, bd=6,command=self.build_book_details, bg="#FFFFFF").grid(row=5, column=1, pady=10, padx=16, sticky="e", ipadx=10)



    #  ADD BOOK
    def insert_book(self):
        self.cur.execute("insert into BOOKS values(?,?,?,?)",(
        self.newitembookid.get(),self.newitembookname.get(),self.newitemgenre.get(),self.newitemauthor.get()))
        self.newitembookid.set('')
        self.newitembookname.set('')
        self.newitemgenre.set('')
        self.newitemauthor.set('')
        messagebox.showinfo('Success','BOOK added successfully')
        self.base.commit()


        #  ADD MEMBER
    def insert_member(self):
        self.cur.execute("insert into MEMBERS values(?,?,?,?,?)",(
        self.newitemmemberid.get(),self.newitemname.get(), self.newitemsurname.get(), self.newitempassword.get(),self.newitemrole.get()))
        self.newitemmemberid.set('')
        self.newitemname.set('')
        self.newitemsurname.set('')
        self.newitempassword.set('')
        self.newitemrole.set('')
        messagebox.showinfo('Success','MEMBER added successfully')
        self.base.commit()


#  ADD BORROW_BOOK
    def insert_borrow_book(self):
        self.cur.execute("insert into BORROW_BOOK values(?,?,?,?,?,?)",(
        self.newitemborrowid.get(),self.newitemmemberid.get(), self.newitembookid.get(), self.newitembookname.get(), self.newitemmembername.get(), datetime.strptime(self.newitemduedate.get(), "%m-%d-%Y").date()))
        self.cur.execute("insert into BOOK_DETAIL values(?,?,?,?,?,?)",(
        self.newitembookid.get(),self.newitemmemberid.get(), self.newitembookname.get(), self.newitemmembername.get(), datetime.strptime(self.newitemduedate.get(), "%m-%d-%Y").date(), None))
        self.newitemborrowid.set('')
        self.newitemmemberid.set('')
        self.newitembookid.set('')
        self.newitembookname.set('')
        self.newitemmembername.set('')
        self.newitemduedate.set('')
        messagebox.showinfo('Success','Borrow book added successfully')
        self.base.commit()


        #  ADD'S RETURN_BOOK
    def insert_return_book(self):
        # Convert the date string to a date object
        return_date = datetime.strptime(self.newitemduedate.get(), "%m-%d-%Y").date()

        self.cur.execute("insert into RETURN_BOOK values(?,?,?,?,?)",(
        self.newitemreturnid.get(),self.newitemmemberid.get(), self.newitembookid.get(), self.newitembookname.get(), datetime.strptime(self.newitemduedate.get(), "%m-%d-%Y").date()))
        self.cur.execute("UPDATE BOOK_DETAIL SET RETURN_DATE = ? WHERE MEMBER_ID = ?", (return_date, self.newitemmemberid.get()))
        self.newitemreturnid.set('')
        self.newitemmemberid.set('')
        self.newitembookid.set('')
        self.newitembookname.set('')
        self.newitemduedate.set('')
        messagebox.showinfo('Success','Return book added successfully')
        self.base.commit()

      #  ADD BOOK DETAIL
    def insert_book_detail(self):
        self.cur.execute("insert into BORROW_BOOK values(?,?,?,?,?)",(
        self.newitemborrowid.get(),self.newitemmemberid.get(), self.newitembookid.get(), self.newitembookname.get(), datetime.strptime(self.newitemduedate.get(), "%m-%d-%Y").date()))
        self.newitemborrowid.set('')
        self.newitemmemberid.set('')
        self.newitembookid.set('')
        self.newitembookname.set('')
        self.newitemduedate.set('')
        messagebox.showinfo('Success','Borrow book added successfully')
        self.base.commit()




   
