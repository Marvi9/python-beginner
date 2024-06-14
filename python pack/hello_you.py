# Ask user for name

name = input("what is your name?: ")

#Ask user for age

age = input("how old are you?: ")

#Ask user for city

city = input("where do you live?: ")

#Ask user what they enjoy

love = input("what is your hobby?: ")

#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

#print output to screen
print(output)
