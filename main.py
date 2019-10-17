print ("Welcome to Cineworld Program")

name = input("What film would you like to see? ")

print (f"You have chosen, {name}")

age = int(input("What is your age? "))

if age >= 18:
	print ("You can watch the film!")
elif age >= 13:
	print ("You must be with an adult")
else:
	print ("You are a child, you can't watch the film")