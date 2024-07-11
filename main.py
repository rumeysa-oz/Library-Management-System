from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from Admin_menu import Books



# MAIN WINDOW
class Visualize(Login,Books):

    def __init__(self):
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  # LOGIN WINDOW EXITS
        self.mainw = Toplevel(bg="white")
        self.mainw.state('zoomed')
        self.mainw.title("Library Management System")
        self.mainw.resizable(0,0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        
        

        self.getdetails()
    # OVERRIDING CLOSE BUTTON && DESTRUCTOR FOR CLASS LOGIN AND MAIN WINDOW
    def __Main_del__(self):
        if messagebox.askyesno("Quit", " Leave Library Management System?") == True:
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

        

    # FETCH DETAILS FROM BOOKS, MEMBERS AND BOOK_DETAİL
    def getdetails(self):
        self.cur.execute("select * from BOOKS")
        self.products = self.cur.fetchall()
        l = self.cur.fetchall()
        self.buildmain()


    #  ADD WIDGETS TO TOP OF MAIN WINDOW
    def buildmain(self):

        super(Books).__init__()
        self.main_menu(8,8)
        self.logout.config(command=self.__Main_del__)
        self.topframe=LabelFrame(self.mainw,width=1600,height=120,bg="#4267b2")
        self.topframe.place(x=0,y=0)
        self.storelable=Label(self.topframe,text="The Library Management System",bg="#4267b2",anchor="center")
        self.storelable.config(font="Roboto 30 bold",fg="snow")
        self.storelable.place(x=360,y=30)
      


if __name__ == '__main__':
    w =  Visualize()
    w.base.commit()
    w.mainw.mainloop()
