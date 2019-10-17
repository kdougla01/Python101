print ("Welcome to the program")

name = input("What is your name? ")

print (f"Well hello, {name}")

age = int(input("What is your age? "))

if age >= 18:
	print ("You must be an adult then!")
elif age >= 13:
	print ("You must be a teenager")
else:
	print ("You are a child")