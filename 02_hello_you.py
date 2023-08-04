#Ask user for name
name=input("Enter your name: ")

#Ask user for the age
age=input("Enter your age: ")

#Ask city
city= input("Enter the city name you live in: ")

#Ask what they enjoy
like=input("Enter what you like to do:")

#Create output text
sentence="Your name is {} and you are {} years old. you live in {} and you love {}"
output=sentence.format(name,age,city,like)

#Print output
print(output)
