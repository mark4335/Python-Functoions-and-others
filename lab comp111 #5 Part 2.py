# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 5 Part 2


c=0
d =0
a = int(input("How many color do you want to enter?:"))
for x in range(a):
  b=input("What is your favorite color?") 
  if b=="blue":
    c +=1
  else:
    b!="blue"
    d +=1

print("Blue color entered:{}".format(c))
print("Blue color not entered:{}".format(d))


