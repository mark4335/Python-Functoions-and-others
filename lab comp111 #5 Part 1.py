# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 6 Part 1



a= int(input("Enter staring pints:"))
b= int(input("Enter ending pints"))
c= int(input("Enter step value"))
print ( "{:14}{:14}{:14}{:14}".format ( 'Pints', 'Quarts', 'Gallons', 'Litres' ) )
while a > b :
    #print(a)
    a -=c
    quarts = a * 0.5
    gallons = a*0.125
    litres = a*0.473
    print("{:.2f}{:14.2f}{:14.2f}{:14.2f}".format(a,quarts,gallons,litres))




#print ( "{:14}{:14}{:14}{:14}".format ( 'Pints', 'Quarts', 'Gallons', 'Litres' ) )

#for pints in range (a,b,c):
#

