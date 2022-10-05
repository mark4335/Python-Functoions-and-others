# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 7 Part 2

a=int(input("Enter the first gross pay :"))
b=int(input("Enter the first gross pay :"))
c=int(input("Enter the first gross pay :"))

#net pay
def f1 (gp1,gp2,gp3):
    return(gp1+gp2+gp3)
t0t= (f1(a,b,c))

def f2 (gp,ded):
    return (gp*ded)
n_p1 = f2(a,0.2)
n_p2 = f2(b,.25)
n_p3 = f2(c,.4)
# f2 is ^_^



print("The first net pay is {}".format(n_p1))
print("The second net pay is {}".format(n_p2))
print("The third net pay is {}".format(n_p3))
print("The Total net pay is {}".format(n_p1+n_p2+n_p3))
print("The Total net pay is {}".format(t0t))
