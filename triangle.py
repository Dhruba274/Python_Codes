def classify_triangle(a, b, c):
    sides = sorted([a, b, c])

    if sides[0] + sides[1] <= sides[2]:
        return 'Invalid Triangle'
    elif sides[0] == sides[1] == sides[2]:
        return 'Equilateral Triangle'
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return 'Isosceles Triangle'
    else:
        return 'Scalene Triangle'

a = float(input('Enter the length of side a: '))
b = float(input('Enter the length of side b: '))
c = float(input('Enter the length of side c: '))

print(classify_triangle(a, b, c))