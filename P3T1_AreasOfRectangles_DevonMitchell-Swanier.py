# Type in the length and width of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Type in length and width of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Find the areas of both rectangles
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
    print ( 'Rectangle 1 has the greater area. ')
else:
    if area2 > area1:
     print ('Rectaangle 2 has the greater area. ')
    else:
     print (' Both have the same area. ')
    
