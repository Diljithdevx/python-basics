type_of_people = 10
#store the number 10 in the variable type_of _people

x = f"there are {type_of_people} type of people" 
#create a formmated string

binary = "binary"
#store the word binnary in the variable binnary

dont_binary ="dont_binary"
#store the word dont_binary in the variable dont_binary

y = f"those who know {binary} and those who {dont_binary}"
#create a formatted string. formatted sting means string where you can put variable directly inside the text


print(x)  #here we are simply printing x and y
print(y)


print(f"i said: {x}")       #here we ar eprinting x and y b using paranthisis beacuse x and y are allreay defined
print (f"i also said {y}")   #string is put inside another string while printing so we need to put ()

halarious = False
#store the boolean value false

joke_evalution = "isn't that jock was not so fun!?{}"
#create a string with placeholder{}

print(joke_evalution.format(halarious))
#put the value of halarious into {} an print it

w = "this is the left side of a string of..."
#store string in w

e = "a string with a right side."
#store string in e

print(w + e)
#join 2 string together and prints them




