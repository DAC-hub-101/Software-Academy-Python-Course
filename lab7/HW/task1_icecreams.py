""" TASK 1:
	If the string contains the word "strawberries" or "raspberries" print the string but append "Yes!" to its end, otherwise append "No!"
"""
import re

strings = [
	'Icecream with strawberries?',
	'Icecream with blueberries?',
	'Icecream with raspberries?',
	'Icecream with strawraspberries?',
	'Icecream with berries?'
]

# YOUR CODE HERE
pathern = re.compile(r"\b(straw|rasp)berries\b")


for str in strings:
	match = pathern.search(str)
	if match:
		print(f"{str} YES!")
	else:
		print(f"{str} NO!")





# EXPECTED OUTPUT:
# Icecream with strawberries? Yes!
# Icecream with blueberries? NO!
# Icecream with raspberries? Yes!
# Icecream with strawraspberries? NO!
# Icecream with berries? Yes!