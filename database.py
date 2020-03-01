"""
CIS 422 Project 2 File I/O

Description: putting in information for mentors and mentees

Date Last Modified: 2/27/20

Authors: James Kang
"""

#import compatibility
import mysql.connector
from compatibility import *


# the function is to create a mentor in our system (will be called in create account if the person is a mentor
def create_mentor(User):
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()

	insert_s = (
		"INSERT INTO mentor(first, last, age, gender, q, bio, email, user_matches, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
	data = (
	str(User.first), str(User.last), str(User.age), str(User.gender), str(User.q), str(User.bio), str(User.email),
	str(User.user_matches), str(User.username), str(User.password))

	mycursor.execute(insert_s, data)

	mydb.commit()


# the function is to create a mentor in our system (will be called in create account if the person is a mentee
def create_mentee(User):
	# connecting to our database
	mydb = mysql.connector.connect(host="ix.cs.uoregon.edu", user="guest", passwd="guest", database="mentor",
								   port="3141")
	# using a cursor to add into the databse
	mycursor = mydb.cursor()

	insert_s = ("INSERT INTO mentee(first, last, age, gender, q, bio, email, user_matches, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
	data = (str(User.first), str(User.last), str(User.age), str(User.gender), str(User.q), str(User.bio), str(User.email), str(User.user_matches), str(User.username), str(User.password))

	mycursor.execute(insert_s, data)

	mydb.commit()

#def creat_account(p: User):
#	if p.user_type:
#		create_mentor(p)
#	else:
#		create_mentee(p)

#def log_in(email: str, password: str):


#test
#user1 = User("Phillipe", "Orozco", '20', "Male", "20,20,20,20,20", "Hiyo", "phillipe@gmail.com", "hierw", "philoroz", "ufhwfwe")
#create_mentee(user1)