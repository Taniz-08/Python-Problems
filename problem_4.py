#Find the maximum of two or three numbers


a = int(input("Enter the Number:")) # 12
b = int(input("Enter the Number:")) # 4
c = int(input("Enter the Number:"))# 5


if a > b & c:  #12 > 4 & 5 
    print(f"{a} is big number")
elif b > c & a:
    print(f"{b} is big number")
else:
    print(f"{c} is bigger")