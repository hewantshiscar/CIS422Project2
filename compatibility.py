"""
CIS 422 Project 2 : Compatibility Algorithm File

Last Modified: 2/29/20

Authors: Mikayla Campbell, Bethany Van Meter
"""

# All of the program's users
users = []

percent_scale = [100/7, 75/7, 50/7, 25/7, 0]
# Divide percent by 7 for each question because there are 7 questions
	# # Max 4 off
	# # 4 = 0%
	# # 3 = 25%
	# # 2 = 50%
	# # 1 = 75%
	# # 0 = 100%

class User:
	"""

	"""
	def __init__(self, user_type, first, last, age, gender, questionnaire, bio, email, username, password):
	 	self.user_type = user_type # int (Mentor = 1, mentee = 0)
	 	self.first = first # string
	 	self.last = last # string
	 	self.age = age # string
	 	self.gender = gender # string
	 	self.q = questionnaire # list of numbers (Starts at 1)
	 	self.bio = bio # string
	 	self.email = email # string
	 	self.user_matches = {} # key = user, value = % compatibile
	 	self.username = username # string
	 	self.password = password #string

	def __str__(self):
		return self.username

	def __repr__(self):
		return "{} {}".format(self.first, self.last)


def equal_q_answer(current_user, user, q_num, matches):
	"""Mentor and mentee must have equal answers"""
	percent = abs(current_user.q[q_num] - user.q[q_num])
	real_percent = percent_scale[percent]
	matches[user] += real_percent


def equal_or_higer(current_user, user, q_num, matches):
	"""Mentor needs to be 1 or higher than mentee or equal"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent >= 0:
		real_percent = percent_scale[percent]
		matches[user] += real_percent


def equal_or_lower(current_user, user, q_num, matches):
	"""Mentee needs to be 1 or lowerer than mentor or equal"""
	percent = current_user.q[q_num] - user.q[q-num]
	if percent <= 0:
		real_percent = percent_scale[abs(percent)]
		matches[user] += real_percent


def higher(current_user, user, q_num, matches):
	"""Mentor needs to be 1 or higher than mentee"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent > 0:
		real_percent = percent_scale[percent - 1]
		matches[user] += real_percent


def lower(current_user, user, q_num, matches):
	"""Mentee needs to be 1 or lower than mentor"""
	percent = current_user.q[q_num] - user.q[q_num]
	if percent < 0:
		real_percent = percent_scale[abs(abs(percent) - 1)]
		matches[user] += real_percent


def pref_check(current_user):
	"""Remove users who do not fit the current user's preferenes

	0) Gender (Male, Female, Other)
	1) Who do you want to be matched with? (Male, Female, Other)
	2) What is your career field? (47)
	"""

	pref_matches = {}

	for user in users:
		if user.user_type != current_user.user_type: # Make sure mentors are assigned to mentees and vice versa
			if user.q[1] == 3 or user.q[1] == current_user.q[0]: # Make sure gender prefeerence match up
				if user.q[2] == current_user.q[2]:
					pref_matches[user] = 0

	return pref_matches


def compat(current_user, matches):
	"""Compute compatibility amongst users"""

	# If the current user is a mentor
	if current_user.user_type:
		for user in matches:
			# 3) How much time do you to invest in your mentor-mentee relationship? (1 = low, 5 = high)
			equal_q_answer(current_user, user, 3, matches)
			# 4) What is your experience level in your field? (1 - 5)
			higher(current_user, user, 4, matches)
			# 5) How good are your networking skills? (1 - 5)
			higher(current_user, user, 5, matches)
			# 6) How good are your organizational skills? (1 - 5)
			higher(current_user, user, 6, matches)
			# 7) How much do you value integrity? (1 - 5)
			equal_q_answer(current_user, user, 7, matches)
			# 8) How patient are you? (1 - 5)
			equal_or_higer(current_user, user, 8, matches)
			# 9) What is your learning style? (1 - 5)
			equal_q_answer(current_user, user, 9, matches)

			# No one is 100% compatible -- account for that
			if matches[user] >= 100:
				matches[user] = 99.0
			else:
				matches[user] = round(matches[user], 1)
	else:
		for user in matches:
			# 3) How much time do you to invest in your mentor-mentee relationship? (1 = low, 5 = high)
			equal_q_answer(current_user, user, 3, matches)
			# 4) What is your experience level in your field? (1 - 5)
			lower(current_user, user, 4, matches)
			# 5) How good are your networking skills? (1 - 5)
			lower(current_user, user, 5, matches)
			# 6) How good are your organizational skills? (1 - 5)
			lower(current_user, user, 6, matches)
			# 7) How much do you value integrity? (1 - 5)
			equal_q_answer(current_user, user, 7, matches)
			# 8) How patient are you? (1 - 5)
			equal_or_lower(current_user, user, 8, matches)
			# 9) What is your learning style? (1 - 5)
			equal_q_answer(current_user, user, 9, matches)

			# No one is 100% compatible -- account for that
			if matches[user] >= 100:
				matches[user] = 99.0
			else:
				matches[user] = round(matches[user], 1)

	current_user.matches = matches


# def main():
# 	"""
# 	Test it
# 	"""
# 	current_user = User(1, "Mikayla", "Campbell", 20, "Female", [2, 3, 11, 4, 4, 3, 5, 5, 4, 5], "Hi", "mikayla@gmail.com", "hewantshiscar")
# 	user1 = User(0, "Phillipe", "Orozco", 20, "Male", [1, 3, 11, 4, 4, 3, 5, 5, 4, 5], "Hiyo", "phillipe@gmail.com", "philoroz")
# 	user2 = User(0, "Olivia", "Pannell", 21, "Female", [2, 3, 11, 4, 3, 2, 4, 5, 4, 5], "Hello", "olivia@gmail.com", "olp")
# 	user3 = User(0, "Jose", "West", 23, "Male", [1, 3, 11, 5, 3, 5, 3, 3, 1, 1], "Hey", "jose@gmail.com", "josewt")
# 	user4 = User(0, "Taylor", "Verney", 22, "Non-binary/Queer", [3, 3, 11, 1, 2, 1, 1, 2, 2, 4], "Heyo", "taylor@gmail.com", "tayvey")
# 	user5 = User(0, "Pablo", "Garcia", 19, "Male", [1, 3, 11, 3, 1, 3, 4, 1, 4, 5], "Greetings", "pablo@gmail.com", "pabgar")

# 	users.append(current_user)
# 	users.append(user1)
# 	users.append(user2)
# 	users.append(user3)
# 	users.append(user4)
# 	users.append(user5)

# 	current_matches = pref_check(current_user)
# 	compat(current_user, current_matches)

# 	print(current_user.matches)

# 	return 1

# if __name__ == "__main__":
# 	main()
