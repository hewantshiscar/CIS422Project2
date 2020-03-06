"""
CIS 422 Project 2: User Interface File

Last Modified: 3/6/20

Authors: Olivia Pannell and Ben Verney and Bethany Van Meter
"""

# Imports
from tkinter import *
from tkinter import Text, messagebox

import compatibility as c
from database import *

# Specific font variables
SMALL_FONT = ("Helvetica", 14)
TITLE_FONT = ("Helvetica", 50, "bold")
TAB_FONT = ("Helvetica", 18, "bold italic")
MATCH_FONT = ("Helvetica", 22, "bold")
PERCENT_FONT = ("Helvetica", 12, "bold italic")
QUESTION_FONT = ("Roboto", 15, "bold")
BUTTON_FONT = ("Helvetica", 10)
INFO_FONT = ("Helvetica", 16, "bold")

# List of Majors/Subjects
MAJORS = ["Accounting", "Anthropology", "Architecture", "Art", "Art and technology", "Art history", "Arts management",
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
		   "Sociology", "Spanish", "Spatial data science and technology", "Theater arts", "Women's, gender, and sexuality studies"]

questionnaireAnswers = {"gender": -1, "matchgender": -1, "userage": -1, "careerfield": -1, "agerange": -1, "timeinvestment": -1,"experiencelevel": -1,
						"networkingskills": -1, "orginizationalskills": -1, "communicationskills": -1, "timemanagementskills": -1,
						"workethic": -1, "flexibility": -1, "workwithothers": -1,
						"introvertextrovert": -1, "learningstyle": -1, "careergoals": -1, "kindofwork": -1}

#Creates new user as a user class
new_account = c.User(0, None, None, 0, None, {}, None, None, None, None)
# c_user = c.User(0, None, None, 0, None, {}, None, None, None, None)


'''
TESTING STUFF
'''
# user_type, first, last, age, gender, questionnaire, bio, email, username, password
test_account = c.User(0, "Oliviadls", "Pannelldsms", 21, "Female", [2, 3, 11, 4, 3, 2, 4, 5, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
	"Hello I am a student at university of Oregon and I am looking for a mentor who can help guide me through the difficulties of being a woman. ",
	"olivia@gmail.com", "olp", "fyeah")
c.users.append(test_account)

'''
POTENTIAL COLOR THEMES
salmon
medium sea green
0d7e83
'''

# this function is checking to make sure the email entered is the correct format
# returns True if email is in the correct format
def check_email(address):
        # check for the @ sign
        if ("@" in address):
                # split the string at the @ to be able to check the second part of the email
                address_split = address.split("@")
                # check if a . exists in the part of the email after the @
                if "." in address_split[1]:
                        # split again at the . to ensure there are characters behind and after the .
                        address_split_second = address_split[1].split(".")
                        if len(address_split_second[0]) >= 1 and len(address_split_second[1]) >= 1:
                                return True
        return False

# this checks if a username already exists in the database. Returns True if username is not taken
def check_username(username):
        for user in c.users:
                if username == user.username:
                        return False
        return True

# Main class that controls which frame is on top (shown to the user)
# in any given instance
class start(Tk):

	def __init__(self, *args, **kwargs):
		global questionnaireAnswers

		Tk.__init__(self, *args, **kwargs)
		container = Frame(self, height=500, width=450, bg="medium sea green")

		container.pack(side="top", fill="both", expand=True)
		self.pages = {}

		for page in (MainMenu, HelpPage, LoginPage, SignUpPage, HomePage, QuestionPage, QuestionPage2, ProfilePage,
					QuestionPage3, QuestionPage4, QuestionPage5, QuestionPage6, NamePreferencesPage):
			frame = page(container, self)
			self.pages[page] = frame
			frame.place(relx=0.0, rely=0.0, height=425, width=600)
			frame.config(bg='medium sea green')

		self.show_frame(MainMenu)

	def show_frame(self, controller):
		frame = self.pages[controller]
		frame.tkraise()

# Contains everything for the Main Menu frame
# This Includes a help button, and sign-in/login buttons.
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

# Contains everything for the Login Page frame.
# This is for the user who already has an existing account.
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

		# Quick way for testing to go to homepage
		debug = True
		if(debug):
			controller.show_frame(HomePage)
			return

		# Error message that displays if at least one of the Username/Password
		# entries are not filled out
		errorlbl = Label(self, text='        *Please fill out all sections.    ', bg="medium sea green", fg="red4", font=SMALL_FONT)
		errorlbl2 = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="red4", font=SMALL_FONT)

		# If the username entry is empty turn text red
		if not username1.get():
			userlbl.config(text='*Username:', fg='red4')
			errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)

		# If the password entry is empty turn text red
		if not password1.get():
			passlbl.config(text='*Password:', fg='red4')
			errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)

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
				# Clears password entry for security reasons
				password1.delete(0, 'end')
				print("Welcome!")
				# If they are get rid of error messages and call the homepage
				errorlbl = Label(self, text='*Incorrect Password or Username.', bg="medium sea green", fg="medium sea green",
							 font=SMALL_FONT)
				errorlbl.place(relx=0.43, rely=0.59, anchor=CENTER)
				# Check to see if current user is mentor or mentee
				# Guides them to corresponding page
				controller.show_frame(HomePage)
			else:
				errorlbl2.place(relx=0.43, rely=0.59, anchor=CENTER)

# Contains everything for the Sign Up Page frame.
# This is where the user can create a new account.
class NamePreferencesPage(Frame):

        def __init__(self, parent, controller):
                global firstname
                global lastname
                global mentormentee
                global firstnamelbl
                global lastnamelbl
                global mentormenteelbl

                Frame.__init__(self, parent)

                lbl2 = Label(self, text='Please fill out all fields:', bg="medium sea green", fg="white",
                                         font=SMALL_FONT)
                lbl2.place(relx=0.5, rely=0.30, anchor=CENTER)

                b0 = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
                                        command=lambda: controller.show_frame(SignUpPage))
                b0.place(relx=0.0, rely=1.0, anchor=SW)

                b2 = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
                                        command=lambda: self.signuperror(parent, controller))
                b2.place(relx=1.0, rely=1.0, anchor=SE)

                firstnamelbl = Label(self, text='First name:', bg="medium sea green", fg="white", font=SMALL_FONT)
                firstnamelbl.place(relx=0.272, rely=0.40, anchor=CENTER)

                firstname = Entry(self)
                firstname.place(relx=0.55, rely=0.40, anchor=CENTER)

                lastnamelbl = Label(self, text='Last name:', bg="medium sea green", fg="white", font=SMALL_FONT)
                lastnamelbl.place(relx=0.275, rely=0.50, anchor=CENTER)

                lastname = Entry(self)
                lastname.place(relx=0.55, rely=0.50, anchor=CENTER)

                mentormentee = StringVar()

                mentormenteelbl = Label(self, text='Are you looking to be a mentor or mentee?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
                mentormenteelbl.place(relx=0.15, rely=0.63, anchor=W)

                mentorrb = Radiobutton(self, text="Mentor", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
								  activebackground="medium sea green", variable=mentormentee, value=1, tristatevalue=2)
                mentorrb.place(relx=0.3, rely=0.7, anchor=W)
                
                menteerb = Radiobutton(self, text="Mentee", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
									activebackground="medium sea green", variable=mentormentee, value=0, tristatevalue=2)
                menteerb.place(relx=0.6, rely=0.7, anchor=W)


        # Error checking on the signup page
        def signuperror(self, parent, controller):
                global firstname
                global lastname
                global mentormentee
                global firstnamelbl
                global lastnamelbl
                global mentormenteelbl

                #debug code so i dont have to enter a password every time i want to check the questionanaire
                #set debug = true to bypass the create account check.
                debug = True
                if(debug):
                        controller.show_frame(QuestionPage)
                        return

                # Error message that displays if at least one of the entry fields is not
                # filled in.
                # Spaces are used here to fully cover larger error labels
                errorlbl = Label(self, text='              *Please fill out all sections.              ', 
                        bg="medium sea green", fg="red4", font=SMALL_FONT)

                # If the first name entry is empty turn text red, else white
                if not firstname.get():
                        firstnamelbl.config(text='*First name:', fg='red4')
                        errorlbl.place(relx=0.50, rely=0.80, anchor=CENTER)
                else:
                        firstnamelbl.config(text='First name:', fg='white')

                # If the last name entry is empty turn text red, else white
                if not lastname.get():
                        lastnamelbl.config(text='*Last name:', fg='red4')
                        errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
                else:
                        lastnamelbl.config(text='Last name:', fg='white')

                # If the mentor/mentee entry is empty turn text red, else white
                if not mentormentee.get():
                        mentormenteelbl.config(text='*Are you looking to be a mentor or mentee?', fg='red4')
                        mentormenteelbl.place(relx=0.15, rely=0.63, anchor=W)
                else:
                        mentormenteelbl.config(text='Are you looking to be a mentor or mentee?', fg='white')

                # If all entries are filled out
                if firstname.get() and lastname.get() and mentormentee.get():
                        # add information to user class to be later added into database
                        c.current_user.first = firstname.get()
                        new_account.first = firstname.get()
                        new_account.last = lastname.get()
                        new_account.user_type = mentormentee.get()

                        controller.show_frame(QuestionPage)


# Contains everything for the Sign Up Page frame.
# This is where the user can create a new account.
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
		newuserlbl.place(relx=0.272, rely=0.40, anchor=CENTER)

		newusername = Entry(self)
		newusername.place(relx=0.55, rely=0.40, anchor=CENTER)

		newpasslbl = Label(self, text='New Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newpasslbl.place(relx=0.275, rely=0.50, anchor=CENTER)

		newpassword = Entry(self, show='*')
		newpassword.place(relx=0.55, rely=0.50, anchor=CENTER)

		pclbl = Label(self, text='Re-Enter Password:', bg="medium sea green", fg="white", font=SMALL_FONT)
		pclbl.place(relx=0.25, rely=0.60, anchor=CENTER)

		passcheck = Entry(self, show = '*')
		passcheck.place(relx=0.55, rely=0.60, anchor=CENTER)

		newemaillbl = Label(self, text='Email:', bg="medium sea green", fg="white", font=SMALL_FONT)
		newemaillbl.place(relx=0.325, rely=0.70, anchor=CENTER)

		newemail = Entry(self)
		newemail.place(relx=0.55, rely=0.70, anchor=CENTER)

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

		#debug code so i dont have to enter a password every time i want to check the questionanaire
		#set debug = true to bypass the create account check.
		debug = True
		if(debug):
			controller.show_frame(NamePreferencesPage)
			return


		# Error message that displays if at least one of the entry fields is not
		# filled in.
		# Spaces are used here to fully cover larger error labels
		errorlbl = Label(self, text='              *Please fill out all sections.              ', 
			bg="medium sea green", fg="red4", font=SMALL_FONT)
 
		# Error message that displays if password and password check dont match.
		errorlbl2 = Label(self, text='*Passwords did not match. Please try again.', 
			bg="medium sea green", fg="red4", font=SMALL_FONT)

		# Error message that displays if email check doesn't pass.
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
				#Check for valid email with @ -> newemail.get().count(at)
				if check_email(newemail.get()):
                                        # Check to ensure the username is not taken
                                        if check_username(newusername.get()):
                                                # add information to user class to be later added into database
                                                #c.current_user = c.User(0, None, None, 0, None, {}, None, None, None, None)
                                                c.current_user.username = newusername.get()
                                                new_account.username = newusername.get()
                                                new_account.password = newpassword.get()
                                                new_account.email = newemail.get()

                                                # Clears password entry for security reasons
                                                # newpassword.delete(0, 'end')
                                                # passcheck.delete(0, 'end')
                                                errorlbl = Label(self, text='*Passwords did not match. Please try again.', bg="medium sea green", fg="medium sea green",
                                                			 font=SMALL_FONT)
                                                errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
                                                controller.show_frame(NamePreferencesPage)
                                        else:
                                                errorlbl.config(text='*Username is taken, please enter a new username', fg='red4')
                                                errorlbl.place(relx=0.50, rely=0.8, anchor=CENTER)
				else:
					newemaillbl.config(text='*Email:', fg='red4')
					errorlbl3.place(relx=0.50, rely=0.8, anchor=CENTER)
			else:
				newpasslbl.config(text='*New Password:', fg='red4')
				pclbl.config(text='*Re-Enter Password:', fg='red4')
				errorlbl2.place(relx=0.50, rely=0.8, anchor=CENTER)
				

# Contains everything for the Mentee Home Page frame.
# This is where the user can see pontential mentors.
class HomePage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		b0 = Button(self, text="Potential Mentors", width=30, font=TAB_FONT)
		b0.place(relx=0.25, rely=0.02, anchor=CENTER)

		b1 = Button(self, text="Profile", padx=50, font=TAB_FONT, command=lambda: controller.show_frame(ProfilePage))
		b1.place(relx=0.65, rely=0.02, anchor=CENTER)

		b2 = Button(self, text="Logout", padx=40, font=TAB_FONT, command=lambda: controller.show_frame(MainMenu))
		b2.place(relx=0.90, rely=0.02, anchor=CENTER)

		'''
		TO DO:
		FIND MENTORS/MENTEES
		FROM CURRENT USERS MATCHES
		REPLACE USERLBL TEXT WITH MATCH FIRST AND LAST 

		ALSO NEED TO CHANGE THE CONNECT BUTTONS SO THAT
		THEY CALL CONNECTWIN(MENTOR FIRST NAME, MENTOR LAST NAME,
		MENTOR EMAIL)
		'''

		# First given mentor
		fr1 = Frame(self, width=570, height=70, bg='white')
		fr1.place(relx=0.50, rely=0.17, anchor=CENTER)

		userlbl = Label(fr1, text='Kelly Tellyphony', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.05, rely=0.3, anchor=W)

		userlbl = Label(fr1, text='Compatibility: 99%', fg="grey40", font=PERCENT_FONT)
		userlbl.place(relx=0.05, rely=0.7, anchor=W)

		b2 = Button(fr1, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr1, text="Connect", padx=25, font=SMALL_FONT,
			command=lambda: connect("Kelly", "Telly", "Ktellyphony@gmail.com"))
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)

		#Second given mentor
		fr2 = Frame(self, width = 570, height = 70, bg = 'white')
		fr2.place(relx=0.50, rely=0.35, anchor=CENTER)

		userlbl = Label(fr2, text='Leanna Phillips', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.05, rely=0.3, anchor=W)

		userlbl = Label(fr2, text='Compatibility: 87%', fg="grey40", font=PERCENT_FONT)
		userlbl.place(relx=0.05, rely=0.7, anchor=W)

		b2 = Button(fr2, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr2, text="Connect", padx=25, font=SMALL_FONT,
			command=lambda: connect("Leanna", "Phillips", "LPPP@gmail.com"))
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Third given mentor
		fr3 = Frame(self, width = 570, height = 70, bg = 'white')
		fr3.place(relx=0.50, rely=0.53, anchor=CENTER)

		userlbl = Label(fr3, text='Hallam Barron', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.05, rely=0.3, anchor=W)

		userlbl = Label(fr3, text='Compatibility: 87%', fg="grey40", font=PERCENT_FONT)
		userlbl.place(relx=0.05, rely=0.7, anchor=W)

		b2 = Button(fr3, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr3, text="Connect", padx=25, font=SMALL_FONT,
			command=lambda: connect("Hallam", "Barron", "Barron@gmail.com"))
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Fourth given mentor
		fr4 = Frame(self, width = 570, height = 70, bg = 'white')
		fr4.place(relx=0.50, rely=0.71, anchor=CENTER)

		userlbl = Label(fr4, text='Damian Steele', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.05, rely=0.3, anchor=W)

		userlbl = Label(fr4, text='Compatibility: 70%', fg="grey40", font=PERCENT_FONT)
		userlbl.place(relx=0.05, rely=0.7, anchor=W)

		b2 = Button(fr4, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr4, text="Connect", padx=25, font=SMALL_FONT,
			command=lambda: connect("Damian", "Steele", "DSTEElee@gmail.com"))
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)


		#Fifth given mentor
		fr5 = Frame(self, width = 570, height = 70, bg = 'white')
		fr5.place(relx=0.50, rely=0.89, anchor=CENTER)

		userlbl = Label(fr5, text='Sheikh Hopkins', fg="black", font=MATCH_FONT)
		userlbl.place(relx=0.05, rely=0.3, anchor=W)

		userlbl = Label(fr5, text='Compatibility: 70%', fg="grey40", font=PERCENT_FONT)
		userlbl.place(relx=0.05, rely=0.7, anchor=W)

		b2 = Button(fr5, text="Learn More...", padx=10, font=SMALL_FONT)
		b2.place(relx=0.90, rely=0.75, anchor=CENTER)

		b2 = Button(fr5, text="Connect", padx=25, font=SMALL_FONT, 
			command=lambda: connect("Sheikh", "Hopkins", "ShiekhH@gmail.com"))
		b2.place(relx=0.90, rely=0.25, anchor=CENTER)

	def learnmore(self):
		pass

# Contains everything for the First page of the questionaire page.
# After creating a new account the user answers questions from these
# pages to help match them up with similar mentors
class QuestionPage(Frame):

	#TODO: make sure all of the options are chosen before moving on to the next page

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		global gender
		global matchgender
		global careerfield
		global userage
		gender = IntVar()
		matchgender = IntVar()
		careerfield = StringVar()

		lbl1 = Label(self, text='Please answer the following questions so\nwe can match you with a mentor:',
					 bg="medium sea green", fg="white", font=("Roboto", 18, "bold"))
		lbl1.place(relx=0.05, rely=0.1, anchor=W)

		lbl1 = Label(self, text='What is your gender?', bg="medium sea green", fg="white", font=QUESTION_FONT)
		lbl1.place(relx=0.05, rely=0.27, anchor=W)

		maleRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green",
							 activebackground="medium sea green", variable=gender, value=1, font=BUTTON_FONT,
							 command=lambda: self.removeinputgender())
		maleRB.place(relx=0.1, rely=0.36, anchor=W)

		femaleRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green",
							   activebackground="medium sea green", variable=gender, value=2, font=BUTTON_FONT,
							   command=lambda: self.removeinputgender())
		femaleRB.place(relx=0.1, rely=0.43, anchor=W)

		selfidentifyRB = Radiobutton(self, text="Self Identify:", bg="medium sea green", selectcolor="medium sea green",
									 activebackground="medium sea green", variable=gender, value=3, font=BUTTON_FONT,
									 command=lambda: self.placeinputgender())
		selfidentifyRB.place(relx=0.1, rely=0.50, anchor=W)

		matchgenderLB = Label(self, text='Who do you want to be\n matched with?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
		matchgenderLB.place(relx=0.53, rely=0.27, anchor=W)

		#FIXME: this dumb tristate value bug is back
		malematchRB = Radiobutton(self, text="Male", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
								  activebackground="medium sea green", variable=matchgender, value=1, tristatevalue=0)
		malematchRB.place(relx=0.58, rely=0.36, anchor=W)

		femalematchRB = Radiobutton(self, text="Female", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
									activebackground="medium sea green", variable=matchgender, value=2, tristatevalue=0)
		femalematchRB.place(relx=0.58, rely=0.43, anchor=W)

		everyonematchRB = Radiobutton(self, text="Everyone", bg="medium sea green", selectcolor="medium sea green", font=BUTTON_FONT,
									  activebackground="medium sea green", variable=matchgender, value=3,
									  tristatevalue=0)
		everyonematchRB.place(relx=0.58, rely=0.50, anchor=W)

		majorLabel = Label(self, text='What is your career field?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
		majorLabel.place(relx=0.05, rely=0.62, anchor=W)

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


		#TODO: need to make sure people only enter intergers in this field
		enterage = Label(self, text='How old are you?', bg="medium sea green", fg="white",
							font=QUESTION_FONT)
		enterage.place(relx=0.53, rely=0.62, anchor=W)
		userage = Entry(self)
		userage.place(relx=0.58, rely=0.69, anchor=W)


		pagenum = Label(self, text='pg 1/5',bg="medium sea green", font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)


		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					  command=lambda: [controller.show_frame(QuestionPage2), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					  command=lambda: [controller.show_frame(NamePreferencesPage), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		global inputgender
		inputgender = Entry(self)

	#NOTE: BEN, WHEN NOTHING IS SELECTED FROM THIS PAGE AND YOU GO BACK
	# TO THE SIGNUP PAGE AN ERROR IS THROWN IN THE TERMINAL. I THINK IT IS
	# BECAUSE THE MAJOR LIST ISNT CHECKED TO MAKE SURE SOMETHING WAS ACTUALLY
	# SELECTED BEFORE SAVING IT
	def save(self):
		global questionnaireAnswers
		global gender
		global matchgender
		global careerfield
		global userage
		questionnaireAnswers["gender"] = gender.get()
		questionnaireAnswers["matchgender"] = matchgender.get()
		questionnaireAnswers["careerfield"] = MAJORS.index(careerfield.get())
		questionnaireAnswers["userage"] = userage.get()

	def placeinputgender(self):
		global inputgender
		inputgender.place(relx=0.13, rely=0.56, anchor=W)

	def removeinputgender(self):
		global inputgender
		inputgender.place_forget()

class QuestionPage2(Frame):

	def __init__(self, parent, controller):
		global agerange
		global timeinvestment
		global experiencelevel
		global networkingskills
		agerange = IntVar()
		timeinvestment = IntVar()
		experiencelevel = IntVar()
		networkingskills = IntVar()


		Frame.__init__(self, parent)

		#TODO: maybe allow them to select multiple age ranges? This is kind of limiting... but also hard to implement. Ask group.
		Label(self, text='What age range do you want to be matched with?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="18-25", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=agerange, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.17, anchor=W)

		Radiobutton(self, text="25-30", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.17, anchor=W)

		Radiobutton(self, text="30-40", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.17, anchor=W)

		Radiobutton(self, text="40-60", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.17, anchor=W)

		Radiobutton(self, text="60+", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=agerange, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.17, anchor=W)



		Label(self, text='How much time would you like to invest in your\nmentor-mentee relationship? (1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.3, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=timeinvestment, value=1, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=2, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=3, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=4, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timeinvestment, value=5, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='What is your experience level in your field?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=experiencelevel, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=experiencelevel, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How good are your networking skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=networkingskills, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.8, anchor=W)




		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
					command=lambda: [controller.show_frame(QuestionPage), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
					  command=lambda: [controller.show_frame(QuestionPage3), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 2/5', bg="medium sea green", font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)

	def save(self):
		global agerange
		global timeinvestment
		global experiencelevel
		global networkingskills
		questionnaireAnswers["agerange"] = agerange.get()
		questionnaireAnswers["timeinvestment"] = timeinvestment.get()
		questionnaireAnswers["experiencelevel"] = experiencelevel.get()
		questionnaireAnswers["networkingskills"] = networkingskills.get()

class QuestionPage3(Frame):

	def __init__(self, parent, controller):
		global kindofwork
		global networkingskills
		global orginizationalskills
		global communicationskills
		kindofwork = IntVar()
		networkingskills = IntVar()
		orginizationalskills = IntVar()
		communicationskills = IntVar()

		Frame.__init__(self, parent)


		Label(self, text='What kind of work do you want to do?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="Large corporate company", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.05, rely=0.17, anchor=W)

		Radiobutton(self, text="Startup/small business", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.35, rely=0.17, anchor=W)

		Radiobutton(self, text="Own your own business", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.65, rely=0.17, anchor=W)

		Radiobutton(self, text="Freelancer/contractor", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.2, rely=0.24, anchor=W)

		Radiobutton(self, text="Non-Profit", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=kindofwork, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.5, rely=0.24, anchor=W)



		Label(self, text='How good are your networking skills? (1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.3, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=networkingskills, value=1, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=2, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=3, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=4, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=networkingskills, value=5, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='How good are your orginizational skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=orginizationalskills, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=orginizationalskills, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How good are your communication skills?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=communicationskills, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=communicationskills, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.8, anchor=W)



		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage2), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage4), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 3/5', bg="medium sea green", font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)


	def save(self):
		global kindofwork
		global networkingskills
		global orginizationalskills
		global communicationskills
		questionnaireAnswers["kindofwork"] = kindofwork.get()
		questionnaireAnswers["networkingskills"] = networkingskills.get()
		questionnaireAnswers["orginizationalskills"] = orginizationalskills.get()
		questionnaireAnswers["communicationskills"] = communicationskills.get()

class QuestionPage4(Frame):

	def __init__(self, parent, controller):
		global careergoals
		global timemanagementskills
		global workethic
		global flexiblility
		careergoals = IntVar()
		timemanagementskills = IntVar()
		workethic = IntVar()
		flexiblility = IntVar()

		Frame.__init__(self, parent)


		Label(self, text='What is your prinary career goal?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.1, anchor=W)

		Radiobutton(self, text="Money", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=careergoals, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.17, anchor=W)

		Radiobutton(self, text="Happiness", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.22, rely=0.17, anchor=W)

		Radiobutton(self, text="Community", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.38, rely=0.17, anchor=W)

		Radiobutton(self, text="Stability", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.17, anchor=W)

		Radiobutton(self, text="Influence", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=careergoals, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.69, rely=0.17, anchor=W)



		Label(self, text='How good are your time management skills?\n(1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.28, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=timemanagementskills, value=1, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.1, rely=0.4, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=2, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.25, rely=0.4, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=3, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.4, rely=0.4, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=4, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.55, rely=0.4, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=timemanagementskills, value=5, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.7, rely=0.4, anchor=W)



		Label(self, text='How would you rate your work ethic?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.5, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=workethic, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.6, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.6, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.6, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.6, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workethic, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.6, anchor=W)



		Label(self, text='How flexible/adaptable are you?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.7, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=flexiblility, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.8, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.8, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.8, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.8, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=flexiblility, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.8, anchor=W)




		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage3), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage5), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 4/5', bg="medium sea green",  font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)


	def save(self):
		global careergoals
		global timemanagementskills
		global workethic
		global flexiblility
		questionnaireAnswers["careergoals"] = careergoals.get()
		questionnaireAnswers["timemanagementskills"] = timemanagementskills.get()
		questionnaireAnswers["workethic"] = workethic.get()
		questionnaireAnswers["flexibility"] = flexiblility.get()

class QuestionPage5(Frame):

	def __init__(self, parent, controller):
		global learningstyle
		global workwithothers
		#global patience
		global introvertextrovert
		learningstyle = IntVar()
		workwithothers = IntVar()
		#patience = IntVar()
		introvertextrovert = IntVar()

		Frame.__init__(self, parent)



		Label(self, text='What kind of learner are you?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.08, anchor=W)

		Radiobutton(self, text="Visual (Spatial): You prefer using pictures, images, and spatial understanding.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.15, anchor=W)

		Radiobutton(self, text="Aural (Auditory-Musical): You prefer using sound and music.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.22, anchor=W)

		Radiobutton(self, text="Verbal (Linguistic): You prefer using words, both in speech and writing", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.29, anchor=W)

		Radiobutton(self, text="Physical (Kinesthetic): You prefer using our body, hands, and sense of touch.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.36, anchor=W)

		Radiobutton(self, text="Logical (Mathematical): You prefer using logic, reasoning, and systems.", bg="medium sea green", selectcolor="medium sea green",
					activebackground="medium sea green", variable=learningstyle, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.43, anchor=W)



		Label(self, text='How would you rate your ablility to work with others?\n(1 = low, 5 = high)', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.55, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=workwithothers, value=1, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.1, rely=0.65, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=2, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.25, rely=0.65, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=3, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.4, rely=0.65, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=4, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.55, rely=0.65, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=workwithothers, value=5, font=BUTTON_FONT,  tristatevalue=0).place(relx=0.7, rely=0.65, anchor=W)


		"""
		Label(self, text='How patient are you?', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.59, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=patience, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.68, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=patience, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.68, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=patience, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.68, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=patience, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.68, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=patience, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.68, anchor=W)
		"""


		Label(self, text='How introverted/extroverted are you?\n(1 = introverted, 5 = extroverted', bg="medium sea green", fg="white",
							  font=QUESTION_FONT).place(relx=0.05, rely=0.75, anchor=W)

		Radiobutton(self, text="1", bg="medium sea green", selectcolor="medium sea green",
								  activebackground="medium sea green", variable=introvertextrovert, value=1, font=BUTTON_FONT, tristatevalue=0).place(relx=0.1, rely=0.85, anchor=W)

		Radiobutton(self, text="2", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=2, font=BUTTON_FONT, tristatevalue=0).place(relx=0.25, rely=0.85, anchor=W)

		Radiobutton(self, text="3", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=3, font=BUTTON_FONT, tristatevalue=0).place(relx=0.4, rely=0.85, anchor=W)

		Radiobutton(self, text="4", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=4, font=BUTTON_FONT, tristatevalue=0).place(relx=0.55, rely=0.85, anchor=W)

		Radiobutton(self, text="5", bg="medium sea green", selectcolor="medium sea green",
								   activebackground="medium sea green", variable=introvertextrovert, value=5, font=BUTTON_FONT, tristatevalue=0).place(relx=0.7, rely=0.85, anchor=W)




		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage4), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Finish!", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage6), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 5/5', bg="medium sea green",  font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)


	def save(self):
		global learningstyle
		global workwithothers
		#global patience
		global introvertextrovert
		questionnaireAnswers["learningstyle"] = learningstyle.get()
		questionnaireAnswers["workwithothers"] = workwithothers.get()
		#questionnaireAnswers["patience"] = patience.get()
		questionnaireAnswers["introvertextrovert"] = introvertextrovert.get()

class QuestionPage6(Frame):

	def __init__(self, parent, controller):


		Frame.__init__(self, parent)

		Label(self, text='Just the test button right now,\nThis should link to the profile page.', bg="medium sea green", fg="white",
			  font=("Roboto", 18, "bold")).place(relx=0.05, rely=0.3, anchor=W)



		test = Button(self, text="Test", highlightbackground="medium sea green", padx=10,
					  command=lambda: print(questionnaireAnswers))
		test.pack()

		back = Button(self, text="Back", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage2), self.save()])
		back.place(relx=0.0, rely=1.0, anchor=SW)

		next = Button(self, text="Next", highlightbackground="medium sea green", padx=10,
				  command=lambda: [controller.show_frame(QuestionPage3), self.save()])
		next.place(relx=1.0, rely=1.0, anchor=SE)

		pagenum = Label(self, text='pg 6', bg="medium sea green",  font=BUTTON_FONT)
		pagenum.place(relx=1.0, rely=0.0, anchor=NE)


	def save(self):
		pass

# Contains the current users profile page.
# The user can see their name as well as some of their information.
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

		# Get current users full (first and last) name
		fullname = c.current_user.first + " " + c.current_user.last
		# maj = "Career Field: " + test_account.

		lbl1 = Label(fr1, text="Olivia WhetherSpooner", bg="white", fg="sea green", font=(
			"Helvetica", 46, "bold"))
		lbl1.place(relx=0.0, rely=0.15, anchor=W)

		# Random line for looks
		fr2 = Frame(fr1, width = 570, height = 5, bg = 'black')
		fr2.place(relx=0.0, rely=0.25, anchor=W)

		# Displays the users bio
		lbl2 = Label(fr1, text=test_account.bio, bg="white", fg="gray20", 
			font=INFO_FONT, wraplength = 570, justify = CENTER)
		lbl2.place(relx=0.5, rely=0.35, anchor=CENTER)

		# More about me sections 
		Label(fr1, text="A little more about me...", bg="white", fg="black", font=TAB_FONT).place(relx=0.2, rely=0.50, anchor=CENTER)
		# Gender label and answer from current user
		Label(fr1, text="Gender: ", bg="white", fg="black", font=INFO_FONT).place(relx=0.02, rely=0.56, anchor=W)
		Label(fr1, text=test_account.gender, bg="white", fg="gray20", font=INFO_FONT).place(relx=0.13, rely=0.56, anchor=W)
		# Career Field and answer from current user
		Label(fr1, text="Career Field:", bg="white", fg="black", font=INFO_FONT).place(relx=0.02, rely=0.62, anchor=W)
		Label(fr1, text="Computer and Information Science", bg="white", fg="gray20", font=INFO_FONT).place(relx=0.185, rely=0.62, anchor=W)

		Label(fr1, text="Something else:", bg="white", fg="black", font=INFO_FONT).place(relx=0.02, rely=0.68, anchor=W)
		Label(fr1, text="is here and so on", bg="white", fg="gray20", font=INFO_FONT).place(relx=0.24, rely=0.68, anchor=W)

		'''
		Next labels x and ys
		relx=0.02, rely=0.74
		relx=0.02, rely=0.80
		relx=0.02, rely=0.86
		relx=0.02, rely=0.92
		'''

# Function used to show mentors/mentees information after the connect
# button from the HomePage is clicked.
def connect(first, last, email):
	#Create new smaller window
	top = Toplevel()
	top.geometry('280x170')
	top.resizable(False, False)
	top.title("Match Information")
	top.config(bg='medium sea green')

	#Combine first and last name
	name = first + " " + last
	l = Label(top, text=name, fg="White", bg = 'medium sea green', font=INFO_FONT)
	l.place(relx=0.05, rely=0.13, anchor=W)
	fr1 = Frame(top, width=600, height=5, bg='white')
	fr1.place(relx=0.05, rely=0.25, anchor=CENTER)

	#Add "Contact By" with email to new string
	em = "Contact By: " + email
	l2 = Label(top, text=em, fg="White", bg = 'medium sea green', font=SMALL_FONT)
	l2.place(relx=0.05, rely=0.4, anchor=W)

	#Button that will exit out of this small window
	b = Button(top, text="Back", padx=50, highlightbackground='medium sea green', command=lambda: exit(top))
	b.place(relx=0.5, rely=0.7, anchor=CENTER)

# Helper function for connect that will close the window after a button
# is clicked
def exit(top):
	top.destroy()

win = start()
win.geometry('600x425')
win.title("Mentor Meeter")
win.config(bg='medium sea green')
win.mainloop()

'''
RESOURCES:
https://pythonprogramming.net/change-show-new-frame-tkinter/

'''
