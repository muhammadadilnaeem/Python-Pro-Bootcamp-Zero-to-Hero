
# import main_utils

# # from main_utils import *

# print("\n-------------")
# print(main_utils.add(5,7))
# print("\n-------------")
# print(main_utils.subtract(10,7))
# print("\n-------------")
# print(main_utils.multiply(5000,7))
# print("\n-------------")

from geometry import triangle,circle,square

print("---------------------------------------------------------------")
print(f"\nThe area of cicle with radius 5 will be 💨 {circle.area(5)}")

print("---------------------------------------------------------------")
print(f"\nThe circumference of cicle with radius 10 will be 💨 {circle.circumference(10)}")

print("---------------------------------------------------------------")

print(f"\nThe area of square with side length 20 will be 💨 {square.area(20)}")
print("---------------------------------------------------------------")

print(f"\nThe perimeter of square with side length 40 will be 💨 {square.perimeter(40)}")
print("---------------------------------------------------------------")

print(f"\nThe area of triangle with base 50 and height 60 will be 💨 {triangle.area(50,60)}")
print("---------------------------------------------------------------")

print(f"\nThe perimeter of triangle with side1=70, side2=80 and side3=90 length 40 will be 💨 {triangle.perimeter(70,80,90)}")
print("---------------------------------------------------------------")
