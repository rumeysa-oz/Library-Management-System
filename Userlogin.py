from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pypyodbc
import ast
# LOGIN CLASS
class Login:

    def __init__(self):
        self.loginw=Tk()
        self.loginw.title("LogIn")
        self.loginw.config(bg="#fff")
        self.loginw.resizable(False, False)
        self.logintable()
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        window_width = 1000
        window_height = 550			   
        x = (screen_width/2) - (window_width/2)  
        y = (screen_height/2) - (window_height/2)
 
        self.loginw.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y)) 
        # Login image
        self.img = PhotoImage(file = "login.png")
        Label(self.loginw, image = self.img, bg = "white").place(x = 110, y = 100)
 
        # Login heading
        self.heading = Label(self.loginw, text = "LOGIN", font = ("Besley","30", "bold"), bg = "#fff", fg = "#57a1f8")
        self.heading.place(x = 700, y = 70)
		 # Login username and password
        self.username = Entry(self.loginw, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.username.place(x=600, y=200)
        self.username.insert(0, "Username")
        self.username.bind("<FocusIn>", self.on_enter)
        self.username.bind("<FocusOut>", self.on_leave)
        Frame(self.loginw, width=295, height=2, bg="black").place(x=600, y=220)
       
        self.password = Entry(self.loginw, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.password.place(x=600, y=250)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", self.on_enter_password)
        self.password.bind("<FocusOut>", self.on_leave_password)
        self.password.bind("<Key>", self.on_type)
        Frame(self.loginw, width=295, height=2, bg="black").place(x=600, y=270)
 													   
		# Login button
        Button(self.loginw, width=42, pady=7, text="Sign In", bg="#57a1f8", fg="white", command = self.signin, font=("Besley", 11)).place(x=600, y=320)
 
 
    # LOGIN SUCCESS
    def signin(self):
        username = self.username.get()
        password = self.password.get()
 
        file = open('datasheet.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
 
        if username in r.keys() and password == r[username]:
            messagebox.showinfo('Login info', 'Login Successful') and self.success()
        else:
            messagebox.showerror("Invalid", "Invalid Username and Password")
 
    # LOGIN USERNAME
    def on_enter(self, event):
        if self.username.get() == 'Username':
            self.username.delete(0, 'end')
 
    def on_leave(self, event):
        if self.username.get() == '':
            self.username.insert(0, 'Username')
 
    # LOGIN PASSWORD
    def on_enter_password(self, event):
        if self.password.get() == 'Password':
                self.password.delete(0, 'end')
                self.password.config(show="*")
 
    def on_leave_password(self, event):
        if self.password.get() == '':
            self.password.insert(0, 'Password')
            self.password.config(show="")
 
    def on_type(self, event):
        if self.password.get() != 'Password':
            self.password.config(show="*")
        else:
            self.password.config(show="")
	
	
    def logintable(self):
        connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-QD6VG7S\SQLEXPRESS;DATABASE=Database_Project;Trusted_Connection=True')

        self.base = connection
        self.cur = self.base.cursor()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM MEMBERS") 
        sonuc = cursor.fetchall()
        for i in sonuc:
            print(i)

    # LOGIN SUCCESS
    def success(self):
        self.loginw.quit()


