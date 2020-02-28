
from tkinter import *
from tkinter import Text, messagebox

SMALL_FONT= ("Helvetica", 12)
TITLE_FONT= ("Helvetica", 50, "bold")
TAB_FONT= ("Helvetica", 18, "bold italic")
MATCH_FONT= ("Times", 15, "bold italic")

'''
POTENTIAL COLOR THEMES
salmon
medium sea green
0d7e83
'''


class start(Tk):

	def __init__(self, *args, **kwargs):

		Tk.__init__(self, *args, **kwargs)
		container = Frame(self, height = 500, width = 450, bg = "medium sea green")

		container.pack(side="top", fill="both", expand = True)
		self.pages = {}

		for page in (MainMenu, HelpPage, LoginPage, SignUpPage, HomePage, QuestionPage):

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
		lbl1 = Label(self, text='THIS IS THE HELP PAGE', bg="medium sea green", fg="white", font = TAB_FONT)
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

		log = Button(self, text="Login", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(HomePage))
		log.place(relx=0.62, rely=0.62, anchor=SW)

	# def error(self, parent, controller):


class SignUpPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font = TITLE_FONT)
		lbl1.place(relx = 0.5, rely = 0.20, anchor = CENTER)

		lbl2 = Label(self, text='Welcome! Create your new account now!', bg="medium sea green", fg="white", font = SMALL_FONT)
		lbl2.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(QuestionPage))
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
		

class HomePage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		b0 = Button(self, text="Potential Mentors", width = 30, font = TAB_FONT)
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)

		b1 = Button(self, text="Profile", padx = 50, font = TAB_FONT)
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)

		b2 = Button(self, text="Logout", padx = 40, font = TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)
 		
 		#First given mentor
		fr1 = Frame(self, width = 570, height = 40, bg = 'white')
		fr1.place(relx=0.50, rely=0.15, anchor=CENTER)

		userlbl = Label(fr1, text='MENTORS GO HERE', fg="black", font = MATCH_FONT)
		userlbl.place(relx=0.2, rely=0.25, anchor=CENTER)


		#Second given mentor
		fr2 = Frame(self, width = 570, height = 40, bg = 'white')
		fr2.place(relx=0.50, rely=0.27, anchor=CENTER)

		#Third given mentor
		fr3 = Frame(self, width = 570, height = 40, bg = 'white')
		fr3.place(relx=0.50, rely=0.39, anchor=CENTER)

		#Fourth given mentor
		fr4 = Frame(self, width = 570, height = 40, bg = 'white')
		fr4.place(relx=0.50, rely=0.51, anchor=CENTER)

		#Fifth given mentor
		fr5 = Frame(self, width = 570, height = 40, bg = 'white')
		fr5.place(relx=0.50, rely=0.63, anchor=CENTER)

class QuestionPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='ASK QUESTIONS FOR QUESTIONNAIRE', bg="medium sea green", fg="white", font = TAB_FONT)
		lbl1.place(relx = 0.5, rely = 0.30, anchor = CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10, command=lambda: controller.show_frame(SignUpPage))
		b0.place(relx=0.0, rely=1.0, anchor=SW)



win = start()
win.geometry('600x425')
win.title("Mentor Meeter")
win.config(bg = 'medium sea green')
win.mainloop()

'''
RESOURCES:
https://pythonprogramming.net/change-show-new-frame-tkinter/

'''

