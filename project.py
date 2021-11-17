import math
def primenumber(p):
	if p<1:
	    pass
	else:
	    for i in range(2,p):
                    if(p%i==0):
                            print(p,"not prime")
                            break;
                    else:
                                print(p,"is prime")


num=int(input("Enter a number.."))
sqrt=math.sqrt(num)
cube=math.pow(num,3)
f=math.factorial(num)
square=math.pow(num,2)
print("square root ",sqrt)
print("cube of ",cube)
print("square of number",square)
print("factorial ",f)
primenumber(num)