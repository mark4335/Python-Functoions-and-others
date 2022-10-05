# Name: Mark Waako
# Class: Comp111 Lab A
# Assignment 4 Part 2


# Input
i_n=int(input("Enter the total sales: "))
D_sCt1=.05
D_sCt2=.10
if i_n < 49:
    print("sales: ${}".format(i_n))
elif i_n>50 and i_n<100:
    print("Sales: ${:.2f}".format(i_n))
    print("Discount rate: {:.2f}".format(D_sCt1))
    print("Reduced price: ${:.2f}".format(i_n-(i_n * D_sCt1)))

elif i_n > 100:
    print ( "Sales: ${:.1f}".format(i_n))
    print ( "Discount rate: {:.2f}".format(D_sCt2))
    print ( "Reduced price: ${:.2f}".format(i_n-(i_n * D_sCt2)))


