import os
from os import system
system("clear")

name = input("What's your name? ")
print("Hello " + name + ". Nice to meet you! Welcome to my tempurature converter. If you live in the U.S. it will convert from farenheight.")

temptype = input("Do you live in the U.S.? ")

temp = int(input ("what is your temp?:"))


if temptype == 'yes':
    mathf = str (((temp) - 32) * 5 / 9)
    print ("Your temp in Celcius is " + mathf + "." )
else:
    mathc = str (((temp) * 9 / 5) + 32)
    print ("Your temp in farenheight is " + mathc + ".")

