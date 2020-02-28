
from tkinter import *
from tkinter import Text, messagebox

#DELETE THIS WHEN CAN
LARGE_FONT= ("Helvetica", 12)
SMALL_FONT= ("Helvetica", 12)
TITLE_FONT= ("Helvetica", 50, "bold")

class start(Tk):

	def __init__(self, *args, **kwargs):

		Tk.__init__(self, *args, **kwargs)
		container = Frame(self, height = 500, width = 450, bg = "medium sea green")

		container.pack(side="top", fill="both", expand = True)
		self.pages = {}

		for page in (MainMenu, HelpPage, LoginPage, SignUpPage):

			frame = page(container, self)
			self.pages[page] = frame
			frame.place(relx = 0.0, rely = 0.0, height = 425, width = 600)
			frame.config(bg = 'medium sea green')

		self.show_frame(MainMenu)

	def show_frame(self, controller):
		frame = self.pages[controller]
		frame.tkraise()

        
class MainMenu(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font = TITLE_FONT)
		lbl1.place(relx = 0.5, rely = 0.20, anchor = CENTER)

		lbl2 = Label(self, text='Meet your new best friend TODAY!', bg="medium sea green", fg="white", font = SMALL_FONT)
		lbl2.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Login", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(LoginPage))
		b0.place(relx=0.5, rely=0.40, width = 150,  anchor=CENTER)

		b1 = Button(self, text="Sign-Up", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(SignUpPage))
		b1.place(relx=0.5, rely=0.50, width = 150, anchor=CENTER)


		b2 = Button(self, text="Help", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(HelpPage))
		b2.place(relx=0.0, rely=1.0, anchor=SW)


class HelpPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='THIS IS THE HELP PAGE', bg="medium sea green", fg="white", font = SMALL_FONT)
		lbl1.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)


class LoginPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font = TITLE_FONT)
		lbl1.place(relx = 0.5, rely = 0.20, anchor = CENTER)

		lbl2 = Label(self, text='Meet your new best friend TODAY!', bg="medium sea green", fg="white", font = SMALL_FONT)
		lbl2.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		userlbl = Label(self, text='Username:', bg="medium sea green", fg="white", font = SMALL_FONT)
		userlbl.place(relx=0.30, rely=0.40, anchor=CENTER)

		username = Entry(self)
		username.place(relx=0.55, rely=0.40, anchor=CENTER)

		passlbl = Label(self, text='Password:', bg="medium sea green", fg="white", font = SMALL_FONT)
		passlbl.place(relx=0.30, rely=0.50, anchor=CENTER)

		password = Entry(self)
		password.place(relx=0.55, rely=0.50, anchor=CENTER)

		log = Button(self, text="Login", highlightbackground="medium sea green", padx=10)
		log.place(relx=0.62, rely=0.62, anchor=SW)

class SignUpPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font = TITLE_FONT)
		lbl1.place(relx = 0.5, rely = 0.20, anchor = CENTER)

		lbl2 = Label(self, text='Welcome! Create your new account now!', bg="medium sea green", fg="white", font = SMALL_FONT)
		lbl2.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=1.0, rely=1.0, anchor=SE)

		userlbl = Label(self, text='New Username:', bg="medium sea green", fg="white", font = SMALL_FONT)
		userlbl.place(relx=0.30, rely=0.40, anchor=CENTER)

		username = Entry(self)
		username.place(relx=0.55, rely=0.40, anchor=CENTER)

		passlbl = Label(self, text='New Password:', bg="medium sea green", fg="white", font = SMALL_FONT)
		passlbl.place(relx=0.30, rely=0.50, anchor=CENTER)

		password = Entry(self)
		password.place(relx=0.55, rely=0.50, anchor=CENTER)

		userlbl = Label(self, text='New Username:', bg="medium sea green", fg="white", font = SMALL_FONT)
		userlbl.place(relx=0.30, rely=0.40, anchor=CENTER)

		username = Entry(self)
		username.place(relx=0.55, rely=0.40, anchor=CENTER)
		
		# log = Button(self, text="Login", highlightbackground="medium sea green", padx=10)
		# log.place(relx=0.62, rely=0.62, anchor=SW)

	    

	    


win = start()
win.geometry('600x425')
win.title("Mentor Meeter")
win.config(bg = 'medium sea green')
win.mainloop()

'''
RESOURCES:
https://pythonprogramming.net/change-show-new-frame-tkinter/

'''

