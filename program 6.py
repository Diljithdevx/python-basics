formatter = "{} {} {} {}"

#formatter is a varible and the place holder is a string here there are 4 place holder we can fill whatever we need

print(formatter.format(1, 2, 3, 4))
#for filling pace holder first weite the varible name formmater then ArithmeticError.format and filling it with integer 
print(formatter.format("one", "two", "three", "four"))
#while flling placeholder with sentense we need two put quotes
print(formatter.format(True, False, True, False))
#while printing boolean values we dont need to put quotes
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("how", "are", "you", "man"))
