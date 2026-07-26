# calculate areas of shapes

# # area and perimeter of rectangle
# l=int(input("Enter length of rectangle: "))
# b=int(input("Enter breadth of rectangle: "))
# area_rectangle=l*b
# perimeter_rectangle=2*(l+b)
# print("Area of rectangle is",area_rectangle)
# print("Perimeter of rectangle is",perimeter_rectangle)

# # area and perimeter of square
# s=int(input("Enter side of square: "))
# area_square=s*s
# perimeter_square=4*s
# print("Area of square is",area_square)
# print("Perimeter of square is",perimeter_square)

# # area and perimeter of circle
# from cmath import pi


# r=int(input("Enter radius of circle: "))
# area_circle=(22/7)*r*r
# perimeter_circle=2*(22/7)*r
# print("Area of circle is",area_circle)
# print("Perimeter of circle is",perimeter_circle)

# area and perimeter of triangle
a = int(input("Enter 1st side of triangle: "))
b = int(input("Enter 2nd side of triangle: "))
c = int(input("Enter 3rd side of triangle: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Perimeter of triangle is", a + b + c)
    print("Area of triangle is", area)
else:
    print("Invalid triangle")