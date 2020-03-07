"""
CIS 422 Project 2: Compatibility Algorithm File

Last Modified: 3/4/20

Authors: Mikayla Campbell
"""

# All of the program's users
users = []

percent_scale = [100/18, 75/18, 50/18, 25/18, 0]
# Divide percent by 18 for each question because there are 18 questions
	# # Max 4 off
	# # 4 = 0%
	# # 3 = 25%
	# # 2 = 50%
	# # 1 = 75%
	# # 0 = 100%

class User:
	"""Class that stores each user's information"""
	def __init__(self, user_type, first, last, age, gender, questionnaire, bio, email, username, password):
	 	self.user_type = user_type # int (Mentor = 1, mentee = 0)
	 	self.first = first # string
	 	self.last = last # string
	 	self.age = age # int
	 	self.gender = gender # string
	 	self.q = questionnaire # list of numbers (Starts at 1)
	 	self.bio = bio # string
	 	self.email = email # string
	 	self.user_matches = [["", 0],["", 0], ["", 0], ["", 0], ["", 0]] # User Matches (Sorted)
	 	#self.user_compats = [0, 0, 0, 0, 0] # User Matches corresponding %
	 	self.username = username # string
	 	self.password = password #string

	def __str__(self):
		return self.first + ' ' + self.last

	def __repr__(self):
		return "User({} {} {} {} {} {} {} {} {})".format(self.first, self.last,
			self.age, self.gender, self.q, self.bio, self.email,
			self.username, self.password)

current_user = User(0, "", "", 0, "", {}, "", "", "", "")

def login_check(username, password):
	"""Checks login credentials"""
	for user in users:
		if user.username == username and user.password == password:
			current_user = user
			pref_check(current_user)
			compat()
			return 1
	return 0


def equal_q_answer(user, q_num, count):
	"""Mentor and mentee must have equal answers"""
	percent = abs(current_user.q[q_num] - user.q[q_num])
	real_percent = percent_scale[percent]
	current_user.user_matches[count][1] += real_percent


def equal_or_higher(user, q_num, count):
	"""Mentor needs to be 1 or higher than mentee or equal"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent >= 0:
		real_percent = percent_scale[percent]
		current_user.user_matches[count][1] += real_percent


def equal_or_lower(user, q_num, count):
	"""Mentee needs to be 1 or lowerer than mentor or equal"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent <= 0:
		real_percent = percent_scale[abs(percent)]
		current_user.user_matches[count][1] += real_percent


def higher(user, q_num, count):
	"""Mentor needs to be 1 or higher than mentee"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent > 0:
		real_percent = percent_scale[percent - 1]
		current_user.user_matches[count][1] += real_percent


def lower(user, q_num, count):
	"""Mentee needs to be 1 or lower than mentor"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent < 0:
		real_percent = percent_scale[abs(abs(percent) - 1)]
		current_user.user_matches[count][1] += real_percent


def pref_check(current_user):
	"""Remove users who do not fit the current user's preferenes

	0) Gender (Male, Female, Other)
	1) Who do you want to be matched with? (Male, Female, Other)
	2) What is your career field? (47)
	3) Age Range (1 - 5)
	"""

	user1 = User(0, "Phillipe", "Orozco", 20, "Male", [1, 3, "Computer Science", 4, 4, 3, 5, 5, 4, 5, 2, 3, 4, 4, 3, 4, 2, 1, 3, 4, 1, 2], "Hiyo", "phillipe@gmail.com", "philoroz", "pickles9")
	user2 = User(0, "Olivia", "Pannell", 21, "Female", [2, 3, "Computer Science", 4, 3, 2, 4, 5, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2], "Hello", "olivia@gmail.com", "olp", "anniepie98")
	user3 = User(0, "Jose", "West", 23, "Male", [1, 3, "Computer Science", 5, 3, 5, 3, 3, 1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 3, 4, 1, 4], "Hey", "jose@gmail.com", "josewt", "glassesguy65")
	user4 = User(0, "Taylor", "Verney", 22, "Non-binary/Queer", [3, 3, "Computer Science", 1, 2, 1, 1, 2, 2, 4, 3, 4, 3, 4, 4, 4, 3, 4, 4, 3, 1, 3], "Heyo", "taylor@gmail.com", "tayvey", "cheezitsaremylove74")
	user5 = User(0, "Pablo", "Garcia", 19, "Male", [1, 3, "Computer Science", 3, 1, 3, 4, 1, 4, 5, 2, 3, 4, 2, 4, 2, 4, 2, 3, 4, 1, 3], "Greetings", "pablo@gmail.com", "pabgar", "9000goo")

	users.append(user1)
	users.append(user2)
	users.append(user3)
	users.append(user4)
	users.append(user5)

	age_ranges = [[18, 25], [25, 30], [30, 40], [40, 60], [60, 130]]

	count = 0
	for user in users:
		if user.user_type != current_user.user_type: # Make sure mentors are assigned to mentees and vice versa
			if user.q[1] == 3 or user.q[1] == current_user.q[0]: # Make sure gender prefeerence match up
				if user.q[2] == current_user.q[2]:
					if user.age >= age_ranges[current_user.q[3] - 1][0] and user.age <= age_ranges[current_user.q[3] - 1][1]:
						if len(current_user.user_matches) <= 5:
							current_user.user_matches[count][1] = 0
							current_user.usermatches[count][0] = user
						else:
							match = []
							match.append(user)
							match.append(0)
							current_user.user_matches.append(match)
						count += 1


def compat():
	"""Compute compatibility amongst users"""

	# If the current user is a mentor
	if current_user.user_type:
		count = 0
		for user in users:
			if user != current_user:
				# 4) What is your experience level in your field? (1 - 5)
				# 5) How good are your networking skills? (1 - 5)
				# 6) How good are your organizational skills? (1 - 5)
				for i in range(4, 7):
					higher(user, i, count)

				# 7) How good are your organizational skills? (1 - 5)
				# 8) How good are your time management skills? (1 - 5)
				# 9) What is your work ethic? (1 - 5)
				# 10) How flexible/adaptable are you?
				# 11) Problem Solving skills (1 - 5)
				# 12) Ability to work with coworkers/other people (1 - 5)
				# 13) Self motivation (1 - 5)
				# 14) Professionalism (1 - 5)
				for i in range(7, 15):
					equal_or_higher(user, i, count)

				# 15) How much do you value integrity?
				equal_or_answer(user, 15, count)

				# 16) How patient are you? (1 - 5)
				equal_or_higher(user, 16, count)

				# 17) How social are you? (1 - 5)
				# 18) What is your learning style? (1 - 5)
				# 19) Career goals (1 - 5)
				for i in range(17, 20):
					equal_q_answer(user, 19, count)

				# 20) How much time do you to invest in your mentor-mentee relationship? (1 = low, 5 = high)
				# 21) What kind of work do you want to do? (1 - 5)
				for i in range(20, 22):
					equal_q_answer(user, i, count)

				# No one is 100% compatible -- account for that
				if current_user.user_matches[count][1] >= 100:
					current_user.user_matches[count][1] = 99.0
				else:
					current_user.user_matches[count][1] = round(current_user.user_matches[count][1], 1)

				count += 1
	else:
		for user in users:
			if user != current_user:
				count = 0
				# 4) What is your experience level in your field? (1 - 5)
				# 5) How good are your networking skills? (1 - 5)
				# 6) How good are your organizational skills? (1 - 5)
				for i in range(4, 7):
					lower(user, i, count)

				# 7) How good are your organizational skills? (1 - 5)
				# 8) How good are your time management skills? (1 - 5)
				# 9) What is your work ethic? (1 - 5)
				# 10) How flexible/adaptable are you?
				# 11) Problem Solving skills (1 - 5)
				# 12) Ability to work with coworkers/other people (1 - 5)
				# 13) Self motivation (1 - 5)
				# 14) Professionalism (1 - 5)
				for i in range(7, 15):
					equal_or_lower(user, i, count)

				# 15) How much do you value integrity?
				equal_q_answer(user, 15, count)
				
				# 16) How patient are you? (1 - 5)
				equal_or_lower(user, 16, count)

				# 17) How social are you? (1 - 5)
				# 18) What is your learning style? (1 - 5)
				# 19) Career goals (1 - 5)
				for i in range(17, 20):
					equal_or_lower(user, 19, count)

				# 20) How much time do you to invest in your mentor-mentee relationship? (1 = low, 5 = high)
				# 21) What kind of work do you want to do? (1 - 5)
				for i in range(20, 22):
					equal_q_answer(user, i, count)

				# No one is 100% compatible -- account for that
				if current_user.user_matches[count][1] >= 100:
					current_user.user_matches[count][1] = 99.0
				else:
					current_user.user_matches[count][1] = round(current_user.user_matches[count][1], 1)

				count += 1

	sort_matches()


def sort_matches():
	"""Sort matches by % compatibility"""
	for i in range(len(current_user.user_matches)):
		for j in range(len(current_user.user_matches) - i - 1):
			if current_user.user_matches[j][1] < current_user.user_matches[j + 1][1]:
				current_user.user_matches[j], current_user.user_matches[j + 1] = current_user.user_matches[j + 1], current_user.user_matches[j]


# def main():
# 	"""
# 	Test it
# 	"""
# 	current_user = User(1, "Mikayla", "Campbell", 20, "Female", [2, 3, "Computer Science", 4, 4, 3, 5, 5, 4, 5, 4, 5, 4, 4, 4, 5, 5, 4, 5, 3, 1, 4], "Hi", "mikayla@gmail.com", "hewantshiscar", "bob2")
# 	print(current_user.q)
# 	user1 = User(0, "Phillipe", "Orozco", 20, "Male", [1, 3, "Computer Science", 4, 4, 3, 5, 5, 4, 5, 2, 3, 4, 4, 3, 4, 2, 1, 3, 4, 1, 2], "Hiyo", "phillipe@gmail.com", "philoroz", "pickles9")
# 	user2 = User(0, "Olivia", "Pannell", 21, "Female", [2, 3, "Computer Science", 4, 3, 2, 4, 5, 4, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2], "Hello", "olivia@gmail.com", "olp", "anniepie98")
# 	user3 = User(0, "Jose", "West", 23, "Male", [1, 3, "Computer Science", 5, 3, 5, 3, 3, 1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 3, 4, 1, 4], "Hey", "jose@gmail.com", "josewt", "glassesguy65")
# 	user4 = User(0, "Taylor", "Verney", 22, "Non-binary/Queer", [3, 3, "Computer Science", 1, 2, 1, 1, 2, 2, 4, 3, 4, 3, 4, 4, 4, 3, 4, 4, 3, 1, 3], "Heyo", "taylor@gmail.com", "tayvey", "cheezitsaremylove74")
# 	user5 = User(0, "Pablo", "Garcia", 19, "Male", [1, 3, "Computer Science", 3, 1, 3, 4, 1, 4, 5, 2, 3, 4, 2, 4, 2, 4, 2, 3, 4, 1, 3], "Greetings", "pablo@gmail.com", "pabgar", "9000goo")

# 	users.append(current_user)
# 	users.append(user1)
# 	users.append(user2)
# 	users.append(user3)
# 	users.append(user4)
# 	users.append(user5)

# 	pref_check(current_user)
# 	compat()

# 	count = 0
# 	for i in current_user.user_matches:
# 		print(i, current_user.matches[i])
# 		count += 1

# 	return 1

# if __name__ == "__main__":
# 	main()
