# Problem 2.01 calculate_bmi( weight, height)
def calculate_bmi( weight, height):
    if height <= 0 or height == None or weight == None:
        return None
    height = height/100
    BMI = weight/(height ** 2)
    BMI_Round = round(BMI, 1)
    return BMI_Round

calculate_bmi (2.5,50)
calculate_bmi (50 ,150)
calculate_bmi (43.5 ,142.3)


# Problem 2.02 position_velocity( vo, t)
def position_velocity(vo, t):
    g = 9.81
    position = round(vo*t - 1/2*(g* t**2), 3)
    velocity = round(vo - g*t, 3)
    return position, velocity 

print(position_velocity(5.0, 0))
print(position_velocity(10.0, 1))
print(position_velocity(5.886, 0.3))

# Problem 2.03 decay(a, t)
import math
def decay(a,t):
    x = math.exp(-a*t)*math.cos(a*t)
    return x
print (decay(2, 0))
print (decay(2, 0.5))

# Problem 2.04 describe_bmi( bmi )
def describe_bmi(bmi):
    if bmi <= 0:
        return None
    elif bmi < 18.5:
        print("nutritional deficiency")
    elif bmi >= 18.5 and bmi < 23:
        print("low risk")
    elif bmi >= 23 and bmi < 27.5:
        print("moderate risk")
    elif bmi >= 27.5:
        print("high risk")

describe_bmi(18)
describe_bmi(20) 
describe_bmi(24)
describe_bmi(27.5)

# Problem 2.05 is_positive_even(n)
def is_positive_even(n):
    if n % 2 == 0 and n >= 0:
        return True
    else:
        return False
print(is_positive_even(-2))
print(is_positive_even(2))
print(is_positive_even(3))

# Problem 2.06 letter_grade( mark )
def letter_grade(mark):
    if mark < 0 or mark > 100:
        return None
    elif mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'E'
        
letter_grade(102)
letter_grade(100)
letter_grade(83)
letter_grade(75)
letter_grade(67)
letter_grade(52)
letter_grade(-2)

# Problem 2.07 largest_area(s,u,v)
def largest_area(s,u,v):
    area1 = u*v
    area2 = (s-u)*v
    area3 = (s-v)*u
    area4 = (s-u)*(s-v)
    maxarea= None

    if s < 0 or u <0 or v < 0:
        return None
    elif u > s or v > s:
        return None
    elif area1 > area2 and area1 > area3 and area1 > area4:
        maxarea = area1
    elif area2 > area1 and area2 > area3 and area2 > area4:
        maxarea = area2
    elif area3 > area1 and area3 > area2 and area3 > area4:
        maxarea = area3
    else:
        maxarea = area4
    return maxarea

maxarea = largest_area(10, 3, 4)
maxarea = largest_area(10, 11, 4)
maxarea = largest_area(-10, 3, 4)