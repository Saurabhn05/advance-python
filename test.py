# simple intrest calculation

def simple_intrest(p,n,r):
    i=(p*n*r)/100
    amt = p+i
    return {"intrest": i,"amount":amt}

# take input from users in console
p = float(input("Please enter Principle in INR :"))
n = int(input("enter number of years :"))
r = float(input("please enter rate of intrest in %p.a :"))

# Calculate intrest and amount
results = simple_intrest(p,n,r)

# Print the result
print(results)
