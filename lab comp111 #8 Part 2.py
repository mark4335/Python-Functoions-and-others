# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 8 Part 2
n=[]
a= int(input("How many payments are there: "))
for i in range (a):
    b = int(input("Enter a payment: "))
    n.append(b)
s=sum(n)

print("Number of payments :{}".format(a))
print("Total amount : {}".format(s))
m=max(n)
print("Maximum amount : {}".format(m))
n.sort(reverse=True)
print("Payments from high to low: {}".format(n))

