#ask user for name
name=input("what is your name?")

#ask user their age
age=input("how old are you?")
# ask user for city
city=input("what city do you live in?")
# ask user what they enjoy
love=input("what do you love doing ?")
#create outout text
string="your name  is{} and you are {} years old and your live in {} and you love {}"
output=string.format(name,age,city,love)
# print output to screen
print(output)
