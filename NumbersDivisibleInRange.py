# Taking input of lower range from the user.
lower=int(input("Enter lower range limit: "))

# Taking input of upper range from the user.
upper=int(input("Enter upper range limit: "))
n=int(input("Enter the number to be divided by: "))

# Using for loop.
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
