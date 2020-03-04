"""
CIS 422 Project 2: User Interface File

Last Modified: 3/3/20

Authors: Olivia Pannell and Ben Verney
"""

# Imports
from tkinter import *
from tkinter import Text, messagebox

import compatibility as c
from database import *

# Specific font variables
SMALL_FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 50, "bold")
TAB_FONT = ("Helvetica", 18, "bold italic")
MATCH_FONT = ("Times", 15, "bold italic")

# List of Majors/Subjects
MAJORS = {"Accounting", "Anthropology", "Architecture", "Art", "Art and technology", "Art history", "Arts management",
		   "Asian studies", "Biochemistry", "Biology", "Business administration", "Chemistry", "Chinese", "Cinema studies",
		   "Classics", "Communication disorders and sciences", "Comparative literature", "Computer and information science",
		   "Dance", "Earth sciences", "Economics", "Educational foundations", "English", "Environmental science","Environmental studies",
		   "Ethnic studies", "Family and human services", "Folklore and public culture", "French", 'General science',
		   "General social science", "Geography", "German", "History", "Humanities", "Human physiology", "Interior architecture",
		   "International studies", "Italian", "Japanese", "Journalism", "Journalism: advertising", "Journalism: mediastudies",
		   "Journalism: public relations", "Judaic studies", "Landscape architecture", "Latin American studies", "Linguistics",
		   "Marine biology", "Mathematics", "Mathematics and computer science", "Medieval studies", "Music", "Music composition",
		   "Music education", "Music: jazz studies", "Music performance", "Philosophy", "Physics", "Planning, public policy and management",
		   "Political science", "Product design", "Psychology", "Religious studies", "Romance languages", "Russian, East European, and Eurasian studies",
		   "Sociology", "Spanish", "Spatial data science and technology", "Theater arts", "Women's, gender, and sexuality studies"}

questionnaireAnswers = {"gender": -1, "matchgender": -1, "careerfield": "", "timeinvestment": -1,"experiencelevel": -1,
						"networkingskills": -1, "orginizationalskills": -1, "communicationskills": -1, "timemanagementskills": -1,
						"integrity": -1, "patience": -1, "social": -1, "learningstyle": -1, "careergoals": -1, "kindofwork": -1}


'''
TO DO CREATE USER CLASS AND ADD TO IT
'''
#Creates current_user as a user class
# current_user = c.User()
'''
POTENTIAL COLOR THEMES
salmon
medium sea green
0d7e83
'''

# Main class that controls which frame is on top (shown to the user)
# in any given instance
class start(Tk):

	def __init__(self, *args, **kwargs):
		global questionnaireAnswers

		Tk.__init__(self, *args, **kwargs)
		container = Frame(self, height=500, width=450, bg="medium sea green")

		container.pack(side="top", fill="both", expand=True)
		self.pages = {}

		for page in (MainMenu, HelpPage, LoginPage, SignUpPage, HomePage, QuestionPage, QuestionPage2, ProfilePage):
			frame = page(container, self)
			self.pages[page] = frame
			frame.place(relx=0.0, rely=0.0, height=425, width=600)
			frame.config(bg='medium sea green')

		self.show_frame(MainMenu)

	def show_frame(self, controller):
		frame = self.pages[controller]
		frame.tkraise()

# Contains everything for the Main Menu frame
class MainMenu(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)

		lbl2 = Label(self, text='Meet your new best friend TODAY!', bg="medium sea green", fg="white", font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)

		b0 = Button(self, text="Login", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(LoginPage))
		b0.place(relx=0.5, rely=0.40, width=150, anchor=CENTER)

		b1 = Button(self, text="Sign-Up", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(SignUpPage))
		b1.place(relx=0.5, rely=0.50, width=150, anchor=CENTER)

		b2 = Button(self, text="Help", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(HelpPage))
		b2.place(relx=0.0, rely=1.0, anchor=SW)

# Contains everything for the Help frame
class HelpPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='THIS IS THE HELP PAGE', bg="medium sea green", fg="white", font=TAB_FONT)
		lbl1.place(relx=0.5, rely=0.30, anchor=CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

# Contains everything for the Login Page frame
class LoginPage(Frame):

	def __init__(self, parent, controller):
		global username1
		global userlbl
		global password1
		global passlbl

		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)

		lbl2 = Label(self, text='Meet your new best friend TODAY!', bg="medium sea green", fg="white", font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		userlbl = Label(self, text='Username:', bg="medium sea green", fg="white", font=SMALL_FONT)
		userlbl.place(relx=0.30, rely=0.40, anchor=CENTER)

		username1 = Entry(self)
		username1.place(relx=0.55, rely=0.40, anchor=CENTER)

		passlbl = Label(self, text='Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		passlbl.place(relx=0.30, rely=0.50, anchor=CENTER)

		password1 = Entry(self, show='*')
		password1.place(relx=0.55, rely=0.50, anchor=CENTER)

		log = Button(self, text="Login", highlightbackground="medium sea green", padx=10,
					 command=lambda: self.loginerror(parent, controller))
		log.place(relx=0.62, rely=0.62, anchor=SW)

	# Checking if username and password entrys were filled out before
	# clicking login
	def loginerror(self, parent, controller):
		global username1
		global password1
		global userlbl
		global passlbl

		# Error message that displays if at least one of the Username/Password
		# entries are not filled out
		errorlbl = Label(self, text='        *Please fill out all sections.    ', bg="medium sea green", fg="red4", font=SMALL_FONT)
		errorlbl2 = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the username entry is empty turn text red
		if not username1.get():
			userlbl.config(text='*Username:', fg='red4')
			errorlbl.place(relx=0.47, rely=0.59, anchor=CENTER)

		# If the password entry is empty turn text red
		if not password1.get():
			passlbl.config(text='*Password:', fg='red4')
			errorlbl.place(relx=0.47, rely=0.59, anchor=CENTER)

		# Resets previous username error text
		if username1.get():
			userlbl.config(text='Username:', fg='white')

		# Resets previous password error text
		if password1.get():
			passlbl.config(text='Password:', fg='white')

		# If both are filled out
		if username1.get() and password1.get():
			# Checks if the username and password are in the database
			valid = c.login_check(username1.get(), password1.get())
			if valid:
				# If they are get rid of error messages and call the homepage
				errorlbl = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="medium sea green",
							 font=SMALL_FONT)
				errorlbl.place(relx=0.47, rely=0.59, anchor=CENTER)
				# Check to see if current user is mentor or mentee
				# Guides them to corresponding page
				controller.show_frame(HomePage)
			else:
				errorlbl2.place(relx=0.47, rely=0.59, anchor=CENTER)


# Contains everything for the Sign Up Page frame
class SignUpPage(Frame):

	def __init__(self, parent, controller):
		global newusername
		global newpassword
		global newemail
		global passcheck
		global newuserlbl
		global newpasslbl
		global newemaillbl
		global pclbl

		Frame.__init__(self, parent)
		lbl1 = Label(self, text='MENTOR SHIT', bg="medium sea green", fg="white", font=TITLE_FONT)
		lbl1.place(relx=0.5, rely=0.20, anchor=CENTER)

		lbl2 = Label(self, text='Welcome! Create your new account now!', bg="medium sea green", fg="white",
					 font=SMALL_FONT)
		lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					command=lambda: self.signuperror(parent, controller))
		b2.place(relx=1.0, rely=1.0, anchor=SE)

		newuserlbl = Label(self, text='New Username:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newuserlbl.place(relx=0.28, rely=0.40, anchor=CENTER)

		newusername = Entry(self)
		newusername.place(relx=0.55, rely=0.40, anchor=CENTER)

		newpasslbl = Label(self, text='New Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newpasslbl.place(relx=0.28, rely=0.50, anchor=CENTER)

		newpassword = Entry(self, show='*')
		newpassword.place(relx=0.55, rely=0.50, anchor=CENTER)

		newemaillbl = Label(self, text='Email:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newemaillbl.place(relx=0.28, rely=0.70, anchor=CENTER)

		newemail = Entry(self)
		newemail.place(relx=0.55, rely=0.70, anchor=CENTER)

		pclbl = Label(self, text='Re-Enter Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		pclbl.place(relx=0.28, rely=0.60, anchor=CENTER)

		passcheck = Entry(self, show = '*')
		passcheck.place(relx=0.55, rely=0.60, anchor=CENTER)

	# Error checking on the signup page
	def signuperror(self, parent, controller):
		global newusername
		global newpassword
		global newemail
		global passcheck
		global newuserlbl
		global newpasslbl
		global newemaillbl
		global pclbl

		# Error message that displays if at least one of the entry fields is not
		# filled in.
		# Spaces are used here to fully cover larger error labels
		errorlbl = Label(self, text='              *Please fill out all sections.              ', 
			bg="medium sea green", fg="red4", font=SMALL_FONT)
 
		# Error message that displays if password and password check dont match.
		errorlbl2 = Label(self, text='*Passwords did not match. Please try again.', 
			bg="medium sea green", fg="red4", font=SMALL_FONT)

		# Error message that displays if password and password check dont match.
		errorlbl3 = Label(self, text='           *Invalid email. Please try again.         ', 
			bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the username entry is empty turn text red, else white
		if not newusername.get():
			newuserlbl.config(text='*New Username:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.80, anchor=CENTER)
		else:
			newuserlbl.config(text='Username:', fg='white')

		# If the password entry is empty turn text red, else white
		if not newpassword.get():
			newpasslbl.config(text='*New Password:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			newpasslbl.config(text='New Password:', fg='white')

		# If the user does not enter the password twice it turns red, else white
		if not passcheck.get():
			pclbl.config(text='*Re-Enter Password:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			pclbl.config(text='Re-Enter Password:', fg='white')

		# If the email entry is empty turn text red, else white
		if not newemail.get():
			newemaillbl.config(text='*Email:', fg='red4')
			errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
		else:
			newemaillbl.config(text='Email:', fg='white')

		# If all entries are filled out
		if newusername.get() and newpassword.get() and passcheck.get() and newemail.get():
			# Check for password and password check to match
			if newpassword.get() == passcheck.get():
				#Check for valid email with @
				at = "@"
				if newemail.get().count(at):
					# -------------TO DO------------------
					#		
					#		  ADD TO DATABASE
					# current_user.username = newusername.get()
					# current_user.password = newpassword.get()
					# current_user.email = newemail.get()
					errorlbl = Label(self, text='*Passwords did not match. Please try again.', bg="medium sea green", fg="medium sea green",
								 font=SMALL_FONT)
					errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
					controller.show_frame(QuestionPage)
				else:
					newemaillbl.config(text='*Email:', fg='red4')
					errorlbl3.place(relx=0.50, rely=0.8, anchor=CENTER)
			else:
				newpasslbl.config(text='*New Password:', fg='red4')
				pclbl.config(text='*Re-Enter Password:', fg='red4')
				errorlbl2.place(relx=0.50, rely=0.8, anchor=CENTER)

# Contains everything for the Home Page frame
# This is where the user can see pontential mentors/mentees
class HomePage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		b0 = Button(self, text="Potential Mentors", width=30, font=TAB_FONT)
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)

		b1 = Button(self, text="Profile", padx=50, font=TAB_FONT, command=lambda: controller.show_frame(ProfilePage))
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)

		b2 = Button(self, text="Logout", padx=40, font=TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)

		# First given mentor
		fr1 = Frame(self, width=570, height=60, bg='white')
		fr1.place(relx=0.50, rely=0.15, anchor=CENTER)

		userlbl = Label(fr1, text='First Last', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.2, rely=0.25, anchor=CENTER)

		userlbl2 = Label(fr1, text='Bio Bio Bio BIo BIO BIo Bio bio Bouioioio', fg="grey", font=SMALL_FONT)
		userlbl2.place(relx=0.2, rely=0.75, anchor=CENTER)

		b2 = Button(fr1, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr1, text="Connect", padx=25, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)

	# #Second given mentor
	# fr2 = Frame(self, width = 570, height = 40, bg = 'white')
	# fr2.place(relx=0.50, rely=0.27, anchor=CENTER)

	# #Third given mentor
	# fr3 = Frame(self, width = 570, height = 40, bg = 'white')
	# fr3.place(relx=0.50, rely=0.39, anchor=CENTER)

	# #Fourth given mentor
	# fr4 = Frame(self, width = 570, height = 40, bg = 'white')
	# fr4.place(relx=0.50, rely=0.51, anchor=CENTER)

	# #Fifth given mentor
	# fr5 = Frame(self, width = 570, height = 40, bg = 'white')
	# fr5.place(relx=0.50, rely=0.63, anchor=CENTER)

# Contains everything for the First page of the questionaire page
class QuestionPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		global gender
		global matchgender
		global careerfield
		gender = IntVar()
		matchgender = IntVar()
		careerfield = StringVar()

		lbl1 = Label(self, text='Please answer the following questions\n so we can match you with a mentor:',
					 bg="medium sea green", fg="white", font=TAB_FONT)
		lbl1.place(relx=0.5, rely=.05, anchor=N)

		lbl1 = Label(self, text='What is your gender?', bg="medium sea green", fg="white", font=MATCH_FONT)
		lbl1.place(relx=0.05, rely=0.27, anchor=W)

		maleRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green",
							 activebackground="medium sea green", variable=gender, value=1,
							 command=lambda: self.removeinputgender())
		maleRB.place(relx=0.1, rely=0.34, anchor=W)

		femaleRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green",
							   activebackground="medium sea green", variable=gender, value=2,
							   command=lambda: self.removeinputgender())
		femaleRB.place(relx=0.1, rely=0.41, anchor=W)

		selfidentifyRB = Radiobutton(self, text="Self Identify:", bg="medium sea green", selectcolor="medium sea green",
									 activebackground="medium sea green", variable=gender, value=3,
									 command=lambda: self.placeinputgender())
		selfidentifyRB.place(relx=0.1, rely=0.48, anchor=W)

		matchgender = Label(self, text='Who do you want to be\n matched with?', bg="medium sea green", fg="white",
							font=MATCH_FONT)
		matchgender.place(relx=0.53, rely=0.27, anchor=W)

		malematchRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=matchgender, value=1, tristatevalue=0)
		malematchRB.place(relx=0.58, rely=0.34, anchor=W)

		femalematchRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green",
									activebackground="medium sea green", variable=matchgender, value=2, tristatevalue=0)
		femalematchRB.place(relx=0.58, rely=0.41, anchor=W)

		everyonematchRB = Radiobutton(self, text="Everyone", bg="medium sea green", selectcolor="medium sea green",
									  activebackground="medium sea green", variable=matchgender, value=3,
									  tristatevalue=0)
		everyonematchRB.place(relx=0.58, rely=0.48, anchor=W)

		majorLabel = Label(self, text='What is your career field?', bg="medium sea green", fg="white",
							font=MATCH_FONT)
		majorLabel.place(relx=0.1, rely=0.62, anchor=W)

		# Sets initial drop down option to say "Choose one"
		# This does not show in the list of options.
		careerfield.set("Choose One...")
		majoroptions = OptionMenu(self, careerfield, *MAJORS)

		#Changes the colors of the background to match our theme
		majoroptions.config(bg = 'medium sea green')

		# Changes the drop down font color to be green, 
		# we can change this if you dont like it!
		majoroptions["menu"].config(bg = 'medium sea green')
		majoroptions.place(relx=0.1, rely=0.70, anchor=W)


		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					  command=lambda: [controller.show_frame(QuestionPage2), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					  command=lambda: [controller.show_frame(SignUpPage), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		global inputgender
		inputgender = Entry(self)

	def save(self):
		global questionnaireAnswers
		global gender
		global matchgender
		global careerfield
		questionnaireAnswers["gender"] = gender
		questionnaireAnswers["matchgender"] = matchgender
		questionnaireAnswers["careerfield"] = careerfield

	def placeinputgender(self):
		global inputgender
		inputgender.place(relx=0.13, rely=0.54, anchor=W)

	def removeinputgender(self):
		global inputgender
		inputgender.place_forget()


class QuestionPage2(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		lbl1 = Label(self, text='Question Page 2', bg="medium sea green", fg="white", font=TAB_FONT)
		lbl1.place(relx=0.5, rely=0.30, anchor=CENTER)

		b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: controller.show_frame(QuestionPage))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		b2 = Button(self, text="Test", highlightbackground="medium sea green", padx=10,
					command=lambda: print(questionnaireAnswers["careerfield"].get()))
		b2.pack()

class ProfilePage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		b0 = Button(self, text = "Potential Mentors", width = 30, font = TAB_FONT, command=lambda: controller.show_frame(HomePage))
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)

		b1 = Button(self, text="Profile", padx = 50, font = TAB_FONT)
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)

		b2 = Button(self, text="Logout", padx = 40, font = TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)

		fr1 = Frame(self, width = 570, height = 380, bg = 'white')
		fr1.place(relx=0.50, rely=0.52, anchor=CENTER)


win = start()
win.geometry('600x425')
win.title("Mentor Meeter")
win.config(bg='medium sea green')
win.mainloop()

'''
RESOURCES:
https://pythonprogramming.net/change-show-new-frame-tkinter/

'''
