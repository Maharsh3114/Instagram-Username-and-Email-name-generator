# Instagram-Username-and-Email-name-generator

import random
print(" Welcome to the instagram username and Gmail generator!!")
print("Enter your first name : ")
a = input()
print("Enter your last name : ")
b = input()
d = random.randint(120,490)
z = str(d)
m = random.randint(0000,9999)
n = str(m)
print("Your instagram username is",a.lower()+"_"+z)
print("Your gmail account name is ",a.lower()+b.lower()+n+"@"+"gmail.com")
